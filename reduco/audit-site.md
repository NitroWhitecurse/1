# Audit tehnic și on-page reduco.ro — orientat pe conversia B2B

August 2026. Paginile au fost accesate live, cu motor Chromium, variind proxy-ul și timpul de așteptare la randare, și comparate cu `robots.txt` și metadatele fiecărei pagini.

**Fără acces la Search Console sau Analytics.** Tot ce ține de trafic, poziții și acoperire de indexare este marcat ca „de verificat acolo" — nu sunt date pe care le putem vedea din exterior.

---

## 1. Probleme tehnice, în ordinea gravității

### 1.1. Randarea e foarte lentă — risc real de indexare incompletă

**Nu este o blocare de bot.** `robots.txt` este permisiv (`User-agent: * / Allow: /`), iar meta `robots` pe fiecare pagină verificată este `index, follow`. Corect configurate amândouă.

**Dovada:** cu setări standard de randare au eșuat complet, cu eroarea *„All scraping engines failed to retrieve content from this URL"*:

- `reduco.ro/` (a reușit abia cu proxy alternativ)
- `/cine-suntem`, `/despre-noi`, `/abonamente`
- `/oferta-energie-electrica-juridic`
- `/solutii-imm`, `/audit-facturi`

Toate au reușit **doar** forțând 15 secunde de așteptare pentru JavaScript.

**Cauza, vizibilă în HTML:** pe fiecare pagină se încarcă simultan Elementor 3.29, WooCommerce, Google Site Kit, widget de chat LiveAgent, buton flotant WhatsApp, **patru formulare popup identice** și un script de cookie-consent care redă în pagină tabelul complet de cookie-uri.

Googlebot are un buget de randare finit per pagină, cu atât mai strâns pe un site fără autoritate mare. Dacă un crawler cu 15 secunde de răbdare abia intră, este rezonabil să presupunem că paginile profunde sunt indexate incomplet sau deloc.

> **De verificat în Search Console:** Inspecție URL → Testare live pe `/solutii-imm`, `/audit-facturi`, `/abonamente`; plus Core Web Vitals și PageSpeed Insights. Dacă randarea pe mobil trece de 4–5 secunde, aceasta explică singură orice problemă de indexare.

### 1.2. Paginile de ofertă juridică afișează prețuri din 2022 ca fiind curente

`/oferta-energie-electrica-juridic`, `/juridic-energie-fix`, `/oferta-gaze-juridic` au toate data ultimei modificări **12–16 iunie 2022** și afișează oferte cu perioadă de aplicare de tipul *„24.05.2022 – 31.08.2022"*, **fără nicio avertizare vizibilă pe pagină** că datele au expirat.

Un director financiar care caută „ofertă energie firmă" ajunge pe o pagină cu prețuri vechi de peste trei ani, prezentate ca actuale. Aceasta nu e o problemă de SEO, e o problemă de credibilitate — și apare exact la prima impresie.

### 1.3. `/cine-suntem` — brandul vechi, confirmat

Ultima modificare: **18 mai 2022**. Conținutul este integral despre „Comparatot", orientat spre consumatori casnici, cu întrebări de tipul „stau în chirie, pot schimba furnizorul?". Zero context B2B.

Se suprapune cu `/despre-noi`, care este **actualizată (10 noiembrie 2025), scrisă corect și relevantă inclusiv pentru firme** — menționează proiecte fotovoltaice, instalații electrice și de gaze.

**Nu există alte pagini cu brand vechi.** Restul (`/servicii`, `/audit-facturi`, `/litigii-anre`, `/racordare-energie-gaz`, `/recuperare-compensatii`, `/solutii-imm`) folosesc corect brandul Reduco.

### 1.4. `smart.reduco.ro` e un site separat, nelegat de restul

Metadate complet diferite, alt favicon, imagini găzduite pe altă infrastructură, generator diferit de WordPress — este o platformă separată, de tip no-code.

**Nu există link direct către el din pagina principală.** Butonul „Verifică dacă poți plăti mai puțin" duce spre `/comparator/`, nu spre `smart.reduco.ro`. Autoritatea acumulată pe domeniul principal nu se transferă, iar experiența de brand se rupe la trecerea între cele două.

### 1.5. Lipsește H1 pe majoritatea paginilor

Aproape toate paginile verificate încep conținutul cu H2 sau chiar H3, nu cu H1: pagina principală, `/audit-facturi`, `/litigii-anre`, `/racordare-energie-gaz`, `/recuperare-compensatii`, `/solutii-imm`, `/despre-noi`, `/cine-suntem` și toate paginile `/juridic-*`.

Excepție: articolul `/audit-facturi-energie-imm` are H1 corect. Inconsecvența indică o setare de șablon Elementor — widgetul de titlu este pus pe H2 în loc de H1 pe majoritatea paginilor — nu greșeli izolate.

---

## 2. Structură și conținut

### Canibalizare confirmată pe ~14 pagini

Cele ~9 pagini „juridic" plus ~5 „casnic" sunt un tipar combinatoric clasic. Verificate direct: `/oferta-energie-electrica-juridic`, `/juridic-energie-fix`, `/oferta-gaze-juridic`, `/juridic-gaz-variabil`, plus echivalentele din harta site-ului.

Toate au: fără H1, titluri aproape identice („Juridic Energie Fix" vs „Juridic Gaz Variabil"), conținut format doar dintr-un tabel static din 2022, fără text explicativ, fără CTA real și **fără nicio legătură cu serviciile pe care le vindem** — audit, negociere, litigii.

**Consolidare propusă:**

| De la | Către |
|---|---|
| cele ~9 pagini `/juridic-*` și `/oferta-*-juridic` | `/solutii-imm` (redirect 301) |
| cele ~5 pagini `/casnic-*` | `/compara-oferte-de-energie` și `/compara-oferte-de-gaz` |
| `/cine-suntem` | `/despre-noi` |

Dacă vrem să păstrăm funcția de comparator, se face **o singură** pagină `/comparator-energie-firme`, alimentată cu date curente — nu completată manual o dată la trei ani.

### Cea mai mare oportunitate ratată: hub-urile B2B nu se leagă între ele

**`/solutii-imm`** este o pagină foarte bine scrisă și actualizată (iulie 2025). În corpul textului face link **doar** spre `/comparator/` și `/panouri-fotovoltaice/`. Nu leagă deloc spre `/audit-facturi`, `/litigii-anre`, `/racordare-energie-gaz`, `/consultanta-prosumator` sau `/recuperare-compensatii` — exact paginile care ar trebui să capteze intenția de cumpărare pe care tot ea o generează.

**`/servicii`** leagă spre șapte pagini, dar omite `/recuperare-compensatii` și `/monitorizarea-inteligenta`, deși ambele sunt pagini complete și bine scrise.

> De verificat manual în browser: secțiunea „Servicii" din subsolul site-ului s-a extras goală pe toate paginile. Poate fi un widget nefuncțional.

### Articolele B2B noi sunt bune, dar izolate

`/audit-facturi-energie-imm` (7 august 2026) și `/schimbare-furnizor-energie-firma` (5 august 2026) sunt conținut de calitate reală: titluri cu intenție de cumpărare clară, întrebări frecvente utile, CTA corecte. Problema e că **legătura merge într-un singur sens** — paginile de serviciu nu trimit înapoi spre ele.

### `/audit-facturi` vorbește altfel decât articolele care îi trimit trafic

Pagina de conversie e scrisă la persoana a II-a, în registru rezidențial („Plătești prea mult la energie sau gaze?"), **fără nicio mențiune de firmă sau IMM** — deși articolul care îi trimite trafic este 100% B2B. Vizitatorul dă click pe un mesaj de business și aterizează pe unul casnic.

---

## 3. Ce lipsește pentru conversia B2B

- **Dovezi sociale B2B aproape inexistente.** Un singur testimonial de la un decident de firmă, pe `/recuperare-compensatii` („Andrei M., Administrator operațional… au recuperat pentru noi peste 1.200 lei"). Restul sunt de la persoane fizice. Nicio cifră agregată, niciun logo de client, nicio certificare.
- **Pagina principală nu semnalează deloc B2B.** Nici titlul (`Reduco | Oferte de energie, gaze | Reclamatii ANRE| Racordare`), nici descrierea nu conțin cuvintele firmă, IMM, persoană juridică sau business — deși pagina are o secțiune vizuală dedicată lor.
- **Formularele par identice pentru toate tipurile de client.** De verificat manual: un lead B2B ar trebui să poată introduce denumirea firmei și CUI din primul formular, ca să se califice automat.
- **CTA-uri generice** („Solicită informații", „Trimite detalii aici"), fără variantă pentru decident de firmă.
- **Pe `/abonamente`, planurile Business apar după cele Casnice**, obligând vizitatorul B2B la derulare lungă. Ancora `/abonamente#bus` există și e folosită din pagina principală — bine — dar titlul paginii e complet generic.
- **Descrierea paginii `/abonamente` conține date greșite**: *„…Recudo Casnici Lei 10 Lună…"* — numele brandului scris greșit și un preț vechi (Basic casnic e acum 15 lei). Exact ce vede omul în Google înainte să dea click.

---

## 4. Prioritizare

| Problemă | Impact | Efort | Cine |
|---|---|---|---|
| Diagnostic și optimizare viteză de randare | Mare | 6–12h | Dezvoltator |
| Consolidare + redirect 301 pentru cele ~14 pagini din 2022 | Mare | 4–8h | Dezvoltator, sau redactor dacă există plugin de redirecturi |
| Redirect `/cine-suntem` → `/despre-noi` | Mare | 0,5–1h | Oricine cu acces admin |
| Linkuri interne din `/solutii-imm` spre cele 5 pagini de serviciu | Mare | 1–2h | Redactor |
| Titlu și descriere pagină principală, cu semnal B2B | Mare | 1h | Redactor |
| Corectarea H1 la nivel de șablon Elementor | Mediu | 3–5h | Dezvoltator |
| Linkuri din `/servicii` spre compensații și monitorizare | Mediu | 0,5h | Redactor |
| Secțiune „Pentru firme" pe cele 3 pagini de serviciu principale | Mediu | 2–3h | Redactor |
| Corectarea descrierii `/abonamente` (typo + preț vechi) | Mediu | 0,5h | Redactor |
| `noindex` temporar pe paginile din 2022, până la consolidare | Mediu | 1h | Oricine cu acces admin |
| Testimoniale B2B pe `/audit-facturi`, `/litigii-anre`, `/solutii-imm` | Mediu | 2–4h | Redactor + acordul clientului |
| Linkuri bidirecționale între articolele noi și paginile de serviciu | Mic–Mediu | 1–2h | Redactor |
| Legarea `smart.reduco.ro` de site-ul principal | Mediu | 4–8h | Dezvoltator |
| Câmp „denumire firmă / CUI" în formular | Mic | 1–2h | Dezvoltator |
| CTA-uri specifice B2B | Mic | 1–2h | Redactor |

---

## 5. Ce se repară în prima săptămână, fără dezvoltator

1. Rescrie titlul și descrierea pentru pagina principală, `/abonamente`, `/audit-facturi`, `/solutii-imm`, adăugând „firmă", „IMM", „consultanță energetică business". Verificat: niciuna nu conține azi asemenea termeni.
2. Corectează descrierea `/abonamente` — typo „Recudo" și prețul vechi.
3. Adaugă linkuri din `/solutii-imm` spre `/audit-facturi`, `/litigii-anre`, `/racordare-energie-gaz`, `/consultanta-prosumator`, `/recuperare-compensatii`. Editare de text, fără cod.
4. Adaugă linkuri din `/servicii` spre `/recuperare-compensatii` și `/monitorizarea-inteligenta`.
5. Adaugă câte o secțiune scurtă „Pentru firme", de 2–3 fraze, pe `/audit-facturi`, `/litigii-anre`, `/racordare-energie-gaz`.
6. Leagă în ambele sensuri articolele B2B noi cu paginile de serviciu.
7. Pune `noindex` temporar pe cele ~14 pagini cu date din 2022, până la consolidare.
8. Cere unui client business existent un testimonial scurt și pune-l pe `/audit-facturi` și `/litigii-anre`.

---

## De verificat separat, în Search Console

- Acoperirea de indexare pentru cele ~14 pagini juridic/casnic
- Timpul mediu de randare raportat pentru paginile testate mai sus
- Dacă `smart.reduco.ro` apare ca proprietate separată sau nu e verificat deloc
