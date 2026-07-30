"""Client for posf.ro (Platforma Online pentru Schimbarea Furnizorului), the ANRE
platform behind the electricity/gas offer comparator.

What actually works without a login, confirmed against the live site:
    - GET /broker/export/operational          -> registered network operators
    - GET /broker/export/furnizor/operational  -> registered suppliers (furnizori)
Both return an HTML table (served with a spreadsheet content-type, but the body is
plain HTML) rather than JSON, so we parse it with an HTML parser below.

What does NOT work without a browser session: the offer comparator itself
(posf.ro/comparator?comparatorType=electric) is a client-rendered app. Its
per-offer price data was not reachable through a public, unauthenticated API at
the time this was written - a plausible export endpoint returned HTTP 401. So
`fetch_offers` here is a thin, generic client you point at whatever endpoint you
find (e.g. via your browser's Network tab while using the comparator); the
supported, working path for offer data is exporting/copying results from the
comparator and loading them with `energy_pricing.importers.load_offers`.
"""

from html.parser import HTMLParser
from typing import Any

import requests

BASE_URL = "https://posf.ro"
SUPPLIERS_URL = f"{BASE_URL}/broker/export/furnizor/operational"
OPERATORS_URL = f"{BASE_URL}/broker/export/operational"
REQUEST_TIMEOUT_SECONDS = 20


class _HTMLTableParser(HTMLParser):
    """Minimal dependency-free parser for the single <table> POSF's export endpoints return."""

    def __init__(self) -> None:
        super().__init__()
        self.rows: list[list[str]] = []
        self._current_row: list[str] | None = None
        self._current_cell: list[str] | None = None
        self._in_cell = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "tr":
            self._current_row = []
        elif tag in ("td", "th"):
            self._in_cell = True
            self._current_cell = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "tr" and self._current_row is not None:
            self.rows.append(self._current_row)
            self._current_row = None
        elif tag in ("td", "th") and self._current_cell is not None:
            text = "".join(self._current_cell).strip()
            if self._current_row is not None:
                self._current_row.append(text)
            self._in_cell = False
            self._current_cell = None

    def handle_data(self, data: str) -> None:
        if self._in_cell and self._current_cell is not None:
            self._current_cell.append(data)


def _parse_html_table(html: str) -> list[dict[str, str]]:
    parser = _HTMLTableParser()
    parser.feed(html)
    if not parser.rows:
        return []
    header, *body = parser.rows
    return [dict(zip(header, row)) for row in body if row]


def _fetch_table(url: str) -> list[dict[str, str]]:
    response = requests.get(url, timeout=REQUEST_TIMEOUT_SECONDS)
    response.raise_for_status()
    return _parse_html_table(response.text)


def fetch_suppliers() -> list[dict[str, str]]:
    """Registered electricity/gas suppliers (furnizori) from POSF's public export."""
    return _fetch_table(SUPPLIERS_URL)


def fetch_network_operators() -> list[dict[str, str]]:
    """Registered network operators (distributie/transport) from POSF's public export."""
    return _fetch_table(OPERATORS_URL)


def fetch_offers(api_url: str, params: dict[str, Any] | None = None) -> list[dict[str, Any]]:
    """Fetches offer rows from a JSON endpoint you supply (see module docstring for why
    there's no hardcoded default). Expects a JSON list of objects, or a JSON object with
    the list under a top-level "offers"/"data"/"items" key.
    """
    response = requests.get(api_url, params=params, timeout=REQUEST_TIMEOUT_SECONDS)
    response.raise_for_status()
    payload = response.json()
    if isinstance(payload, list):
        return payload
    for key in ("offers", "data", "items", "results"):
        if isinstance(payload, dict) and isinstance(payload.get(key), list):
            return payload[key]
    raise ValueError(
        "Unexpected offers API response shape; expected a JSON list or an object "
        "with an 'offers'/'data'/'items'/'results' list."
    )
