# Re-audit SEO complet — reduco.ro (ALMA SKY SRL)

**Data auditului:** 17.08.2026
**Metodă:** crawl live cu Firecrawl (map + sitemap-uri XML + scrape pagină cu pagină, inclusiv reîncercări cu `waitFor` extins și proxy stealth acolo unde randarea a fost lentă). Nu am acces la Google Analytics / Search Console — orice afirmație despre trafic, poziții sau conversii reale **trebuie verificată acolo**; nu am inventat cifre de trafic nicăieri în acest document.

Legendă folosită mai jos:
- **[VERIFICAT]** — am deschis URL-ul respectiv în această sesiune și citez ce am văzut, cu link.
- **[DEDUS]** — concluzie logică bazată pe date verificate, dar nu o observație directă 1:1.
- **[NEVERIFICABIL ÎN ACEASTĂ SESIUNE]** — am încercat, dar o limitare tehnică a instrumentelor mele m-a împiedicat să confirm; spun explicit ce trebuie verificat manual.

---

## REZUMAT EXECUTIV — Top 10 acțiuni, în ordinea impact/efort

1. **Corectează meta description de pe /abonamente** — conține literal "Recudo" (typo) și prețul vechi "10 Lună" în loc de 15 lei. [VERIFICAT] Efort: 5 minute. Impact: apare direct în Google pentru pagina cu cea mai mare valoare comercială a site-ului.
2. **Adaugă H1 pe toate paginile-cheie** — homepage și toate cele ~10 pagini B2B analizate la Secțiunea 2 nu au niciun H1 (confirmat direct pe fiecare); e o singură setare de template Elementor, corectează tot site-ul dintr-o mișcare. Excepție: `/cine-suntem` (pagina veche) chiar are H1 — bug-ul e specific template-ului nou.
3. **Repară sau elimină widget-ul rupt de pe `/consultanta-prosumator`** — secțiunea "Simulator cost implementare sistem fotovoltaic" afișează public textul de eroare "Project not found / No Lovable project found at this address". [VERIFICAT] Vizibil oricărui vizitator, foarte neprofesional pe o pagină premium.
4. **301 redirect `/cine-suntem` → `/despre-noi`** — elimină definitiv brandul vechi "Comparatot" din 2022 care încă e live și indexabil. [VERIFICAT]
5. **Leagă `/solutii-imm` (cea mai bună pagină B2B) de cele 5 pagini de servicii** — în acest moment nu duce trafic nicăieri mai departe în funnel-ul B2B. [VERIFICAT]
6. **Noindex + 301 grupat pentru ~20+ pagini "comparator" juridic/casnic cu prețuri din 24.05.2022–31.08.2022** — conținut subțire, dezinformant, care diluează autoritatea domeniului. [VERIFICAT cu citate exacte]
7. **Publică treapta Business Plus (899 lei)** — nu apare nicăieri pe site (căutare directă pe domeniu = zero rezultate). Strategia de preț există în cap, dar nu pe site.
8. **Aliniază arhitectura site-ului cu poziționarea nouă** — tehnic, site-ul e construit ca un comparator (40+ pagini `/oferte-energie/*` și `/oferte-gaz/*`, `/comparator`, subdomeniul `smart.reduco.ro` care se auto-descrie ca "Comparator Furnizori"), în timp ce mesajul de brand spune "NU suntem comparator". E o tensiune structurală, nu doar de copywriting. Detalii la Secțiunea 1 și 8 (Woo/comparator).
9. **Interlinkează bidirecțional blogul B2B nou (foarte bun, ~15 articole din iul–aug 2026) cu paginile de servicii** — există cazuri de cannibalizare parțială de cuvinte cheie (ex. `/audit-facturi` vs `/audit-facturi-energie-imm`) fără o structură clară de linking pillar↔articol.
10. **Adaugă schema FAQPage pe paginile care deja au secțiuni "Întrebări frecvente" scrise** (audit-facturi, litigii-anre, racordare-energie-gaz, consultanta-prosumator, recuperare-compensatii, solutii-imm) — conținutul există deja, lipsește doar marcajul; câștig relativ ieftin de rich snippet.

**Notă tehnică suplimentară, confirmată direct în acest audit:** capul (`<head>`) homepage-ului conține **~197.000 de caractere** de CSS inline Elementor — atât de mult încât a depășit limitele instrumentelor mele de citire. În plus, paginile `/servicii`, `/racordare-energie-gaz`, `/comanda` și `/contul-meu` au **eșuat la prima încercare de accesare** ("all scraping engines failed") și au încărcat corect abia la a doua încercare, cu timp de așteptare extins (8-10s) și proxy alternativ. Acestea sunt dovezi tehnice noi, mai puternice decât în auditul anterior, pentru problema de randare lentă — nu mai e vorba doar de homepage, ci de mai multe tipuri de pagini.

---

## 1. Inventar complet al site-ului

Sursă: `firecrawl_map` fără filtru + `sitemap_index.xml` + sitemap-urile individuale (`page-sitemap.xml`, `post-sitemap.xml`, `product-sitemap.xml`, `oferte_energie-sitemap.xml`, `oferte_gaz-sitemap.xml`, `category-sitemap.xml`, `post_tag-sitemap.xml`, `product_cat-sitemap.xml`, `author-sitemap.xml`). [VERIFICAT — toate sitemap-urile au fost deschise direct]

### 1.1 Pagini de serviciu B2B — **PĂSTREAZĂ** (nucleul afacerii)
| URL | Stare |
|---|---|
| `/` (homepage) | Păstrează, repoziționează hero (vezi Secțiunea 2) |
| `/solutii-imm` | Păstrează — cea mai bună pagină B2B, dar orfană funcțional (nu leagă spre servicii) |
| `/audit-facturi` | Păstrează |
| `/litigii-anre` | Păstrează |
| `/racordare-energie-gaz` | Păstrează |
| `/recuperare-compensatii` | Păstrează — cea mai completă pagină (singura cu testimoniale) |
| `/consultanta-prosumator` | Păstrează, repară widget rupt |
| `/servicii` | Păstrează (hub) |
| `/despre-noi` | Păstrează |
| `/abonamente` | Păstrează, corectează meta + adaugă treapta Plus |
| `/eficienta-energetica` | Păstrează |
| `/schimbarea-furnizorului` | Păstrează |
| `/panouri-fotovoltaice` | Păstrează (pillar) |
| `/pompe-de-caldura` | Păstrează |
| `/centrale-termice-rate` | Păstrează — dar hai să vedem și `/centrale-termice`, posibil duplicat (vezi 1.3) |
| `/aer-conditionat-in-rate` | Păstrează |
| `/negociere-colectiva` | Evaluează dacă e încă activă campania — dacă da, păstrează și leagă din homepage mai vizibil (deja are CTA pe homepage) |
| `/contacte` | Păstrează |
| `/intrebari-frecvente` | Păstrează, adaugă schema FAQPage |

### 1.2 Blog B2B nou — **PĂSTREAZĂ, conținut de calitate** [VERIFICAT direct pe `/blog`, `/blog/page/2`]
Serie de articole foarte recente (iulie–august 2026), clar orientate spre firme, publicate consistent (aproape zilnic în această perioadă):
- `/aer-conditionat-comercial-firme` (17.08.2026)
- `/centrala-termica-spatiu-comercial` (17.08.2026)
- `/pompa-de-caldura-pentru-firme` (14.08.2026)
- `/masuri-eficienta-energetica-firme-mici` (14.08.2026)
- `/termene-anre-plangeri` (14.08.2026)
- `/recuperare-compensatii-energie-firma` (13.08.2026)
- `/pret-fix-vs-variabil-firme` (12.08.2026)
- `/cum-citesti-factura-firmei` (12.08.2026)
- `/greseli-frecvente-contracte-furnizare` (11.08.2026)
- `/panouri-fotovoltaice-firme` (11.08.2026)
- `/ghid-atr-prosumator-firma` (11.08.2026)
- `/audit-facturi-energie-imm` (07.08.2026)
- `/reclamatie-anre-firma` (06.08.2026)
- `/legea-160-2026-prosumatori-firme` (06.08.2026)
- `/schimbare-furnizor-energie-firma` (06.08.2026)

Acesta e cel mai bun activ SEO nefolosit al site-ului momentan: conținut proaspăt, cu intenție de căutare specifică B2B ("factura energie firmă", "reclamație ANRE persoană juridică", "pompă de căldură pentru firme"), dar **fără structură de interlinking clară** spre paginile de servicii care ar trebui să convertească acest trafic (vezi Secțiunea 3).

Articole media/newsjacking mai generale, utile pt. autoritate dar cu intenție redusă de conversie B2B: `/ce-se-schimba-la-facturile-de-gaze-din-aprilie-2026...`, `/de-ce-raman-facturile-la-energie-atat-de-mari...`, `/noua-ordonanta-privind-comunitatile-de-energie...`, `/hidroelectrica-intra-in-razboiul-preturilor...`, `/schimbari-la-plata-facturilor-la-energie...`, `/romanii-pentru-care-facturile-la-energie-ar-creste...`, `/cine-a-castigat-cu-adevarat-din-plafonarea-preturilor...` — păstrează, dar nu prioritiza pentru B2B.

### 1.3 Pagini "comparator" combinatorice — **NOINDEX + 301 grupat** [VERIFICAT cu conținut exact]
Toate afișează tabele de preț **expirate din 2022**, fără avertizare de dată. Exemplu citat direct de pe `/oferta-energie-electrica-juridic` (modificat ultima dată 12.06.2022):
> „GRENERG SRL — Denumire ofertă: Smart One — Perioada de aplicare: 24.05.2022 – 31.08.2022" / „CEZ VANZARE SA — Perioadă de aplicare: 01.06.2022 – 30.06.2023"

Lista completă găsită (mai multe decât cele ~14 din auditul anterior — am găsit efectiv **peste 20**):
`/oferta-energie-electrica-juridic`, `/oferta-gaze-juridic`, `/oferta-energie-si-gaze-juridic`, `/juridic-energie-fix`, `/juridic-energie-variabil`, `/juridic-gaz-fix`, `/juridic-gaz-variabil`, `/juridic-energie-si-gaze-fix`, `/juridic-energie-si-gaz-variabil`, `/casnic-pret-fix-gaz`, `/casnic-pret-variabil-gaze`, `/casnic-pret-variabil-energie`, `/casnic-energie-si-gaze-variabil`, `/casnic-energie-si-gaz-fix`, `/oferte-energie-casnic-pret-fix`, `/energie-si-gaze`, `/energie-si-gaze-oferta`, `/energie-electrica`, `/gaze`, `/oferte-energetice`, `/comparator-energie`, `/compara-oferte-energie`, `/compara-oferte-energie-step-1`, `/compara-oferte-energie-step-2`, `/comparatot-activare-oferte-trimitere-date`, `/alege-smart`, `/analiza-factura`, `/contract`, `/ghid-complet-reduco`, `/blueprint`.

**Recomandare:** noindex imediat pe toate (risc de a induce în eroare cu prețuri false vechi de peste 4 ani + Google poate penaliza conținut low-value/duplicat la scară), apoi 301 grupat către `/compara-oferte-de-energie` sau `/compara-oferte-de-gaz` (versiunile actualizate, care par să funcționeze corect — vezi 1.5) sau șterse dacă nu au trafic (verifică în Search Console înainte).

### 1.4 Pagină moartă/duplicat de brand — **ȘTERGE + 301**
`/cine-suntem` — text brand vechi „Comparatot", modificat ultima dată 18.05.2022. [VERIFICAT, citat exact]:
> „Comparatot este site-ul care vă oferă sfaturi profesionale atunci când sunteți în căutarea unei oferte de Electricitate si Gaze mai bune."
Se suprapune complet cu `/despre-noi` (actualizată 10.11.2025). → 301 către `/despre-noi`.

### 1.5 Comparator "activ" (păstrează ca instrument secundar) — [VERIFICAT]
`/comparator`, `/compara-oferte-de-energie`, `/compara-oferte-de-gaz` par să fie versiunile curente/întreținute (modificate 05.11.2025 și listate cu titlu actualizat „Comparator preturi energie electrica — REDUCO"). Sub ele stau ~40 de pagini individuale de ofertă (`/oferte-energie/*`, `/oferte-gaz/*`) cu date recente (ex. „TINMAR BUSINESS 29 07 2026", „E.ON business 29 07 2026") — acestea par actualizate dinamic, spre deosebire de paginile din 1.3. Păstrează-le ca infrastructură a comparatorului, dar **nu le lăsa să fie prima impresie** despre Reduco (vezi tensiunea de poziționare de la Secțiunea 8).

### 1.6 Pagini WooCommerce — vezi detaliu la Secțiunea 4
`/produs/reduco-business-basic`, `/produs/reduco-business-standard`, `/produs/reduco-business-premium`, `/produs/reduco-business-basic-anual`… (14 produse în total, incl. variante "loc suplimentar de consum" și un `/produs/test-abonament` care pare a fi rămas din testare — **verifică și ascunde/șterge dacă e produs de test**), `/comanda` (noindex,follow — corect setat [VERIFICAT]), `/contul-meu` (noindex,follow — corect setat [VERIFICAT]), `/finalizare`, `/livrare`, `/retur-anulare`, `/produse`, `/categorie-produs/fara-categorie`, `/categorie-produs/abonamente-anuale`, `/categorie-produs/abonamente-lunare`.

### 1.7 Taxonomii/arhive subțiri — candidat noindex
`/category/business`, `/category/energie-electrica`, `/category/persoana-juridica`, `/category/senza-categoria` (categorie implicită **în italiană** — "senza categoria" = "fără categorie" — dovadă că site-ul a pornit dintr-o temă/instalare italiană, coerent cu istoricul "Comparatot"), `/tag/eliminareplafonare`, `/tag/anre`, `/tag/compensatii`, `/tag/firma`, `/tag/juridica`, `/tag/persoana`, `/author/marian`, `/author/adrian` — arhive automate WordPress, conținut duplicat față de articolele-sursă, fără valoare SEO proprie. Noindex recomandat.

### 1.8 Legal/utilitare — păstrează, corect
`/termeni-si-conditii`, `/politica-de-confidentialitate`, `/cookie-policy`, `/thank-you` (probabil pas tehnic post-formular, verifică dacă e noindex).

### 1.9 Subdomeniu separat
`smart.reduco.ro/prosumatori` — [VERIFICAT] platformă complet diferită tehnic (nu rulează WordPress; meta tags arată o aplicație separată găzduită pe infrastructură de tip "gpt-engineer"/Lovable, cu titlu propriu „Reduco - Analiză Facturi Energie și Comparator Furnizori | Economisește" — poziționare explicit de comparator, care contrazice mesajul „nu suntem comparator" de pe site-ul principal).
**Corecție față de auditul anterior:** nu e complet nelinkată — am găsit **un singur link** către ea, de pe `/consultanta-prosumator` ("Comparator dedicat prosumatori"). Deci e practic invizibilă pentru restul site-ului (niciun link din meniu, footer sau homepage), dar afirmația „zero linkuri" nu era 100% exactă — există exact una.

---

## 2. Analiză pagină cu pagină — cele 10 pagini B2B critice

Pentru fiecare: title/meta actuale (citate exact) → propuse (RO, ≤60/≤155 caractere, semnal B2B + poziționare „negociem, nu comparăm"), H1 propus, ce lipsește pentru conversie, unde intră CTA.

### 2.1 Homepage — `https://reduco.ro/`
- **Title actual:** „Reduco \| Oferte de energie, gaze \| Reclamatii ANRE\| Racordare" (62 car. — peste limită, conduce cu „oferte" = cadru de comparator)
- **Meta actuală:** „Reduco - Cele mai bune oferte de energie electrica si gaze! Reclamatii ANRE si reclamatii energie! Aviz tehnic de racordare energie si gaze." (143 car., ton generic/spammy cu semne de exclamare)
- **H1:** LIPSĂ [VERIFICAT] — conținutul începe direct cu un H2: „PLĂTEȘTE PREȚUL CORECT LA ENERGIE ȘI GAZE..."
- **Title propus (53 car.):** „Reduco – negociem tariful la energie pentru firma ta"
- **Meta propusă (152 car.):** „Reduco negociază tarife la energie și te reprezintă în fața furnizorilor și ANRE — pentru firme și IMM-uri. Nu suntem comparator. Cere o ofertă."
- **H1 propus:** „Negociem tariful la energie și te reprezentăm în fața furnizorilor — pentru firma ta"
- **Ce lipsește:**
  - Zero testimoniale B2B pe homepage — ambele existente (Alexandru P., Maria D.) sunt casnice.
  - Butoanele „Detalii" din secțiunea „PRODUSE POPULARE" (Panouri fotovoltaice, Pompe de căldură, Aer condiționat, Centrale termice) duc toate la `https://reduco.ro/#` — **link mort**, în loc de paginile reale existente (`/panouri-fotovoltaice`, `/pompe-de-caldura`, `/aer-conditionat-in-rate`, `/centrale-termice-rate`). [VERIFICAT direct]
  - Blocul „BLOGURI & GHIDURI UTILE REDUCO" (3 carduri) nu are linkuri funcționale vizibile în conținutul randat — verifică dacă e bug sau design intenționat fără click.
  - Secțiunea B2B („IMM-uri / Business") e mică, aproape de subsol, sub 6-7 alte blocuri.
- **CTA:** adaugă buton secundar în hero „Vezi soluții pentru firma ta" → `/solutii-imm`; mută blocul B2B mai sus (imediat sub „Servicii complete Reduco"); repară cele 4 linkuri moarte din „PRODUSE POPULARE".

### 2.2 `/solutii-imm`
- **Title actual:** „Soluții IMM pentru energie și gaze \| Reduco" (44 car., OK ca lungime)
- **Meta actuală:** „Soluții IMM pentru reducerea costurilor la energie și gaze. Reduco ajută firmele cu analiză consum, optimizare contracte, energie reactivă.." (143 car.)
- **H1:** LIPSĂ [VERIFICAT] — pornește cu H2 „Soluții IMM pentru optimizarea consumului de energie și gaze"
- **Title propus (50 car.):** „Soluții IMM: negociem tariful la energie – Reduco"
- **Meta propusă (140 car.):** „Reducem costurile cu energia pentru IMM-uri: negociem tariful, verificăm facturile și te reprezentăm la furnizor. Cere o analiză gratuită."
- **H1 propus:** „Soluții pentru IMM: reducem costurile cu energia și gazele naturale"
- **Ce lipsește:** [VERIFICAT — lista completă de linkuri de pe pagină] pagina NU leagă spre niciunul dintre `/audit-facturi`, `/litigii-anre`, `/racordare-energie-gaz`, `/consultanta-prosumator`, `/recuperare-compensatii`; leagă doar spre `/comparator` și `/panouri-fotovoltaice`. Zero testimoniale. Zero mențiune a prețurilor `/abonamente`.
- **CTA:** adaugă o secțiune „Servicii conexe" cu cele 5 linkuri de mai sus, plus link către `/abonamente#bus`. Păstrează CTA-ul principal existent („Solicită o analiză pentru afacerea ta").

### 2.3 `/audit-facturi`
- **Title actual:** „Audit facturi - REDUCO" (22 car. — prea generic, fără semnal B2B)
- **Meta actuală:** „Plătești prea mult la energie sau gaze?Lasă-ne să facem un audit de facturi – s-ar putea să ai bani de recuperat." (114 car., ton casnic)
- **H1:** LIPSĂ [VERIFICAT]
- **Title propus (44 car.):** „Audit facturi energie pentru firme – Reduco"
- **Meta propusă (146 car.):** „Verificăm facturile de energie ale firmei tale: găsim erori, suprataxări și clauze dezavantajoase. Raport clar + recuperare sume. Cere un audit."
- **H1 propus:** „Audit facturi energie și gaze pentru firme — verifică dacă plătești corect"
- **Ce lipsește:** conținutul e scris generic (persoană fizică/firmă nediferențiat); nu leagă către `/solutii-imm` sau `/litigii-anre`; zero testimoniale; FAQ menționează „gratuit pentru clienții cu alt serviciu activ" — clarifică asta explicit pentru cazul business.
- **CTA:** păstrează „SOLICITĂ UN AUDIT"; adaugă sub el „Pentru firme: inclus în abonamentul Business" → link `/abonamente#bus`.

### 2.4 `/litigii-anre`
- **Title actual:** „Litigii / ANRE - REDUCO" (23 car.)
- **Meta actuală:** „Litigii ANRE – rezolvă problemele cu furnizorul de energie sau gaze. Te ajutăm să o rezolvi legal, rapid și eficient." (118 car.)
- **H1:** LIPSĂ [VERIFICAT]
- **Title propus (44 car.):** „Litigii ANRE și reprezentare firmă – Reduco"
- **Meta propusă (137 car.):** „Te reprezentăm în fața furnizorului și ANRE, pe bază de mandat: reclamații, penalități abuzive, facturi greșite. Rezolvăm rapid, legal."
- **H1 propus:** „Litigii și reclamații ANRE — te reprezentăm în fața furnizorului"
- **Ce lipsește:** nu menționează explicit conceptul de „mandat de reprezentare" (element central al poziționării noi, folosit deja pe `/recuperare-compensatii` dar nu aici); nu leagă spre `/solutii-imm` sau `/audit-facturi`.
- **CTA:** păstrează „SOLICITĂ INFORMAȚII"; adaugă în FAQ întrebarea „Ce înseamnă mandat de reprezentare?" cu răspuns care ancorează explicit noua poziționare.

### 2.5 `/racordare-energie-gaz`
- **Title actual:** „Racordare Energie Gaz - REDUCO" (31 car.)
- **Meta actuală:** „Reduco te ajută cu întregul proces de racordare energie și gaz, de la documentație și avize până la relația cu distribuitorul și furnizorul." (143 car.)
- **H1:** LIPSĂ [VERIFICAT]. **Notă tehnică:** primul acces a eșuat cu "all scraping engines failed"; a funcționat abia la reîncercare cu `waitFor: 8000` + proxy stealth — dovadă suplimentară a randării lente semnalate anterior.
- **Title propus (52 car.):** „Racordare energie/gaz și ATR pentru firme – Reduco"
- **Meta propusă (140 car.):** „Te reprezentăm la distribuitor pentru racordare, ATR și avize — documentație completă, fără birocrație. Racordare rapidă pentru firma ta."
- **H1 propus:** „Racordare la energie electrică și gaze — ATR și avize, gestionate de noi"
- **Ce lipsește:** menționează „hală industrială" o singură dată, restul e generic casnic; nu leagă spre `/consultanta-prosumator` deși ambele ating ATR-ul; zero testimoniale.
- **CTA:** păstrează „Trimite detalii aici"; adaugă CTA secundar spre `/consultanta-prosumator` pentru racordări fotovoltaice.

### 2.6 `/recuperare-compensatii`
- **Title actual:** „Recuperare Compensatii - REDUCO" (32 car.)
- **Meta actuală:** „Reduco te ajută cu procesul de recuperare compensații pentru energie electrică și gaze naturale, verificând dacă furnizorul a aplicat corect" (142 car., trunchiată de Yoast la mijlocul propoziției)
- **H1:** LIPSĂ [VERIFICAT]
- **Title propus (50 car.):** „Recuperare compensații ANRE pentru firme – Reduco"
- **Meta propusă (131 car.):** „Recuperăm compensațiile legale de la furnizor sau distribuitor pentru firma ta: fără efort, fără risc, plătești doar dacă reușim."
- **H1 propus:** „Recuperare compensații energie și gaze — plătești doar dacă reușim"
- **Ce lipsește:** **aproape nimic** — aceasta e cea mai completă pagină de pe tot site-ul: are deja 3 testimoniale (2 casnice: Mihai P. București, Radu L. Cluj-Napoca; 1 B2B explicit: „Andrei M., Administrator operațional, București" — **confirmat: acesta e singurul testimonial B2B de pe tot site-ul**), menționează explicit „mandat de reprezentare conform Codului Civil", are secțiune FAQ solidă. **Folosește-o ca șablon pentru celelalte pagini de servicii.**
- **CTA:** deja bun („Verifică gratuit eligibilitatea") — model de referință pentru restul site-ului.

### 2.7 `/consultanta-prosumator`
- **Title actual:** „Consultanta Prosumator - REDUCO" (32 car.)
- **Meta actuală:** „Consultanță prosumator – suport complet pentru dosar, contract și compensarea energiei. Gestionăm relația cu furnizorul și distribuitorul..." (143 car.)
- **H1:** LIPSĂ [VERIFICAT]
- **Title propus (46 car.):** „Consultanță prosumator pentru firme – Reduco"
- **Meta propusă (142 car.):** „Ajutăm firma ta să devină prosumator: dosar, ATR, avize și compensare corectă a energiei. Gestionăm relația cu furnizorul și distribuitorul."
- **H1 propus:** „Consultanță prosumator — dosar, ATR și compensarea corectă a energiei"
- **Ce lipsește:** **critic — widget public rupt** [VERIFICAT]: secțiunea „Simulator cost implementare sistem fotovoltaic" afișează textul de eroare „Project not found" / „No Lovable project found at this address" direct în pagina live. Conținutul e orientat majoritar casnic (menționează „stau la bloc", „Casa Verde", subvenții pentru persoane fizice) și nu diferențiază clar oferta pentru firme.
- **CTA:** repară/elimină widget-ul rupt de urgență; adaugă secțiune dedicată firmelor cu linkuri spre articolele noi de blog `/panouri-fotovoltaice-firme` și `/legea-160-2026-prosumatori-firme`.

### 2.8 `/abonamente`
- **Title actual:** „Abonamente - REDUCO" (20 car.)
- **Meta actuală [VERIFICAT, citat exact — confirmă integral finding-ul din auditul anterior]:** „Abonamente petnru Casnici Basic Abonamente **Recudo** Casnici Lei **10 Lună** fără TVA 1 analiză/an a facturii de energie/gaze..." — typo „petnru" (pentru), typo „**Recudo**" (Reduco), preț vechi „10 Lună" (pe pagina live curentă, planul Casnic Basic costă de fapt 15 lei).
- **H1:** LIPSĂ [VERIFICAT] — pornește cu H2 „Abonamente pentru Casnici"
- **Title propus (49 car.):** „Abonamente Business – de la 99 lei/lună – Reduco"
- **Meta propusă (127 car.):** „Abonamente Reduco Business: audit facturi, negociere tarife și reprezentare juridică pentru firma ta. De la 99 lei/lună + TVA."
- **H1 propus:** „Abonamente Reduco — Casnic și Business"
- **Ce lipsește:**
  - Meta description trebuie scrisă manual în Yoast (nu lăsată să se auto-genereze din conținut).
  - **Treapta nouă Business Plus (899 lei) nu apare deloc pe pagina live** — am căutat "899" pe tot domeniul reduco.ro, zero rezultate. Strategia de preț a clientului nu e încă publicată.
  - Cele 3 planuri Casnic au bullet-uri **identice** între ele (Basic/Standard/Premium au aceleași 14 beneficii cuvânt cu cuvânt, doar prețul diferă cu 1-2 rânduri) — la fel pentru cele 3 planuri Business. Fără un tabel comparativ clar, un cumpărător B2B nu poate justifica de ce să plătească 399 lei în loc de 99 lei.
- **CTA:** butoanele „Alege" funcționează tehnic (add-to-cart); adaugă și opțiunea „Vorbește cu un consultant înainte să alegi" pentru planul Plus, tipic pentru vânzări B2B cu bilet mare.

### 2.9 `/despre-noi`
- **Title actual:** „Despre noi - REDUCO" (20 car.)
- **Meta actuală:** „Suntem un grup de profesioniști cu peste 15 ani de experiență în domeniul energiei..." (trunchiată de Yoast, ~150 car., fără cuvinte-cheie B2B/negociere)
- **H1:** prezent doar ca H2: „Ghidul tău de încredere pentru alegerea celor mai bune oferte de energie și gaz". **Constatare importantă:** deși pagina a fost actualizată pe 10.11.2025 (confirmat din `modifiedTime`), textul de poziționare tot vorbește de „alegerea celor mai bune oferte" — limbaj de comparator, NU „negociem și te reprezentăm". Actualizarea din noiembrie a schimbat parțial conținutul (a scos "Comparatot"), dar **nu a schimbat poziționarea fundamentală** din hero.
- **Title propus (49 car.):** „Despre Reduco – consultanți energie pentru firme"
- **Meta propusă (135 car.):** „15+ ani experiență în energie. Negociem tarife, verificăm facturile și te reprezentăm în fața furnizorilor — nu suntem un comparator."
- **H1 propus:** „Despre Reduco — negociem și te reprezentăm, nu doar comparăm oferte"
- **Ce lipsește:** nicio secțiune dedicată echipei/certificărilor/clienților business; testimonialul B2B existent (de pe `/recuperare-compensatii`) nu e reciclat aici.
- **CTA:** schimbă „SOLICITĂ INFORMAȚII" generic în „Discută cu un consultant energie" pentru ton profesional B2B.

### 2.10 `/servicii`
- **Title actual:** „Servicii - REDUCO" (17 car.)
- **Meta actuală:** „SOLUȚII COMPLETE, ADAPTATE NEVOILOR TALE La Reduco.ro, îți oferim o gamă variată de servicii..." (trunchiată, ~155 car.)
- **H1:** LIPSĂ [VERIFICAT]. **Notă tehnică:** a eșuat la prima accesare, a funcționat la reîncercare cu proxy stealth — a doua pagină, după `/racordare-energie-gaz`, care confirmă problema de randare lentă la nivel de site, nu doar homepage.
- **Title propus (48 car.):** „Servicii pentru firme: energie, ANRE, racordare"
- **Meta propusă (139 car.):** „Servicii Reduco pentru firme: schimbare furnizor, audit facturi, litigii ANRE, racordare și consultanță prosumator. Vezi toate serviciile."
- **H1 propus:** „Serviciile Reduco — consultanță și reprezentare în energie"
- **Ce lipsește:** pagina listează corect toate cele 7 servicii, inclusiv `/solutii-imm` [VERIFICAT] — structura de bază e bună; dar nu diferențiază oferta pentru firme de cea casnică, și nu leagă spre `/abonamente`.
- **CTA:** adaugă la finalul grilei de servicii un CTA „Vezi planurile Business" → `/abonamente#bus`.

---

## 3. Structura propusă a site-ului după consolidare

### 3.1 Arbore final (max. 25 pagini + blog)

```
/                                    (homepage repoziționat)
/despre-noi
/servicii                            (hub)
  /audit-facturi
  /litigii-anre
  /racordare-energie-gaz
  /consultanta-prosumator
  /recuperare-compensatii
  /solutii-imm
  /eficienta-energetica
/schimbarea-furnizorului
/panouri-fotovoltaice                (pillar; leagă spre /panouri-fotovoltaice-firme din blog)
/pompe-de-caldura
/centrale-termice-rate               (consolidează cu /centrale-termice dacă există duplicat — verifică)
/aer-conditionat-in-rate
/negociere-colectiva                 (dacă activă)
/abonamente
  /produs/*                          (14 pagini WooCommerce — rămân, sunt tehnice/tranzacționale)
/comparator                          (instrument secundar, nu identitate de brand)
  /compara-oferte-de-energie
  /compara-oferte-de-gaz
/contacte
/intrebari-frecvente
/blog  (+ articole)
/termeni-si-conditii
/politica-de-confidentialitate
/cookie-policy
/livrare
/retur-anulare
```
= 21 pagini „conținut" de bază + zona WooCommerce/legal + blog. Sub pragul de 25 cerut.

### 3.2 Hartă de redirecturi 301 (vechi → nou)

| De la | Către |
|---|---|
| `/cine-suntem` | `/despre-noi` |
| `/oferta-energie-electrica-juridic`, `/juridic-energie-fix`, `/juridic-energie-variabil`, `/juridic-energie-si-gaze-fix`, `/juridic-energie-si-gaz-variabil`, `/oferta-energie-si-gaze-juridic` | `/compara-oferte-de-energie` |
| `/oferta-gaze-juridic`, `/juridic-gaz-fix`, `/juridic-gaz-variabil` | `/compara-oferte-de-gaz` |
| `/casnic-pret-fix-gaz`, `/casnic-pret-variabil-gaze`, `/casnic-energie-si-gaz-fix` | `/compara-oferte-de-gaz` |
| `/casnic-pret-variabil-energie`, `/casnic-energie-si-gaze-variabil`, `/oferte-energie-casnic-pret-fix` | `/compara-oferte-de-energie` |
| `/energie-si-gaze`, `/energie-si-gaze-oferta`, `/energie-electrica`, `/gaze`, `/oferte-energetice`, `/comparator-energie` | `/comparator` |
| `/compara-oferte-energie`, `/compara-oferte-energie-step-1`, `/compara-oferte-energie-step-2` | `/compara-oferte-de-energie` |
| `/comparatot-activare-oferte-trimitere-date`, `/alege-smart`, `/ghid-complet-reduco`, `/blueprint` | `/` (verifică întâi trafic în GSC; dacă zero, poți doar 410/șterge) |
| `/analiza-factura`, `/contract` | `/audit-facturi` |
| `/monitorizarea-inteligenta` | `/eficienta-energetica` |
| `/enel-centrala-termica` | `/centrale-termice-rate` |
| `/aparat-de-aer-conditionat`, articolele vechi din 2022 despre AC/răcorire vara | `/aer-conditionat-comercial-firme` sau `/aer-conditionat-in-rate` |
| `/despre-centrale-termice`, `/cum-alegi-cele-mai-eficiente-centrale-termice`, `/de-ce-sa-alegi-centrale*` (2022) | `/centrala-termica-spatiu-comercial` |
| restul articolelor generice 2022 fără echivalent modern (economisire generică, contoare) | `/blog` (sau 410 dacă zero trafic în GSC) |

**Important:** verifică fiecare URL din stânga în Google Search Console (Performance → Pages) înainte de a redirecționa/șterge — nu am acces la date de trafic, deci nu pot confirma care dintre aceste pagini încă aduc vizite organice.

---

## 4. Zona WooCommerce — are sens un coș de cumpărături pentru consultanță B2B?

**Răspuns scurt: parțial da (ca motor de facturare recurentă), dar limbajul și structura din jurul lui trebuie de-ecommerce-izate.**

- Abonamentele (99/199/399/899 lei+TVA, recurente lunar) sunt, de fapt, un produs de tip subscription billing — WooCommerce poate rula asta tehnic corect ca infrastructură de plată. Nu recomand scoaterea lui complet.
- **Ce subminează credibilitatea unui serviciu profesional pe bază de mandat:**
  - `/livrare` — [VERIFICAT] textul e deja adaptat rezonabil ("Serviciile ... sunt livrate exclusiv în format digital"), dar **slug-ul URL "livrare" ("shipping") apare în Google ca titlu de pagină și în breadcrumb**, semnalând unei firme prospect că vorbește cu un magazin online, nu cu un consultant. Recomand păstrarea conținutului dar redenumirea internă în comunicare/nav ca "Condiții de acces la servicii", fără să afectezi URL-ul existent (evită alt 301 inutil).
  - `/retur-anulare` — [VERIFICAT] la fel, conținut deja adaptat corect legal (obligatoriu conform legislației comerțului electronic — nu poate fi eliminat), dar ar trebui linkat doar din footer/checkout, nu evidențiat în navigare.
  - `/produse` — [VERIFICAT] amestecă sub eticheta generică "Produse" atât echipamente fizice (panouri, pompe de căldură, AC, centrale) cât și, implicit, abonamentele de consultanță. Recomand separarea clară în navigare: "Servicii" / "Abonamente" / "Echipamente recomandate" — nu tot sub "Produse".
  - `/produs/test-abonament` — [VERIFICAT, apare în sitemap] pare un produs de test rămas din configurare; verifică și ascunde/șterge dacă nu e folosit activ.
- **Ce e deja făcut corect:** `/comanda` și `/contul-meu` au ambele `robots: noindex, follow` [VERIFICAT direct în meta tag-uri] — exact configurarea corectă pentru pagini tranzacționale WooCommerce. Nu schimba asta.
- **Recomandare de fond:** dacă iconița de coș de cumpărături e vizibilă în header-ul principal (nu am putut confirma vizual din acest audit, vezi Secțiunea 7), recomand eliminarea ei din navigarea primară pentru un site B2B de consultanță — înlocuiește cu butoane directe "Alege abonament" / "Autentificare", fără metafora vizuală de magazin.

---

## 5. Blogul (`/blog` + arhive)

**Corecție față de auditul anterior:** blogul are **5 pagini de arhivă, nu 3** [VERIFICAT prin paginare directă: "Blog - Pagina 2 din 5", "Pagina 3 din 5", "Pagina 4 din 5", "Pagina 5 din 5"], cu aproximativ **41 de articole** în total (10/pagină pe primele 4 pagini + 1 pe ultima).

### 5.1 Potențial B2B ridicat (păstrează, prioritizează interlinking) — vezi lista completă la 1.2
Cele ~15 articole din iulie–august 2026 sunt scrise specific pentru firme, cu unghiuri concrete (praguri legale, ISCIR, energie reactivă, POSF). Sunt cel mai puternic activ de conținut nefolosit al site-ului.

### 5.2 Articole "punte"/media (păstrează pentru autoritate topicală, prioritate joasă pentru conversie B2B)
`/ce-se-schimba-la-facturile-de-gaze-din-aprilie-2026...`, `/de-ce-raman-facturile-la-energie-atat-de-mari...`, `/noua-ordonanta-privind-comunitatile-de-energie...`, `/hidroelectrica-intra-in-razboiul-preturilor...`, `/schimbari-la-plata-facturilor-la-energie...`, `/romanii-pentru-care-facturile-la-energie-ar-creste...`, `/cine-a-castigat-cu-adevarat-din-plafonarea-preturilor...`, `/legea-160-2026-prosumatori-firme` (aceasta e de fapt B2B, o pun aici doar informativ că se leagă și de context media).

### 5.3 Articole moarte (2022, pagini 4-5 din arhivă) — 301 sau rescrie
[VERIFICAT direct pe `/blog/page/4` și `/blog/page/5`]:
`/ce-trebuie-sa-stii-despre-aerul-conditionat`, `/despre-centrale-termice`, `/alege-ofertele-potrivite`, `/sfaturi-pentru-economisire-la-gaz`, `/cum-sa-economisesti-energia-electrica` (titlu cu caractere corupte „￼￼" vizibile — bug de encoding, în plus față de faptul că e conținut vechi), `/cum-sa-economisesti-la-facturi`, `/economisirea-energiei-electrice-contoare`, `/cum-sa-economisesti-pentru-facturi-mai-mici`, `/aparat-de-aer-conditionat`, `/cum-sa-te-racoresti-vara`, `/sfaturi-pentru-a-avea-o-casa-racoroasa-pe-timpul-verii`. Toate sunt casnice, generice, fără valoare pentru poziționarea B2B nouă — 301 către echivalentul modern unde există (vezi harta din 3.2) sau rescrie cu unghi de firmă dacă păstrează trafic organic relevant (verifică în GSC).

### 5.4 Legătură lipsă homepage → blog
Secțiunea „BLOGURI & GHIDURI UTILE REDUCO" de pe homepage afișează 3 carduri fără linkuri funcționale vizibile în conținutul randat — de verificat manual dacă e un bug de widget sau o decizie de design.

---

## 6. Schema.org / date structurate

**[NEVERIFICABIL DIRECT ÎN ACEASTĂ SESIUNE]** — capul HTML al homepage-ului (`<head>`) conține ~197.000 de caractere, aproape în totalitate CSS inline generat de Elementor, ceea ce a depășit limitele instrumentelor de citire disponibile în acest audit. Nu am putut extrage și confirma cu certitudine blocurile `<script type="application/ld+json">`.

**Indiciu indirect găsit:** metadata extrasă automat de pe homepage conține câmpurile `"bestRating": ["5","5"]` și `"worstRating": ["0","0"]` — aceste câmpuri nu provin din meta tag-uri OG/Twitter standard, ci de regulă sunt derivate din markup de tip `Review`/`AggregateRating` (schema.org sau microdata). Asta sugerează că **există undeva pe homepage un fragment de schema Review/Rating** (probabil de la un plugin de testimoniale), dar nu am găsit niciun indiciu de schema `Organization`, `LocalBusiness`, `Service` sau `FAQPage`.

**Ce știm sigur:** site-ul rulează Yoast SEO [VERIFICAT — sitemap-urile poartă semnătura „XML Sitemap generated by Yoast SEO"]. Yoast adaugă implicit un grafic de bază (`WebSite`, `WebPage`, autor) dar **nu adaugă automat** `LocalBusiness`, `Service` sau `FAQPage` — acestea trebuie configurate manual.

**Recomandare de verificare imediată pentru client/dezvoltator:** rulează homepage-ul prin [Google Rich Results Test](https://search.google.com/test/rich-results) pentru un răspuns definitiv despre ce schema există azi — eu nu am putut confirma programatic în acest mediu.

### 6.1 JSON-LD propus pentru homepage (de adăugat, indiferent de ce există deja)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "ProfessionalService",
      "@id": "https://reduco.ro/#organization",
      "name": "Reduco",
      "legalName": "ALMA SKY SRL",
      "url": "https://reduco.ro/",
      "logo": "https://reduco.ro/wp-content/uploads/2022/02/REDUCO-1.png",
      "image": "https://reduco.ro/wp-content/uploads/2025/07/reduco-1.jpg",
      "description": "Consultanță energetică pentru firme: negociere tarife, audit facturi, reprezentare în fața furnizorilor și ANRE pe bază de mandat.",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Margineni, FN",
        "addressLocality": "Bacău",
        "addressCountry": "RO"
      },
      "email": "info@reduco.ro",
      "telephone": "+40318211205",
      "taxID": "RO28501770",
      "areaServed": "RO",
      "priceRange": "99-899 RON",
      "sameAs": [
        "https://www.facebook.com/Reduco.ro",
        "https://www.instagram.com/reduco.ro",
        "https://www.tiktok.com/@reduco_ro",
        "https://www.youtube.com/@reduco-ro"
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://reduco.ro/#website",
      "url": "https://reduco.ro/",
      "name": "Reduco",
      "publisher": { "@id": "https://reduco.ro/#organization" },
      "inLanguage": "ro-RO"
    },
    {
      "@type": "Service",
      "@id": "https://reduco.ro/#service-business",
      "serviceType": "Consultanță și reprezentare energie pentru firme",
      "provider": { "@id": "https://reduco.ro/#organization" },
      "areaServed": "RO",
      "audience": { "@type": "BusinessAudience", "audienceType": "IMM și firme" },
      "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "Abonamente Reduco Business",
        "itemListElement": [
          { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Reduco Business Basic" }, "price": "99", "priceCurrency": "RON" },
          { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Reduco Business Standard" }, "price": "199", "priceCurrency": "RON" },
          { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Reduco Business Premium" }, "price": "399", "priceCurrency": "RON" },
          { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Reduco Business Plus" }, "price": "899", "priceCurrency": "RON" }
        ]
      }
    },
    {
      "@type": "FAQPage",
      "@id": "https://reduco.ro/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Reduco este comparator de energie?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nu. Reduco este un consultant care negociază tarife și te reprezintă în fața furnizorilor și distribuitorilor de energie, pe bază de mandat, nu un simplu comparator de oferte."
          }
        },
        {
          "@type": "Question",
          "name": "Ce înseamnă reprezentare pe bază de mandat?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Reduco acționează în numele firmei tale, conform Codului Civil, în relația cu furnizorii, distribuitorii și ANRE — de la negocierea tarifelor până la litigii și recuperarea compensațiilor."
          }
        }
      ]
    }
  ]
}
```

**Aplică același model `FAQPage`** (cu întrebările deja scrise pe pagină) pe: `/audit-facturi`, `/litigii-anre`, `/racordare-energie-gaz`, `/consultanta-prosumator`, `/recuperare-compensatii`, `/solutii-imm` — conținutul FAQ există deja pe fiecare, lipsește doar marcajul.

---

## 7. Mobil

**[NEVERIFICABIL VIZUAL ÎN ACEASTĂ SESIUNE]** — am capturat screenshot-uri cu `mobile: true` pentru homepage și `/abonamente`, dar instrumentul de citire disponibil în acest mediu acceptă doar fișiere de pe disc local, nu URL-uri semnate temporare generate de Firecrawl. Nu pot deci confirma vizual probleme specifice de layout mobil în acest raport — **recomand ferm o verificare manuală directă pe telefon** de către client/dezvoltator, plus rulare prin Google PageSpeed Insights (mobil) pentru homepage și `/abonamente`.

**Ce am putut confirma indirect din meta tag-uri (același pe toate paginile testate):**
- `viewport: width=device-width, initial-scale=1` prezent pe toate paginile [VERIFICAT] — bază responsive corectă instalată.
- Linkurile "Alege" din `/abonamente` conțin caractere spațiu encodate (`%20`) în query string (ex. `/comanda/?add-to-cart=75886%20`) [VERIFICAT] — artefact probabil dintr-un shortcode configurat greșit; funcționează probabil oricum, dar merită curățat.
- Toate elementele deja cunoscute din auditul anterior — chat LiveAgent, buton WhatsApp, banner cookie cu categorii GDPR — sunt confirmate prezente pe fiecare pagină testată în acest audit [VERIFICAT în markdown-ul fiecărei pagini scrapuite]. Pe un viewport mobil mic, aceste elemente ocupă disproporționat mai mult spațiu relativ decât pe desktop — recomand testare vizuală directă.
- **Corecție/nuanțare a finding-ului „4 popup-uri identice":** am observat că majoritatea CTA-urilor de pe site (pe toate paginile verificate) trimit către **același ID de popup Elementor (76489)**, ceea ce sugerează un singur popup global reutilizat — practică normală și, de fapt, bună. Nu pot confirma din conținutul text câte instanțe de popup se încarcă efectiv simultan în pagină; recomand verificare tehnică directă (view-source, caută `elementor-popup-modal`) pentru a clarifica dacă sunt 4 popup-uri separate care se încarcă redundant sau un singur template.

**Nu am date de performanță mobilă reale (LCP, CLS, INP) — nu le pot inventa.** Rulați PageSpeed Insights / CrUX pentru cifre concrete.

---

## Sinteză: ce confirm, ce infirm/nuanțez, ce e nou față de auditul anterior

| Constatare din auditul anterior | Rezultatul acestui re-audit |
|---|---|
| Randare foarte lentă (~15s) | **Confirmat și întărit** — homepage are ~197KB CSS inline doar în `<head>`; 4 pagini diferite (`/servicii`, `/racordare-energie-gaz`, `/comanda`, `/contul-meu`) au eșuat la accesare simplă și au necesitat `waitFor` extins + proxy alternativ |
| `/cine-suntem` = brand vechi „Comparatot" | **Confirmat**, citat exact |
| ~14 pagini juridic/casnic cu prețuri 2022 | **Confirmat și extins** — am găsit peste 20 de pagini în aceeași categorie |
| `/solutii-imm` nu leagă spre servicii | **Confirmat**, listă exactă de linkuri verificată |
| H1 lipsă pe majoritatea paginilor | **Confirmat pe 10/11 pagini testate** — cu nuanța că `/cine-suntem` (template vechi) chiar are H1 |
| Meta `/abonamente` are „Recudo" + preț vechi | **Confirmat, citat exact** |
| `smart.reduco.ro` nelinkată | **Nuanțat** — există exact 1 link, de pe `/consultanta-prosumator`, deci nu e literal zero, dar e practic invizibilă |
| Un singur testimonial B2B | **Confirmat exact** — pe `/recuperare-compensatii`, „Andrei M." |
| — (nou, negăsit anterior) | Widget public rupt pe `/consultanta-prosumator` ("Project not found") |
| — (nou) | Business Plus (899 lei) nu există deloc pe site |
| — (nou) | Blog are 5 pagini de arhivă, nu 3, cu ~41 articole |
| — (nou) | Tensiune structurală: site tehnic construit ca site de comparator (40+ pagini oferte, subdomeniu comparator) vs. poziționare de brand „nu suntem comparator" |
| — (nou) | 4 linkuri moarte pe homepage (`#`) în secțiunea „Produse populare" |

---

## Fișiere/pagini de referință pentru verificare directă de către client

Toate URL-urile citate mai sus sunt de pe `https://reduco.ro/` (WordPress + WooCommerce + Elementor + Yoast SEO + Site Kit by Google) și `https://smart.reduco.ro/` (aplicație separată). Pentru verificarea afirmațiilor din acest raport, folosiți: view-source direct pe fiecare URL citat, Google Search Console (trafic real, nu presupus), Google Rich Results Test (schema.org), PageSpeed Insights (performanță mobil/desktop reală).
