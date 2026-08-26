# Format draft — reduco-growth/content/drafts/

Fiecare fișier de draft generat de rutină respectă exact această structură, ca să știi mereu unde să
te uiți fără să citești tot fișierul.

```markdown
# Draft [id] — [pilon_serviciu] / [declanșator_psihologic]

Generat: [data]  |  Status: în așteptarea aprobării

## Postare (varianta principală)

[textul complet al postării, 900-1.400 caractere, gata de copiat]

## Variante de hook alternative (primele 2 rânduri)

1. [varianta 1]
2. [varianta 2]
3. [varianta 3]

## Cifre / placeholdere de completat

- `[X]` = [ce reprezintă, de unde iei valoarea reală]
- ...

## Checklist de aprobare (din reduco-linkedin, verifică înainte să postezi)

- [ ] Primele 2 rânduri funcționează singure, fără restul postării?
- [ ] Există cel puțin o cifră reală (placeholderele de mai sus completate)?
- [ ] Cuvântul-cheie de CTA e prezent și cu majuscule, diferit de ultimele postări?
- [ ] Zero date care ar putea identifica un client anume?
- [ ] Zero promisiuni de rezultat garantat?
- [ ] Sub 1.600 de caractere?

## Instrucțiuni de postare (pas cu pas)

1. Completează placeholderele `[X]` de mai sus cu date reale — nu posta cu placeholder rămas.
2. Alege varianta de hook (principală sau una din cele 3 alternative) — dacă ai timp, testează diferite
   hook-uri pe postări diferite din aceeași rotație, așa cum cere Faza 1 din `lead-magnet.md`.
3. Postează direct din contul LinkedIn — nu există conector automat de postare, textul se copiază manual.
4. Nu pune link în corpul postării. Dacă e nevoie de link, adaugă-l în primul comentariu, la 10-15 minute
   după publicare (nu imediat — algoritmul penalizează link-urile din comentariul instant).
5. În primele 30-60 de minute, răspunde activ la fiecare comentariu — asta contează în cele 100 de minute
   zilnice din Faza 1 a planului (`plan-status.md`).
6. Când cineva scrie cuvântul-cheie de CTA în comentarii, trimite-i în DM lista de documente / pasul
   următor promis în postare, în aceeași zi.
7. După 48-72 de ore, notează în `content-log.csv` (coloana `performanta_note`) câte comentarii/DM-uri/
   leaduri reale a generat postarea — se leagă de `tracking.csv` (leaduri din conținut) la revizuirea
   săptămânală.
8. Marchează `status_aprobare` în `content-log.csv` ca `postat` (sau `respins` cu motivul, dacă ai decis
   să nu postezi acel draft).
```
