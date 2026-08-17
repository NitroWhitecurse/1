# Reduco.ro — Strategie SEO pentru repoziționare: din „comparator de oferte" în „manager energetic"

Versiune: august 2026
Autor: consultanță SEO externă
Sursă context: `/home/user/1/reduco/00-brief-context.md` + verificare SERP live (august 2026)

---

## 0. Metodologie și onestitatea datelor — citește înainte de orice

**Ce am verificat efectiv (date reale):** am rulat 9 căutări live pe Google pentru piața românească și am analizat compoziția rezultatelor (cine rankează, ce tip de site, ce intenție servește pagina). Aceste observații sunt marcate cu **[SERP verificat]**.

**Ce NU am:** acces la Ahrefs / Semrush / Google Keyword Planner / Search Console-ul Reduco. **Nu voi da volume de căutare în cifre**, pentru că orice cifră ar fi inventată. Domeniul reduco.ro este blocat de proxy în această sesiune, deci nu am putut face crawl propriu — toate afirmațiile despre paginile actuale vin din auditul intern din brief și trebuie reverificate pe site înainte de implementare.

**Scala de dificultate folosită** (1–5, calitativă, bazată pe compoziția SERP observată):

| Nivel | Ce înseamnă concret |
| --- | --- |
| **1 — Foarte scăzută** | SERP-ul e populat de bloguri personale, forumuri, site-uri fără autoritate în energie. O pagină bine făcută intră în top 10 în 1–3 luni. |
| **2 — Scăzută** | Site-uri de nișă mici, agregatoare slabe, conținut vechi. 3–6 luni cu conținut bun + câteva linkuri. |
| **3 — Medie** | Amestec: 1–2 jucători serioși + conținut mediocru. 6–9 luni, necesită pilon + cluster + autoritate. |
| **4 — Ridicată** | Furnizori mari (ENGIE, PPC, Electrica), certificatori (TÜV SÜD), consultanți industriali consacrați. 9–18 luni. |
| **5 — Foarte ridicată** | Domeniu dominat de instituții (ANRE, legislatie.just.ro, energie.gov.ro) sau de furnizori cu buget nelimitat. Nu se atacă frontal — se atacă pe long-tail. |

**Regula de aur pentru Reduco:** nu ataca niciodată termenul-cap unde SERP-ul e plin de furnizori sau de certificatori. Atacă **intenția de problemă** („de ce am factura mare", „ce fac dacă furnizorul mi-a facturat retroactiv"), unde Reduco are competență reală și concurența are conflict de interese.

---

## 1. Harta de cuvinte-cheie

### 1.0 Descoperirea strategică din analiza SERP — citește asta prima

Din cele 9 SERP-uri verificate rezultă trei concluzii care schimbă strategia:

1. **„Audit energetic" ≠ „audit de factură".** [SERP verificat] Căutarea `audit factura energie electrica firma` returnează aproape exclusiv **audit energetic tehnic** (ENGIE, TÜV SÜD, Enel X, Servelect, cgservices.ro, energymanagementaudit.ro). Nimeni nu ocupă spațiul „verific factura ta și îți spun cât plătești real per kWh". **Reduco nu trebuie să concureze pe „audit energetic" — trebuie să creeze și să dețină categoria „audit de factură".** Este cea mai mare oportunitate de poziționare din tot documentul.

2. **Zona ANRE / litigii este practic nepăzită.** [SERP verificat] Pe `reclamatie ANRE furnizor energie compensatii` rankează infocontact.ro, elcata.ro, playtech.ro, un blog pe Blogspot (elycriss.ro) și arhiva ANRE. **Zero jucători B2B serioși.** Reduco are dosare reale (NOVEX SPACE, 82.463,75 lei în dispută) — poate domina această zonă în 3–6 luni. Este cel mai bun raport impact/efort din întreaga strategie.

3. **Zona „putere contractată / depășire de putere" este goală.** [SERP verificat] Rankează un blog WordPress personal, un blog de electrician și un blog maghiar (`silverpc.hu`). Pentru o problemă care costă firmele bani reali lunar. Dificultate 1–2.

Contra-exemplu, ca să fie clar unde NU se merge: pe `prosumator 2026` [SERP verificat] rankează mașinării de conținut foarte active (instalatori-fotovoltaice.ro, siana-energie.ro, greenlead.ro, economisi.ro) care publică săptămânal. Nu se atacă frontal.

**Competitor de conținut de urmărit:** `economisi.ro` a apărut în 3 din 9 SERP-uri verificate (prosumator, ATR, energie reactivă). Este cel mai consistent producător de conținut din nișa energetică RO. De monitorizat lunar.

---

### 1.1 Segment: IMM (client primar) — restaurante, hoteluri, magazine, farmacii, clinici, ateliere

#### Grup 1.1.A — Audit de factură (TRANZACȚIONAL / COMERCIAL) ⭐ prioritate maximă

| | |
| --- | --- |
| **Cuvânt-cheie principal** | `audit factura energie firma` |
| **Variante secundare** | `verificare factura energie electrica firma`, `analiza factura energie companie`, `factura energie prea mare firma ce fac`, `pret real kwh factura firma`, `cine verifica factura de energie`, `erori factura energie electrica firma`, `audit factura gaze naturale firma` |
| **Pagina țintă** | `/audit-facturi/` (rescrisă B2B) |
| **Dificultate estimată** | **2 — Scăzută**, pentru varianta „factură". **4 — Ridicată** dacă se folosește formularea „audit energetic". |
| **Argument** | [SERP verificat] SERP-ul pe „audit factura energie firma" este ocupat de pagini care vorbesc despre *audit energetic tehnic*, nu despre verificarea facturii. Intenția reală a utilizatorului (administrator care se uită la o factură mare) nu este servită de nimeni. Este un gol de intenție, nu un gol de volum. |
| **Nivel de certitudine** | Compoziția SERP = date reale. Volumul = **estimare calitativă**: probabil volum mic-mediu, dar intenție extrem de comercială — un administrator care caută asta are o factură pe masă. Prefer 50 de căutări cu intenție de cumpărare decât 5.000 informaționale. |

**Atenție la implementare:** brieful spune că `/audit-facturi` este scrisă în registru casnic, deși primește trafic din articole B2B (`/audit-facturi-energie-imm`, `/schimbare-furnizor-energie-firma`). Aceasta este o **pierdere de conversie măsurabilă azi**, nu o ipoteză. Rescrierea acestei pagini este task-ul #1 din tot planul.

#### Grup 1.1.B — Schimbare furnizor / achiziție energie (COMERCIAL)

| | |
| --- | --- |
| **Cuvânt-cheie principal** | `schimbare furnizor energie electrica firma` |
| **Variante secundare** | `schimbare furnizor energie persoana juridica`, `cum aleg furnizorul de energie pentru firma`, `oferte energie electrica firme 2026`, `negociere contract energie firma`, `licitatie furnizare energie electrica`, `contract energie electrica firma clauze`, `reziliere contract furnizare energie firma` |
| **Pagina țintă** | `/pentru-firme/` (pilon) + `/licitatie-furnizare-energie/` (nou) |
| **Dificultate estimată** | **3 — Medie** |
| **Argument** | [SERP verificat] Rankează furnizorii înșiși (PPC, MET, Engie), comparatoare (pandabot.ro), presă (capital.ro) și AFEER. Furnizorii au autoritate mare, **dar au un handicap structural: nu pot scrie onest „pleacă de la noi".** Reduco poate. Unghiul de conținut care câștigă: „ce NU îți spune furnizorul când semnezi". |
| **Nivel de certitudine** | SERP = date reale. Dificultatea 3 = **estimare argumentată** — furnizorii au DR mare, dar paginile lor sunt subțiri și autopromoționale. |

#### Grup 1.1.C — Costuri ascunse din factură (INFORMAȚIONAL, cu conversie mare) ⭐

| | |
| --- | --- |
| **Cuvânt-cheie principal** | `energie reactiva penalitati firma` |
| **Variante secundare** | `ce este energia reactiva pe factura`, `cum scap de penalitatile de energie reactiva`, `factor de putere sub 0.92 penalizare`, `compensare energie reactiva cost`, `depasire putere contractata penalitati`, `putere contractata supradimensionata firma`, `tarif distributie nivel de tensiune gresit` |
| **Pagina țintă** | `/energie-reactiva/` (nouă) + `/optimizare-putere-contractata/` (nouă, faza 3) + articole de blog |
| **Dificultate estimată** | **2 — Scăzută** pentru partea informațională / „penalități". **3 — Medie** pentru `compensare energie reactiva` (comercial). |
| **Argument** | [SERP verificat, două căutări] Pe energie reactivă rankează Servelect, Senys, Electrica Furnizare, dar și instalatori mici (panouricluj.ro, crismartelectric.ro) — SERP mixt, penetrabil. Pe `putere contractata / depasire putere` SERP-ul este **foarte slab**: bloguri WordPress personale, un blog de electrician, un blog maghiar. Este cel mai ușor teren din listă. |
| **Nivel de certitudine** | SERP = date reale, foarte clare. **Diferențiator de exploatat:** instalatorii care rankează vând baterii de condensatoare — au interes să vândă echipament. Reduco poate spune „poate nu ai nevoie de echipament, ai nevoie de alt tarif". Acesta e exact argumentul de independență. |

#### Grup 1.1.D — Abonament / manager energetic externalizat (TRANZACȚIONAL)

| | |
| --- | --- |
| **Cuvânt-cheie principal** | `manager energetic externalizat firma` |
| **Variante secundare** | `abonament management energetic`, `consultanta energetica pentru firme`, `servicii management energetic IMM`, `monitorizare consum energie firma`, `externalizare management energie`, `cat costa un manager energetic` |
| **Pagina țintă** | `/abonamente/` (rescrisă, B2B first) + `/monitorizare-consum-energie/` |
| **Dificultate estimată** | **4 — Ridicată** pentru `management energetic` simplu; **2–3** pentru variantele cu „externalizat", „IMM", „abonament". |
| **Argument** | [SERP verificat] `management energetic servicii firme` returnează TÜV SÜD, Enegav (consultanta-energie.ro), Servelect, Enesco Industrial, Energobit — jucători industriali consacrați, orientați spre uzine, nu spre restaurante și farmacii. **Nimeni nu vorbește IMM-ului cu 2 puncte de consum.** Long-tail-ul cu „IMM", „abonament", „lunar" e liber. |
| **Nivel de certitudine** | SERP = date reale. **Notă critică:** termenul „manager energetic" are în RO un sens juridic strict (persoană atestată de Ministerul Energiei, obligatorie peste 1.000 tep/an). Reduco NU trebuie să sugereze că este manager energetic atestat dacă nu are atestarea — riscul e legal, nu doar SEO. Formulare sigură: **„managementul energetic al firmei tale"** sau „partenerul tău energetic", și, pentru Legea 121, „coordonăm relația cu managerul energetic atestat" (exact ce spune brieful că face Reduco în realitate). |

---

### 1.2 Segment: Multi-locație (rețele — lanțuri de magazine, farmacii, restaurante, benzinării)

#### Grup 1.2.A — Management energetic pentru rețele (COMERCIAL)

| | |
| --- | --- |
| **Cuvânt-cheie principal** | `management energie mai multe puncte de consum` |
| **Variante secundare** | `facturi energie lant de magazine`, `optimizare costuri energie retea franciza`, `contract energie multi-locatie firma`, `centralizare facturi energie companie`, `raport consum energie pe locatii`, `energie pentru lanturi de restaurante` |
| **Pagina țintă** | `/pentru-firme/multi-locatie/` (nouă) |
| **Dificultate estimată** | **1–2 — Foarte scăzută spre scăzută** |
| **Argument** | **Estimare calitativă, nu am rulat SERP dedicat.** Raționament: aceste formulări sunt descrieri de problemă, nu termeni de industrie. Foarte puțini caută exact așa, dar cei care caută sunt exact clientul-țintă cu cea mai mare valoare pe viață (5+ puncte de consum × 89 lei/lună = minimum 595 lei/lună). |
| **Cum se validează** | Aceasta este zona unde **conținutul de tip „studiu de caz" bate cuvintele-cheie**. Un director financiar de rețea nu caută pe Google „management energie multi-locație" — caută „de ce farmaciile mele plătesc prețuri diferite pe kWh". Prioritizează articolele-problemă și LinkedIn peste SEO pur aici. |

---

### 1.3 Segment: Industrial (peste 500 MWh/an, obligații Legea 121/2014)

#### Grup 1.3.A — Conformare Legea 121/2014 (COMERCIAL, valoare mare) ⭐

| | |
| --- | --- |
| **Cuvânt-cheie principal** | `conformare Legea 121/2014 firma` |
| **Variante secundare** | `declaratie consum energie 2026 termen`, `Legea 121 2014 obligatii companii`, `audit energetic obligatoriu 4 ani`, `program de imbunatatire a eficientei energetice`, `peste 1000 tep obligatii`, `manager energetic atestat obligatoriu`, `amenda nedepunere declaratie consum energie` |
| **Pagina țintă** | `/conformare-legea-121-2014/` (nouă) + articolul-pilon existent |
| **Dificultate estimată** | **3 — Medie** pentru variantele comerciale („conformare", „cine face", „cost"). **5 — Foarte ridicată** pentru textul legii în sine. |
| **Argument** | [SERP verificat] SERP-ul pe Legea 121/2014 este dominat de surse instituționale și juridice (legislatie.just.ro, lege5.ro, energie.gov.ro) — **imposibil și inutil de atacat**; nimeni nu cumpără de pe legislatie.just.ro. Dar în același SERP apar și servelect.ro, senys.ro și prahovabusiness.ro — dovadă că **paginile comerciale pot intra**. Golul real: nimeni nu răspunde clar la „cât costă și cine îmi face dosarul". Reduco are preț declarat (2.500–6.000 lei) — poate publica un ghid cu costuri reale, ceea ce aproape nimeni nu face în RO. |
| **Nivel de certitudine** | SERP = date reale. **Discrepanță importantă de rezolvat înainte de a publica:** sursele găsite dau termene diferite pentru declarația anuală de consum (30 aprilie vs 30 iunie), iar pragurile diferă între surse (500 MWh/an în brieful intern vs 1.000 tep/an în surse publice). **Verifică termenul și pragul la sursa primară (energie.gov.ro / textul actualizat al legii) înainte de publicare.** Un articol de conformare cu termen greșit distruge exact credibilitatea pe care o construiește. |

#### Grup 1.3.B — Audit energetic industrial (INFORMAȚIONAL — trafic de anvergură, conversie indirectă)

| | |
| --- | --- |
| **Cuvânt-cheie principal** | `audit energetic obligatoriu companii` |
| **Variante secundare** | `cat costa un audit energetic industrial`, `auditor energetic autorizat lista`, `bilant energetic firma`, `ISO 50001 certificare cost`, `audit energetic la 4 ani obligatie` |
| **Pagina țintă** | Articole de blog → trimit spre `/conformare-legea-121-2014/` |
| **Dificultate estimată** | **4 — Ridicată** |
| **Argument** | [SERP verificat] ENGIE, TÜV SÜD, Enel X, Servelect, afacerist.ro. Autoritate mare, buget mare. **Recomandare: nu construi pagină de serviciu pe „audit energetic".** Reduco nu execută auditul, îl coordonează. Fă conținut informațional care captează căutarea și o convertește spre coordonare/conformare. A minți despre ce execuți se întoarce împotrivă la primul client industrial. |

---

### 1.4 Segment: Prosumator

#### Grup 1.4.A — Prosumator persoană juridică (COMERCIAL)

| | |
| --- | --- |
| **Cuvânt-cheie principal** | `prosumator persoana juridica firma` |
| **Variante secundare** | `prosumator firma decontare surplus`, `Legea 160/2026 prosumatori firma`, `schimbare furnizor prosumator`, `contract prosumator care furnizor e mai bun`, `compensare cantitativa prosumator`, `fotovoltaice firma factura energie` |
| **Pagina țintă** | `/consultanta-prosumator/` (păstrată) + `/prosumatori/` consolidat de pe subdomeniu |
| **Dificultate estimată** | **4 — Ridicată** pe termenii generali, **2–3** pe „persoană juridică" / „firmă". |
| **Argument** | [SERP verificat] Zona prosumatorilor are mașinării de conținut foarte active: instalatori-fotovoltaice.ro, siana-energie.ro, greenlead.ro, economisi.ro. Publică rapid și des. **Nu ataca frontal.** Dar aproape tot ce scriu ei e pentru persoane fizice cu 5 kW pe casă. Unghiul B2B (prosumator firmă, decontare pentru companie) e mai slab acoperit. |
| **Oportunitate de timing (reală)** | Legea 160/2026 privind prosumatorii a fost declarată constituțională de CCR (29 aprilie 2026), se aplică contractelor existente la 26 iulie 2026, iar metodologia ANRE are termen legal ~24 septembrie 2026. **Există o fereastră de conținut deschisă acum**, exact pe segmentul unde Reduco are un serviciu identificat intern („abonament prosumator cu schimbarea furnizorului în funcție de istoricul consum/producție"). De publicat în luna 1, nu în luna 5. |
| **Nivel de certitudine** | SERP + datele legislative = din rezultate de căutare publice. **Verifică statusul metodologiei ANRE la momentul publicării** — se poate să fi apărut deja. |

---

### 1.5 Segment: Casnic (terțiar — pâlnie de reputație, NU motor de venit)

| | |
| --- | --- |
| **Cuvânt-cheie principal** | `compara oferte energie electrica` |
| **Variante secundare** | `cea mai buna oferta energie 2026`, `pret kwh furnizori comparatie`, `schimbare furnizor energie pasi`, `compensatie ANRE 100 lei factura`, `reclamatie furnizor energie persoana fizica` |
| **Pagina țintă** | `/compara-oferte-de-energie/`, `/compara-oferte-de-gaz/` (păstrate, retitrate), `/abonamente-casnici/` |
| **Dificultate estimată** | **4–5 — Ridicată spre foarte ridicată** |
| **Argument** | [SERP verificat] Comparatoarele mari, presa (capital.ro), furnizorii și site-urile de conținut ocupă tot. Reduco nu are cum să câștige aici cu resurse rezonabile. |
| **Decizie strategică** | **Nu investi în acest segment.** Păstrează paginile (au trafic și linkuri existente — ștergerea lor pierde echitate degeaba), retitrează-le, dar **scoate-le din navigația principală** și pune-le în footer sub „Instrumente". Rolul lor devine: captează trafic casnic → link intern spre B2B când vizitatorul e administrator de firmă. Nicio pagină casnică nu mai primește buget de conținut. |

---

### 1.6 Cuvinte-cheie de brand și de diferențiere (toate segmentele)

| Cuvânt-cheie | Tip | Dificultate | Notă |
| --- | --- | --- | --- |
| `reduco` | Navigațional | 1 | Deja deținut. Problema e ce **spune** titlul, nu poziția. |
| `consultant energetic independent` | Comercial | 2 | **Estimare calitativă.** Volum mic, dar e teritoriul pe care nimeni nu-l revendică explicit. Merită o pagină/secțiune. |
| `consultant energie fara comision de la furnizor` | Comercial | 1 | Volum foarte mic. Valoare: e fraza care închide vânzarea, nu care aduce trafic. Folosește-o în copy peste tot, nu ca țintă SEO. |
| `recuperare compensatii ANRE firma` | Tranzacțional | **2** | [SERP verificat] Zona ANRE e slab păzită. ⭐ |
| `reprezentare litigiu furnizor energie` | Tranzacțional | **1–2** | [SERP verificat] Practic nimeni. ⭐ |
| `facturare retroactiva energie ilegala` | Informațional→Tranzacțional | **1–2** | **Estimare calitativă**, dar Reduco are un dosar real pe exact această temă (art. 24 alin. 3, Ordin ANRE 5/2023, max 3 luni). Conținut imbatabil. ⭐⭐ |

---

## 2. Arhitectura de site propusă

### 2.1 Principii

1. **Un hub B2B, nu servicii orfane.** Azi `/solutii-imm` nu trimite spre niciun serviciu, iar `/servicii` nu trimite spre `/recuperare-compensatii` și `/monitorizarea-inteligenta`. Asta înseamnă că paginile de serviciu sunt izolate: nu primesc autoritate internă și nu convertesc. Se repară prin `/pentru-firme/` ca pilon care leagă tot.
2. **Nu redenumi URL-uri fără motiv puternic.** Fiecare 301 pierde puțin. Redenumesc doar acolo unde URL-ul actual e activ dăunător.
3. **B2B înainte de B2C peste tot.** Inclusiv pe `/abonamente/`, care azi deschide cu „Casnici".
4. **Segmentare pe punct de consum**, în acord cu noul model de facturare.

### 2.2 Tabelul complet al arhitecturii

Legendă status: **PĂSTRATĂ** = URL și conținut ok, ajustări minore · **RESCRISĂ** = URL păstrat, conținut refăcut · **MUTATĂ** = URL nou + 301 · **NOUĂ** · **DEPRECIATĂ** = 301, dispare

| # | URL recomandat | Status | Cuvânt-cheie țintă | Rol în pâlnie |
| --- | --- | --- | --- | --- |
| 1 | `/` | **RESCRISĂ** | manager energetic pentru firme | TOFU/MOFU — poziționare; hero unic (azi sunt două hero consecutive) |
| 2 | `/pentru-firme/` | **NOUĂ** (pilon) | management energetic pentru firme | MOFU — hub B2B, leagă toate serviciile |
| 3 | `/pentru-firme/imm/` | **MUTATĂ** ← `/solutii-imm` | soluții energie IMM | MOFU — segment |
| 4 | `/pentru-firme/multi-locatie/` | **NOUĂ** | management energie mai multe locații | MOFU — segment de valoare mare |
| 5 | `/pentru-firme/industrial/` | **NOUĂ** | management energetic industrial | MOFU — segment >500 MWh |
| 6 | `/servicii/` | **RESCRISĂ** | servicii management energetic | MOFU — index de servicii, trebuie să linkeze TOATE cele 8 |
| 7 | `/audit-facturi/` | **RESCRISĂ** ⭐ | audit factură energie firmă | **BOFU — produs de intrare, cel mai important CTA de pe site** |
| 8 | `/litigii-anre/` | **RESCRISĂ** ⭐ | reprezentare litigiu ANRE furnizor energie | BOFU — diferențiator #2 |
| 9 | `/recuperare-compensatii/` | **PĂSTRATĂ** + extinsă | recuperare compensații ANRE firmă | BOFU — „fără succes, fără plată" |
| 10 | `/racordare-energie-gaz/` | **RESCRISĂ** | racordare energie electrică și gaz firmă | BOFU — cerere punctuală, ciclu scurt |
| 11 | `/energie-reactiva/` | **NOUĂ** | penalități energie reactivă firmă | BOFU — serviciu de proiect, 1.200–2.500 lei |
| 12 | `/conformare-legea-121-2014/` | **NOUĂ** ⭐ | conformare Legea 121/2014 | BOFU — serviciu de proiect, 2.500–6.000 lei |
| 13 | `/licitatie-furnizare-energie/` | **NOUĂ** | licitație furnizare energie firmă | BOFU — 15–25% din economia primului an |
| 14 | `/monitorizare-consum-energie/` | **MUTATĂ** ← `/monitorizarea-inteligenta` | monitorizare consum energie firmă | MOFU — justifică abonamentul recurent |
| 15 | `/eficienta-energetica/` | **RESCRISĂ** | eficiență energetică pentru firme | MOFU |
| 16 | `/consultanta-prosumator/` | **PĂSTRATĂ** + extinsă | consultanță prosumator firmă | MOFU/BOFU |
| 17 | `/prosumatori/` | **NOUĂ** (consolidare subdomeniu) | prosumator persoană juridică | MOFU — preia `smart.reduco.ro/prosumatori` |
| 18 | `/abonamente/` | **RESCRISĂ** ⭐ | abonament management energetic firmă | BOFU — B2B first, grila nouă |
| 19 | `/abonamente-casnici/` | **NOUĂ** (desprindere) | abonament energie persoane fizice | BOFU B2C — scoate casnicul din calea B2B |
| 20 | `/studii-de-caz/` | **NOUĂ** ⭐ | studii de caz management energetic | MOFU — repară golul de dovadă socială |
| 21 | `/studii-de-caz/facturare-retroactiva-25-luni/` | **NOUĂ** | contestare facturare retroactivă energie | MOFU — dosarul de 82.463,75 lei |
| 22 | `/despre-noi/` | **RESCRISĂ** ⭐ | despre Reduco consultant energetic independent | TOFU — aici trăiește argumentul independenței |
| 23 | `/intrebari-frecvente/` | **NOUĂ** | întrebări frecvente factură energie firmă | TOFU — suport pentru FAQPage schema |
| 24 | `/parteneri-contabili/` | **NOUĂ** | parteneriat contabil recomandări clienți | Canal — recomandări calificate |
| 25 | `/contact/` | **RESCRISĂ** | contact Reduco | BOFU — formular cu Companie/CUI |
| 26 | `/blog/` | **PĂSTRATĂ** | — | TOFU — hub de conținut |
| 27 | `/compara-oferte-de-energie/` | **PĂSTRATĂ**, retitrată | compară oferte energie electrică | TOFU — instrument, mutat în footer |
| 28 | `/compara-oferte-de-gaz/` | **PĂSTRATĂ**, retitrată | compară oferte gaze naturale | TOFU — instrument, mutat în footer |
| 29 | `/cine-suntem/` | **DEPRECIATĂ** ⚠️ | — | 301 → `/despre-noi/`. Conține brandul vechi din 2022. |
| 30 | ~14 pagini `/juridic-*`, `/casnic-*`, `/oferta-*` | **DEPRECIATE** ⚠️ | — | Prețuri din 2022, indexate. Vezi secțiunea 3. |
| 31 | `/optimizare-putere-contractata/` | **NOUĂ** (faza 3) | putere contractată supradimensionată | BOFU — SERP aproape gol |
| 32 | `/racordare-energie-gaz/energie-electrica/` | **NOUĂ** (faza 3) | racordare energie electrică firmă ATR | BOFU |
| 33 | `/racordare-energie-gaz/gaze-naturale/` | **NOUĂ** (faza 3) | racordare gaze naturale firmă | BOFU |

### 2.3 Reguli de linking intern (repară problemele din audit)

Acestea sunt fixuri directe pentru probleme constatate, nu recomandări generale:

| Problemă din audit | Fix concret |
| --- | --- |
| `/solutii-imm` nu trimite spre niciun serviciu | `/pentru-firme/imm/` primește un bloc „Serviciile incluse" cu 6 linkuri: audit-facturi, litigii-anre, racordare, recuperare-compensatii, monitorizare, energie-reactiva |
| `/servicii` nu trimite spre recuperare-compensatii și monitorizare | `/servicii/` listează toate cele 12 servicii, fiecare cu link + descriere de o frază |
| `smart.reduco.ro/prosumatori` e orfan | Link din meniul principal + din `/servicii/` + din footer, până la migrarea completă |
| Articolele B2B trimit spre o pagină casnică | După rescrierea `/audit-facturi/`, verifică ancorele din `/audit-facturi-energie-imm` și `/schimbare-furnizor-energie-firma` |
| Zero dovadă socială B2B | Fiecare pagină de serviciu primește un bloc cu link spre `/studii-de-caz/` |

**Regulă de nav:** meniul principal are maximum 5 intrări — `Pentru firme` · `Servicii` · `Abonamente` · `Studii de caz` · `Despre noi`. Comparatoarele și zona casnică merg în footer.

### 2.4 Decizia despre subdomeniul `smart.reduco.ro`

`smart.reduco.ro` se prezintă azi drept „Analiză Facturi Energie și **Comparator Furnizori**". Adică subdomeniul propriu al Reduco întărește exact poziționarea de care încearcă să scape.

Recomandare, în ordine:
1. **Imediat:** schimbă title/meta pe `smart.reduco.ro` — scoate „Comparator Furnizori".
2. **Luna 1:** `noindex` pe paginile de marketing de pe subdomeniu (păstrează indexabilă doar aplicația, dacă e cazul). Autoritatea unui subdomeniu nu se cumulează cu domeniul principal.
3. **Trimestrul 1:** migrează `/prosumatori` pe `reduco.ro/prosumatori` cu 301. Subdomeniul rămâne strict aplicație (login).

---

## 3. Planul de redirecturi 301

### 3.1 Avertisment de implementare — citește înainte

**Nu am lista exactă a celor ~14 pagini cu prețuri din 2022.** Brieful le descrie doar prin tipar: `/juridic-*`, `/casnic-*`, `/oferta-*`. **Nu le inventez slug-urile.**

Pasul obligatoriu înainte de a scrie orice redirect:

```
1. Google Search Console → Indexare → Pagini → exportă toate URL-urile indexate
2. Screaming Frog pe reduco.ro (crawl complet, inclusiv sitemap.xml)
3. Verifică live: site:reduco.ro/juridic  |  site:reduco.ro/casnic  |  site:reduco.ro/oferta
4. Pentru fiecare URL găsit, notează: are trafic organic? are linkuri externe?
```

**Regula de decizie pe fiecare URL vechi:**
- Are trafic sau linkuri externe → **301 spre cel mai relevant echivalent** (niciodată spre homepage — 301-urile în masă spre homepage sunt tratate ca soft-404).
- Nu are nici trafic, nici linkuri → **410 Gone**. Mai curat decât 301, scoate pagina din index mai repede.

### 3.2 Tabelul de redirecturi

| # | URL vechi | URL nou | Tip | Motiv |
| --- | --- | --- | --- | --- |
| 1 | `/cine-suntem/` | `/despre-noi/` | 301 | Duplicat de intenție cu `/despre-noi`; conține brandul anterior („Comparatot"), nemodificat din 2022. Risc reputațional activ. |
| 2 | `/solutii-imm/` | `/pentru-firme/imm/` | 301 | Intră sub pilonul B2B; azi e o pagină moartă care nu linkează niciun serviciu. |
| 3 | `/monitorizarea-inteligenta/` | `/monitorizare-consum-energie/` | 301 | Slug fără cuvânt-cheie și greu de citit. Noul slug prinde `monitorizare consum energie firma`. |
| 4 | `/juridic-[slug]/` × ~5 | `/abonamente/` | 301 | Prețuri B2B din 2022, încă indexate. Intenția (abonament pentru firmă) există în continuare → 301, nu 410. |
| 5 | `/casnic-[slug]/` × ~5 | `/abonamente-casnici/` | 301 | Prețuri B2C din 2022. Intenția persistă pe segmentul casnic. |
| 6 | `/oferta-[slug]/` × ~4 | `/compara-oferte-de-energie/` sau `/compara-oferte-de-gaz/` | 301 | Ofertele din 2022 nu mai există. Se trimite spre instrumentul viu corespunzător utilității. |
| 7 | Orice `/juridic-*`, `/casnic-*`, `/oferta-*` fără trafic și fără linkuri | — | **410** | Curăță indexul mai rapid decât 301. |
| 8 | `smart.reduco.ro/prosumatori` | `reduco.ro/prosumatori/` | 301 (Trim. 1) | Consolidare de autoritate pe domeniul principal. |
| 9 | Orice URL cu `?` sau `/feed/` din vechile pagini de preț | echivalentul canonic | 301 | Igienă. |

### 3.3 Reguli tehnice de implementare (WordPress)

```apache
# .htaccess — redirecturi la nivel de server, ÎNAINTE de regulile WordPress.
# Server-level bate plugin: mai rapid, nu depinde de PHP, nu se pierde la update.

Redirect 301 /cine-suntem/ https://reduco.ro/despre-noi/
Redirect 301 /solutii-imm/ https://reduco.ro/pentru-firme/imm/
Redirect 301 /monitorizarea-inteligenta/ https://reduco.ro/monitorizare-consum-energie/

# Pentru paginile fără valoare, după verificarea traficului:
Redirect 410 /oferta-[slug-exact]/
```

Checklist:
- [ ] **Un singur salt.** Verifică să nu apară lanțuri A→B→C (Screaming Frog, raportul Redirect Chains).
- [ ] Fără redirect spre pagini care returnează 404 sau 301 mai departe.
- [ ] Actualizează **linkurile interne** să pointeze direct spre destinația finală — un 301 corect nu scuză un link intern leneș.
- [ ] Actualizează `sitemap.xml` — scoate URL-urile vechi, adaugă-le pe cele noi.
- [ ] În GSC: „Removals" **doar** pentru urgențe reputaționale (`/cine-suntem/` cu brandul vechi merită tratament de urgență).
- [ ] Dacă se folosește plugin (Redirection / Rank Math), verifică să nu dubleze regulile din `.htaccess`.
- [ ] Păstrează redirecturile **minimum 12 luni**. Nu le șterge după „s-a reindexat".

---

## 4. Title tags și meta descriptions — gata de copiat

Reguli respectate: title **50–60 caractere** (peste ~580px Google trunchiază), meta **145–160 caractere**. Numărătoarea de mai jos include spațiile. Diacriticele contează ca 1 caracter în numărătoare, dar ocupă lățime normală — sunt sigure.

**Regulă de brand:** „| Reduco" la final pe paginile comerciale. Pe articolele de blog, brandul se omite ca să rămână spațiu pentru cuvântul-cheie.

### 4.1 Tabelul (16 pagini prioritare)

| # | Pagina | Title (car.) | Meta description (car.) |
| --- | --- | --- | --- |
| 1 | `/` ⚠️ | `Manager energetic pentru firme și IMM-uri \| Reduco` **(50)** | `Reduco reduce factura de energie a firmei tale: audit de factură, reprezentare la ANRE, racordare și monitorizare lunară. Independenți de furnizori.` **(148)** |
| 2 | `/pentru-firme/` | `Management energetic pentru firme \| Reduco` **(42)** | `Externalizează managementul energiei: verificăm lunar facturile, negociem contractele și te reprezentăm în fața furnizorului. Pentru IMM-uri și rețele.` **(151)** |
| 3 | `/audit-facturi/` ⭐ | `Audit factură energie pentru firme \| Reduco` **(43)** | `Îți spunem prețul real per kWh pe care îl plătește firma ta, în 48 de ore. Raport de 2 pagini. Dacă nu găsim economie, îți spunem clar în scris.` **(146)** |
| 4 | `/litigii-anre/` ⭐ | `Litigii ANRE și reprezentare furnizor \| Reduco` **(46)** | `Te reprezentăm în fața furnizorului și a ANRE: facturare retroactivă, index eronat, penalități contestate, eșalonare sub minimul legal. Dosare reale.` **(152)** |
| 5 | `/recuperare-compensatii/` | `Recuperare compensații ANRE pentru firme \| Reduco` **(49)** | `Recuperăm compensațiile legale ANRE datorate firmei tale, fără efort intern din partea ta. Onorariu doar din sumele recuperate: fără succes, fără plată.` **(154)** |
| 6 | `/abonamente/` ⚠️ | `Abonamente management energetic firme \| Reduco` **(46)** | `Abonamente Reduco pentru firme, de la 149 lei/lună fără TVA per punct de consum. Monitorizare lunară a facturii, renegociere și reprezentare inclusă.` **(151)** |
| 7 | `/conformare-legea-121-2014/` | `Conformare Legea 121/2014 pentru companii \| Reduco` **(50)** | `Declarația anuală de consum, programul de eficiență și coordonarea auditului energetic. Gestionăm tot dosarul de conformare, de la 2.500 lei per proiect.` **(155)** |
| 8 | `/racordare-energie-gaz/` | `Racordare energie electrică și gaze firme \| Reduco` **(50)** | `Obținem avizul tehnic de racordare (ATR) pentru firma ta, la energie electrică și gaze naturale. Depunem dosarul, urmărim termenele, te ținem la curent.` **(155)** |
| 9 | `/energie-reactiva/` | `Penalități energie reactivă: analiză firme \| Reduco` **(51)** | `Analizăm penalitățile de energie reactivă din factura firmei și dimensionăm compensarea corect. Nu vindem echipamente, deci recomandăm doar ce ai nevoie.` **(154)** |
| 10 | `/monitorizare-consum-energie/` | `Monitorizare consum și facturi energie \| Reduco` **(47)** | `Verificăm lunar factura firmei tale, te alertăm când apare o ofertă mai bună și verificăm clauzele înainte de semnare. Rapoarte clare pentru conducere.` **(153)** |
| 11 | `/pentru-firme/multi-locatie/` | `Energie pentru rețele multi-locație \| Reduco` **(44)** | `Gestionăm energia pentru lanțuri de magazine, restaurante, farmacii și benzinării. Un preț per punct de consum, un raport unic pentru toate locațiile.` **(152)** |
| 12 | `/pentru-firme/industrial/` | `Management energetic industrial \| Reduco` **(40)** | `Pentru consumatori peste 500 MWh/an: conformare Legea 121/2014, licitații de furnizare, analiză de energie reactivă și optimizarea puterii contractate.` **(152)** |
| 13 | `/despre-noi/` ⚠️ | `Despre Reduco: consultant energetic independent` **(47)** | `Reduco nu este furnizor de energie și nu primește comision de la niciun furnizor. Suntem plătiți doar de client, deci putem recomanda plecarea de oriunde.` **(155)** |
| 14 | `/studii-de-caz/` | `Studii de caz: rezultate reale \| Reduco` **(40)** | `Dosare reale de management energetic: facturare retroactivă contestată, compensații recuperate, penalități eliminate. Cu cifre și articole de lege citate.` **(155)** |
| 15 | `/servicii/` | `Servicii de management energetic firme \| Reduco` **(47)** | `Audit de factură, litigii ANRE, recuperare compensații, racordare, energie reactivă, conformare Legea 121 și monitorizare lunară. Toate într-un singur loc.` **(157)** |
| 16 | `/licitatie-furnizare-energie/` | `Licitație furnizare energie pentru firme \| Reduco` **(49)** | `Organizăm licitația de furnizare pentru firma ta și punem furnizorii să concureze pe preț. Onorariu: 15-25% din economia primului an, plătit din economie.` **(157)** |

### 4.2 Cele trei corecturi cu marcaj ⚠️ — verifică-le personal

1. **Homepage.** Titlul actual — „Reduco | Oferte de energie, gaze | Reclamatii ANRE| Racordare" — nu conține „firmă", „IMM" sau „business", are un spațiu lipsă înainte de ultimul pipe, și începe cu „Oferte", ceea ce confirmă exact poziționarea de comparator. Noul title conține „firme" și „IMM-uri" încă din primele cuvinte.
2. **`/abonamente/`.** Meta description actuală conține brandul scris greșit — **„Recudo" → „Reduco"** — plus un preț vechi. Ambele sunt corectate mai sus. **Caută „Recudo" pe tot site-ul**, nu doar în meta: dacă a apărut o dată, probabil apare și în alte locuri (copy, alt text, footer, PDF-uri, subdomeniu).
3. **`/despre-noi/` și `/cine-suntem/`.** Textul „Comparatot" (brandul anterior) trebuie eliminat din tot site-ul înainte de orice altceva.

### 4.3 Implementare în WordPress

- Rank Math sau Yoast → Editează pagina → fila SEO → „Titlu SEO" și „Meta descriere".
- **Nu lăsa titlurile pe șablonul global** (`%title% %sep% %sitename%`) — pierzi controlul lungimii și al cuvintelor.
- Dezactivează generarea automată de meta description din primul paragraf.
- Verifică `og:title` și `og:description` separat — pe multe instalări rămân pe vechea valoare și apar greșit la share pe LinkedIn, care e canalul principal B2B al Reduco.

---

## 5. Structura H1–H2 pentru cele 5 pagini principale

### 5.0 Mai întâi: repară H1-ul global în Elementor

Brieful spune corect: **H1 lipsește pe aproape tot site-ul, din cauza unei setări de șablon, nu din erori izolate.** Nu rezolvi asta editând pagină cu pagină. Ordinea de verificare:

1. **Elementor → Theme Builder → Single / Page template.** Găsește widgetul **Post Title** (sau „Heading" folosit ca titlu) → panoul **Advanced/Layout** → **HTML Tag**. E aproape sigur setat pe `H2` sau `div`. Setează **H1**.
2. Dacă hero-ul e construit manual cu widget **Heading**, verifică fiecare hero — și acolo tagul e adesea `div` pentru control stilistic.
3. **Un singur H1 per pagină.** După fix, crawlează cu Screaming Frog și verifică raportul `H1 → Multiple` și `H1 → Missing`. Ambele trebuie să fie zero.
4. **Nu lăsa logo-ul din header ca H1** — o greșeală frecventă pe temele WordPress. Logo-ul trebuie să fie `<img>` într-un `<div>`, nu într-un `<h1>`.
5. **Contrast:** H1-ul portocaliu pe fundal deschis are 1.86:1, sub minimul WCAG de 4.5:1. Aplică fixul intern deja propus: `#9A3E0A` pentru text pe fundal deschis, `#F99E0A` doar pentru butoane cu text închis. Se rezolvă în același pas cu H1-ul, în Elementor → Site Settings → Global Fonts/Colors.
6. **Homepage:** elimină al doilea hero. Două secțiuni hero consecutive cu același mesaj înseamnă și doi candidați la H1 și un mesaj diluat.

---

### 5.1 Homepage `/`

```
H1  Managerul energetic al firmei tale

    H2  Nu suntem furnizor și nu luăm comision de la niciun furnizor
    H2  Ce facem pentru firma ta
        H3  Verificăm factura și îți spunem prețul real per kWh
        H3  Te reprezentăm în fața furnizorului și a ANRE
        H3  Recuperăm compensațiile care ți se cuvin
        H3  Monitorizăm lunar și te alertăm când apare ceva mai bun
    H2  Pentru cine lucrăm
        H3  IMM-uri cu 1-4 puncte de consum
        H3  Rețele cu mai multe locații
        H3  Consumatori industriali peste 500 MWh/an
    H2  Rezultate din dosare reale
        H3  82.463,75 lei contestați într-un singur dosar
    H2  Începe cu un audit gratuit al facturii
```

Note: H1-ul spune ce ești, nu ce vinzi. „Nu suntem furnizor" apare ca **al doilea element de pe pagină** — e diferențiatorul care azi nu apare nicăieri vizibil. Un singur CTA final, unic pe toată pagina.

### 5.2 `/servicii/`

```
H1  Servicii de management energetic pentru firme

    H2  Analiză și control al costurilor
        H3  Audit de factură
        H3  Analiză de energie reactivă
        H3  Optimizarea puterii contractate
        H3  Monitorizare lunară a facturilor
    H2  Reprezentare și recuperare
        H3  Litigii și relația cu ANRE
        H3  Recuperare de compensații
    H2  Achiziție și contractare
        H3  Licitație de furnizare
        H3  Verificarea clauzelor și renegociere
    H2  Racordare și avize
        H3  Racordare energie electrică (ATR)
        H3  Racordare gaze naturale
    H2  Conformare și eficiență
        H3  Conformare Legea 121/2014
        H3  Eficiență energetică
        H3  Consultanță pentru prosumatori
    H2  Ce este inclus în abonament și ce se plătește per proiect
```

Note: fiecare H3 este un **link către pagina de serviciu**. Asta repară direct constatarea „`/servicii` nu trimite spre `/recuperare-compensatii` și `/monitorizarea-inteligenta`". Ultimul H2 clarifică modelul de business — o confuzie care blochează vânzarea.

### 5.3 `/pentru-firme/` (pilon nou)

```
H1  Management energetic pentru firme și IMM-uri

    H2  Problema: firmele plătesc energie fără să știe cât plătesc de fapt
        H3  Oferta comercială arată doar componenta de furnizare
        H3  Prețul real e total factură fără TVA împărțit la kWh facturați
    H2  Ce verificăm în fiecare factură
        H3  Preț peste piață
        H3  Penalități de energie reactivă
        H3  Tarif de distribuție necorespunzător nivelului de tensiune
        H3  Putere contractată supradimensionată și depășiri de putere
        H3  Consum de gaz facturat pe estimare
        H3  Clauze contractuale dezavantajoase
    H2  Alege pachetul după numărul de puncte de consum
        H3  1 punct de consum
        H3  Până la 4 puncte de consum
        H3  De la 5 puncte de consum
        H3  Peste 500 MWh/an sau obligații Legea 121/2014
    H2  De ce un consultant independent, nu un comparator
    H2  Rezultate din dosare reale
    H2  Începe cu auditul gratuit al facturii
```

Note: secțiunea „Ce verificăm" este **cea mai valoroasă din tot site-ul din perspectiva SEO** — acoperă natural 6 cuvinte-cheie long-tail comerciale într-o structură pe care utilizatorul chiar o citește. Fiecare H3 poate deveni ulterior un articol de blog care linkează înapoi aici.

### 5.4 `/audit-facturi/`

```
H1  Audit de factură la energie pentru firme

    H2  Ce primești: un raport de maximum 2 pagini, în 48 de ore
    H2  Prețul real per kWh — singurul număr comparabil între oferte
    H2  Ce verificăm concret
        H3  Prețul plătit față de piață
        H3  Penalitățile de energie reactivă
        H3  Componentele facturate incorect
        H3  Tariful de distribuție față de nivelul de tensiune
        H3  Puterea contractată și depășirile de putere
        H3  Consumul de gaz facturat pe estimare
        H3  Clauzele contractuale dezavantajoase
    H2  Dacă nu găsim economie, îți spunem clar în scris
    H2  De ce e gratuit prima dată
    H2  Ce urmează după audit
    H2  Întrebări frecvente
        H3  Ce documente îmi trebuie?
        H3  Trebuie să schimb furnizorul?
        H3  Funcționează și pentru gaze naturale?
        H3  Cât durează dacă am mai multe locații?
```

Note: **întreaga pagină se rescrie din registru casnic în registru B2B** — este cea mai urgentă rescriere de pe site, pentru că primește deja trafic B2B calificat pe care îl pierde. „Dacă nu găsim economie, îți spunem clar în scris" e regula internă declarată a Reduco și e cel mai puternic element de încredere pe care îl are; merită H2 propriu, nu o notă de subsol. Blocul de FAQ alimentează schema FAQPage din secțiunea 6.

### 5.5 `/litigii-anre/`

```
H1  Reprezentare în litigii cu furnizorul de energie și la ANRE

    H2  Când ai un caz și nu știi
        H3  Ai primit o factură retroactivă pe mai multe luni
        H3  Indexul facturat nu seamănă cu consumul tău real
        H3  Ți s-a refuzat eșalonarea sau ți s-a oferit sub minimul legal
        H3  Ți se calculează penalități pe o factură contestată
        H3  Contorul a fost demontat fără să fii notificat
    H2  Ce spune legea, concret
        H3  Facturarea nu poate depăși 3 luni (Ordin ANRE 5/2023, art. 24 alin. 3)
        H3  Eșalonarea minimă legală (art. 25 alin. 7)
        H3  Suspendarea penalităților pe factura contestată (art. 29 alin. 5)
    H2  Cum lucrăm un dosar
        H3  Analizăm factura și documentele de măsurare
        H3  Construim contestația cu articolele de lege citate
        H3  Purtăm corespondența cu furnizorul și distribuitorul
        H3  Escaladăm la ANRE dacă e nevoie
    H2  Un dosar real: 82.463,75 lei în dispută
    H2  Cât costă
    H2  Întrebări frecvente
```

Note: **H2 „Când ai un caz și nu știi" este cel mai important element de conversie de pe site.** Majoritatea firmelor nu știu că au un litigiu — știu doar că factura e mare. Fiecare H3 e formulat ca simptom, nu ca termen juridic. Citarea articolelor exacte de lege este ceea ce niciun blog care rankează azi pe ANRE nu face — și e cel mai rapid mod de a construi E-E-A-T real, nu declarat.

---

## 6. Schema markup (JSON-LD)

### 6.1 Ce se pune și unde

| Tip schema | Pagini | Prioritate | Beneficiu realist |
| --- | --- | --- | --- |
| `Organization` + `ProfessionalService` | Doar homepage (o singură dată pe site) | **P0** | Knowledge panel, entitate corectă în Google și în răspunsurile AI |
| `WebSite` | Homepage | P1 | Sitelinks |
| `BreadcrumbList` | Toate paginile interne | **P0** | Breadcrumbs în SERP; ajută la înțelegerea ierarhiei `/pentru-firme/*` |
| `Service` | Fiecare pagină de serviciu (8–12) | **P0** | Legătură explicită serviciu ↔ furnizor |
| `FAQPage` | `/audit-facturi/`, `/litigii-anre/`, `/intrebari-frecvente/`, `/abonamente/` | P1 | **Vezi avertismentul de mai jos** |
| `BlogPosting` + `author` | Toate articolele | **P0** | E-E-A-T. Autorul trebuie să fie o **persoană reală cu nume**, nu „Echipa Reduco" |
| `Offer` / `AggregateOffer` | `/abonamente/` | P2 | Doar dacă prețurile sunt publice și corecte |
| `Review` / `AggregateRating` | Nicăieri, deocamdată | — | **Nu implementa cu un singur testimonial.** Rating agregat pe o recenzie e semnal de spam. Revine în discuție la 10+ recenzii verificabile. |

**Avertisment onest despre FAQPage:** din august 2023, Google afișează rezultate îmbogățite FAQ aproape exclusiv pentru site-uri guvernamentale și de sănătate. **Nu te aștepta la stele/acordeoane în SERP.** Merită totuși implementat, pentru că ajută la înțelegerea entității și la citarea în AI Overviews — dar nu îl vinde intern ca „o să apărem cu întrebări în Google".

### 6.2 Organization + ProfessionalService — homepage

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": ["Organization", "ProfessionalService"],
  "@id": "https://reduco.ro/#organization",
  "name": "Reduco",
  "alternateName": "Reduco Management Energetic",
  "url": "https://reduco.ro/",
  "logo": {
    "@type": "ImageObject",
    "url": "https://reduco.ro/wp-content/uploads/logo-reduco.png",
    "width": 600,
    "height": 200
  },
  "description": "Reduco este consultant energetic independent pentru firme si IMM-uri din Romania: audit de factura, reprezentare in litigii cu furnizorii si la ANRE, recuperare de compensatii, racordare la retea si monitorizare lunara a costurilor cu energia.",
  "slogan": "Nu suntem furnizor si nu primim comision de la niciun furnizor.",
  "areaServed": {
    "@type": "Country",
    "name": "Romania"
  },
  "knowsAbout": [
    "audit factura energie electrica",
    "litigii ANRE",
    "compensatii ANRE",
    "energie reactiva",
    "racordare la reteaua electrica",
    "aviz tehnic de racordare",
    "Legea 121/2014 eficienta energetica",
    "management energetic pentru firme",
    "prosumatori persoane juridice"
  ],
  "email": "COMPLETEAZA@reduco.ro",
  "telephone": "+40-COMPLETEAZA",
  "address": {
    "@type": "PostalAddress",
    "addressCountry": "RO",
    "addressLocality": "COMPLETEAZA",
    "streetAddress": "COMPLETEAZA",
    "postalCode": "COMPLETEAZA"
  },
  "vatID": "RO-COMPLETEAZA",
  "sameAs": [
    "https://www.linkedin.com/company/COMPLETEAZA",
    "https://www.facebook.com/COMPLETEAZA"
  ],
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Servicii de management energetic",
    "itemListElement": [
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Audit de factura la energie", "url": "https://reduco.ro/audit-facturi/" } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Reprezentare in litigii cu furnizorul si la ANRE", "url": "https://reduco.ro/litigii-anre/" } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Recuperare de compensatii ANRE", "url": "https://reduco.ro/recuperare-compensatii/" } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Racordare la retea si obtinere ATR", "url": "https://reduco.ro/racordare-energie-gaz/" } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Conformare Legea 121/2014", "url": "https://reduco.ro/conformare-legea-121-2014/" } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Monitorizare consum si facturi", "url": "https://reduco.ro/monitorizare-consum-energie/" } }
    ]
  }
}
</script>
```

**Câmpurile marcate `COMPLETEAZA` sunt obligatorii de umplut cu date reale.** Nu publica schema cu placeholdere — schema cu date false e mai rea decât lipsa ei. `vatID` cu CUI-ul real este un semnal de legitimitate puternic pentru o firmă de consultanță B2B.

### 6.3 Service — exemplu pe `/audit-facturi/`

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": "https://reduco.ro/audit-facturi/#service",
  "name": "Audit de factura la energie pentru firme",
  "serviceType": "Audit de factura la energie electrica si gaze naturale",
  "description": "Analizam factura de energie a firmei si calculam pretul unitar real platit (total factura fara TVA impartit la kWh facturati). Verificam pretul fata de piata, penalitatile de energie reactiva, componentele facturate incorect, tariful de distributie fata de nivelul de tensiune, puterea contractata si depasirile de putere, consumul de gaz facturat pe estimare si clauzele contractuale dezavantajoase. Livram un raport de maximum 2 pagini in 48 de ore.",
  "provider": { "@id": "https://reduco.ro/#organization" },
  "areaServed": { "@type": "Country", "name": "Romania" },
  "audience": {
    "@type": "BusinessAudience",
    "name": "IMM-uri, retele multi-locatie si consumatori industriali din Romania"
  },
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "RON",
    "description": "Primul audit de factura este gratuit, o singura data per client.",
    "availability": "https://schema.org/InStock",
    "url": "https://reduco.ro/audit-facturi/"
  },
  "termsOfService": "https://reduco.ro/termeni-si-conditii/",
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Ce verificam in audit",
    "itemListElement": [
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Verificarea pretului unitar real fata de piata" } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Identificarea penalitatilor de energie reactiva" } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Verificarea tarifului de distributie fata de nivelul de tensiune" } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Analiza puterii contractate si a depasirilor de putere" } }
    ]
  }
}
</script>
```

Pentru serviciile plătite, înlocuiește blocul `offers` cu interval real:

```json
"offers": {
  "@type": "Offer",
  "priceCurrency": "RON",
  "priceSpecification": {
    "@type": "PriceSpecification",
    "minPrice": "2500",
    "maxPrice": "6000",
    "priceCurrency": "RON",
    "valueAddedTaxIncluded": false
  }
}
```

### 6.4 FAQPage — exemplu pe `/litigii-anre/`

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "@id": "https://reduco.ro/litigii-anre/#faq",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Furnizorul imi poate factura retroactiv pe mai multe luni?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nu nelimitat. Conform Ordinului ANRE 5/2023, art. 24 alin. 3, facturarea de regularizare nu poate acoperi o perioada mai mare de 3 luni. Am contestat cu succes o facturare retroactiva intinsa pe aproximativ 25 de luni exact pe acest temei. Daca ai primit o factura care acopera o perioada mai lunga de 3 luni, ai un motiv de contestatie."
      }
    },
    {
      "@type": "Question",
      "name": "Trebuie sa platesc penalitati pentru o factura pe care am contestat-o?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nu, atat timp cat contestatia este in analiza. Art. 29 alin. 5 prevede suspendarea penalitatilor pe factura contestata. In practica, multi furnizori continua sa calculeze penalitati; cerem in scris suspendarea lor si documentam refuzul pentru dosarul de la ANRE."
      }
    },
    {
      "@type": "Question",
      "name": "Cate rate am dreptul sa cer la esalonare?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Numarul minim de rate este stabilit prin art. 25 alin. 7 si depinde de perioada facturata. Intr-un dosar recent, furnizorul a oferit 20 de rate desi minimul legal aplicabil era de 25. Diferenta a fost obtinuta prin contestatie scrisa, fara proces."
      }
    },
    {
      "@type": "Question",
      "name": "Ce fac daca mi s-a demontat contorul fara sa fiu anuntat?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Este un viciu de procedura care poate invalida rezultatul verificarii metrologice. Verificam trei lucruri: daca titularul a fost notificat inainte de demontare, cine a semnat procesul-verbal si daca avea calitatea sa il semneze, si daca exista documentul de custodie al contorului. Lipsa oricaruia dintre ele este un argument de contestatie."
      }
    },
    {
      "@type": "Question",
      "name": "Cat costa reprezentarea intr-un litigiu cu furnizorul?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Pentru recuperarea de compensatii lucram pe onorariu de succes, intre 20% si 30% din suma efectiv recuperata: daca nu recuperam nimic, nu platesti nimic. Reprezentarea in litigii este inclusa in abonamentele pentru firme, in limita numarului de dosare din pachetul ales."
      }
    }
  ]
}
</script>
```

### 6.5 Reguli de implementare a schemei

- **`@id` consistent.** `https://reduco.ro/#organization` se referențiază din toate celelalte scheme. Fără asta, Google vede entități separate.
- **Fără diacritice în JSON-LD** (așa cum e mai sus) — evită probleme de encoding pe instalări WordPress cu configurări de charset inconsistente. În textul vizibil de pe pagină, diacriticele rămân obligatorii.
- **Conținutul din schema FAQ trebuie să existe vizibil pe pagină.** Schema care descrie conținut inexistent = penalizare manuală.
- În WordPress: Rank Math generează automat `Organization` și `BreadcrumbList`. **Verifică să nu ai duplicate** — o schemă manuală peste una generată de plugin produce două entități Organization conflictuale.
- Validează totul pe `search.google.com/test/rich-results` și `validator.schema.org` înainte de publicare.

---

## 7. Plan de conținut pe 6 luni — 24 de articole B2B

### 7.1 Structura pe clustere

Șase clustere, fiecare legat de un pilon. **Fiecare articol linkează spre pilonul său cu ancoră descriptivă**, iar pilonul linkează înapoi spre 3–4 articole din cluster. Fără această reciprocitate, clusterul e doar o listă de articole.

| Cluster | Pilon | Articole | De ce acest cluster |
| --- | --- | --- | --- |
| **A. Ce ascunde factura** | `/audit-facturi/` | 6 | [SERP verificat] Gol de intenție — nimeni nu servește „verifică-mi factura" |
| **B. Drepturile tale în fața furnizorului** | `/litigii-anre/` + `/recuperare-compensatii/` | 6 | [SERP verificat] SERP nepăzit, Reduco are dosare reale ⭐ |
| **C. Conformare și obligații legale** | `/conformare-legea-121-2014/` | 4 | Există deja articolul-pilon Legea 121/2014 de valorificat |
| **D. Racordare, putere și avize** | `/racordare-energie-gaz/` | 3 | [SERP verificat] Cerere concretă, competiție medie |
| **E. Cum cumperi energie ca firmă** | `/pentru-firme/` | 3 | Furnizorii nu pot scrie onest pe subiect |
| **F. Prosumatori B2B** | `/consultanta-prosumator/` | 2 | Fereastră legislativă deschisă acum (Legea 160/2026) |

### 7.2 Calendarul

**Luna 1 — construiește credibilitatea pe terenul cel mai liber**

| # | Cluster | Titlu propus | Cuvânt-cheie țintă |
| --- | --- | --- | --- |
| 1 | A | Cum calculezi prețul real per kWh pe care îl plătește firma ta (și de ce nu e cel din ofertă) | preț real kwh factură firmă |
| 2 | B | Facturare retroactivă pe 25 de luni: ce spune legea și cum am contestat-o | facturare retroactivă energie legal |
| 3 | B | Compensațiile ANRE pe care firma ta le poate cere și nu le cere | compensații ANRE firmă |
| 4 | F | Legea 160/2026 pentru prosumatori persoane juridice: ce se schimbă pentru firma ta | prosumator persoană juridică 2026 |

Nota pe #4: fereastră de timing reală — legea se aplică contractelor existente la 26 iulie 2026, metodologia ANRE are termen ~24 septembrie 2026. Publică-l în prima lună sau nu-l mai publica.

**Luna 2 — costurile ascunse (SERP-ul cel mai slab)**

| # | Cluster | Titlu propus | Cuvânt-cheie țintă |
| --- | --- | --- | --- |
| 5 | A | Energia reactivă: de ce plătește firma ta penalități și cum scapi de ele | penalități energie reactivă firmă |
| 6 | A | Putere contractată supradimensionată: banii pe care îi plătești pentru nimic | putere contractată supradimensionată |
| 7 | B | Ce faci când indexul de pe factură nu seamănă cu consumul tău real | index factură energie greșit |
| 8 | E | Ce nu îți spune furnizorul când semnezi contractul de energie | clauze contract energie firmă |

Nota pe #6: [SERP verificat] concurență = bloguri personale și un blog maghiar. Cel mai bun raport efort/rezultat din tot planul de conținut.

**Luna 3 — conformare și obligații**

| # | Cluster | Titlu propus | Cuvânt-cheie țintă |
| --- | --- | --- | --- |
| 9 | C | Legea 121/2014 în 2026: cine e obligat, ce depune și până când | obligații Legea 121/2014 companii |
| 10 | C | Cât costă de fapt conformarea cu Legea 121/2014 | cost conformare Legea 121 |
| 11 | B | Cum faci o reclamație la ANRE care chiar produce un rezultat | reclamație ANRE furnizor energie |
| 12 | D | Aviz tehnic de racordare (ATR) pentru firme: pași, termene, costuri reale | ATR firmă costuri |

Nota pe #9: **verifică termenul declarației anuale la sursa primară înainte de publicare** — sursele publice consultate dau termene diferite (30 aprilie vs 30 iunie) și praguri diferite (500 MWh/an vs 1.000 tep/an). Nu publica un articol de conformare cu date neverificate.

Nota pe #10: [SERP verificat] aproape nimeni nu publică prețuri pe această temă. Reduco are interval declarat (2.500–6.000 lei). Transparența de preț este aici un avantaj competitiv, nu o vulnerabilitate.

**Luna 4 — decizii de achiziție**

| # | Cluster | Titlu propus | Cuvânt-cheie țintă |
| --- | --- | --- | --- |
| 13 | E | Cum organizezi o licitație de furnizare a energiei pentru firma ta | licitație furnizare energie firmă |
| 14 | E | Schimbarea furnizorului de energie pentru firmă: pași, termene, capcane | schimbare furnizor energie firmă |
| 15 | A | Tariful de distribuție și nivelul de tensiune: eroarea de facturare pe care n-o vede nimeni | tarif distribuție nivel tensiune |
| 16 | A | Consum de gaz facturat pe estimare: cum verifici și cum ceri regularizarea | gaz facturat pe estimare firmă |

**Luna 5 — segmente și scară**

| # | Cluster | Titlu propus | Cuvânt-cheie țintă |
| --- | --- | --- | --- |
| 17 | A | De ce plătesc locațiile tale prețuri diferite pe kWh, deși sunt aceeași firmă | costuri energie multi-locație |
| 18 | D | Spor de putere: când îți trebuie, cât durează și cât costă | spor de putere firmă |
| 19 | C | Auditul energetic obligatoriu la 4 ani: ce este, cine îl face, ce faci cu rezultatul | audit energetic obligatoriu companii |
| 20 | B | Eșalonarea la plata facturii de energie: câte rate ești îndreptățit să ceri | eșalonare factură energie rate |

**Luna 6 — consolidare și autoritate**

| # | Cluster | Titlu propus | Cuvânt-cheie țintă |
| --- | --- | --- | --- |
| 21 | B | Verificarea metrologică a contorului: ce trebuie să se întâmple și ce se întâmplă de fapt | verificare metrologică contor drepturi |
| 22 | C | ISO 50001 sau conformare simplă: de ce ai nevoie de fapt | ISO 50001 firmă necesitate |
| 23 | D | Racordarea la rețeaua de gaze naturale pentru firme: dosarul complet | racordare gaze naturale firmă |
| 24 | F | Prosumator cu firmă: cum alegi furnizorul în funcție de istoricul de producție | prosumator firmă alegere furnizor |

### 7.3 Reguli de producție

- **Ritm: 4 articole/lună.** Mai bine 4 articole cu cifre reale decât 12 generice. În B2B energetic, un articol care citează „art. 24 alin. 3, Ordinul ANRE 5/2023" bate zece articole care spun „economisește la factură".
- **Lungime:** 1.200–2.000 cuvinte pentru cele informaționale, 800–1.200 pentru cele tranzacționale. Nu umple.
- **Fiecare articol are:** autor persoană reală cu bio și link LinkedIn (E-E-A-T), schema `BlogPosting`, minimum 2 linkuri interne spre pilon și servicii, un CTA spre auditul gratuit, dată de actualizare vizibilă.
- **Actualizează articolul-pilon existent despre Legea 121/2014** înainte de a scrie #9 și #10 — devine hub-ul clusterului C, cu linkuri spre toate cele 4 articole.
- **Reciclare pe LinkedIn:** fiecare articol produce 2–3 postări. LinkedIn e canalul unde decidenții B2B (administrator, director financiar) sunt efectiv accesibili, iar Reduco are deja un flux acolo. SEO-ul construiește activul, LinkedIn aduce traficul inițial și primele linkuri.

---

## 8. Prioritizare după raport impact/efort

### 8.1 Primele 2 săptămâni — igienă critică și opriri de sângerare

Ordonat strict după impact/efort. Nimic din listă nu necesită conținut nou.

| # | Acțiune | Efort | Impact | De ce acum |
| --- | --- | --- | --- | --- |
| 1 | **Repară H1 în șablonul Elementor** (Theme Builder → Post Title → HTML Tag = H1) | 1–2 ore | **Foarte mare** | O singură setare repară toate paginile. Cel mai bun raport din tot documentul. |
| 2 | **Șterge brandul vechi** — „Comparatot" de pe `/cine-suntem/` și „Recudo" din meta pe `/abonamente/`. Caută ambele pe tot site-ul. | 1 oră | **Mare** | Problemă de credibilitate, nu de SEO. Un prospect B2B care vede brandul greșit pleacă. |
| 3 | **Rescrie title + meta pe cele 16 pagini** din secțiunea 4 | 3–4 ore | **Mare** | Homepage-ul spune azi „Oferte de energie" — contrazice direct repoziționarea. |
| 4 | **Schimbă title/meta pe `smart.reduco.ro`** — scoate „Comparator Furnizori" | 30 min | **Mare** | Propriul subdomeniu întărește poziționarea de care fugi. |
| 5 | **Exportă lista completă de URL-uri** din GSC + Screaming Frog și identifică cele ~14 pagini din 2022 | 2 ore | Mediu (activator) | Fără lista exactă nu se pot scrie redirecturile. Blochează pasul 6. |
| 6 | **Implementează redirecturile 301/410** (secțiunea 3) | 2–3 ore | **Mare** | Prețuri din 2022 indexate = riscul ca un prospect să vadă o ofertă expirată. |
| 7 | **Repară formularul de contact:** adaugă Companie + CUI, șterge „Model și capacitate" și „Sunt client Enel" | 1 oră | **Foarte mare** (conversie) | Nu e SEO, dar tot traficul SEO ajunge aici. Câmpuri reziduale = pierdere de încredere. |
| 8 | **Scoate butonul „Alege" din coșul WooCommerce** pe abonamentele Business → înlocuiește cu „Discută cu un consultant" | 2 ore | **Foarte mare** (conversie) | ~4.000 lei/an cu aprobare internă nu se cumpără din coș. |
| 9 | **Elimină 3 din cele 4 popup-uri identice** și încarcă chatul asincron | 2 ore | Mediu | Core Web Vitals + experiență. Efort mic. |
| 10 | **Aplică fixul de contrast** `#9A3E0A` / `#F99E0A` în Elementor → Site Settings → Global Colors | 1–2 ore | Mediu | Accesibilitate; se face în aceeași sesiune Elementor cu #1. |

**Rezultat așteptat la finalul săptămânii 2:** site-ul nu mai contrazice poziționarea, are H1-uri, nu mai afișează prețuri din 2022 și nu mai trimite leadurile B2B în coșul de cumpărături. Zero conținut nou scris.

### 8.2 Prima lună (săptămânile 3–4) — structura B2B

| # | Acțiune | Efort | Impact |
| --- | --- | --- | --- |
| 11 | **Rescrie `/audit-facturi/` în registru B2B** (structura din 5.4) | 1 zi | **Foarte mare** — primește deja trafic B2B pe care îl pierde |
| 12 | **Rescrie `/litigii-anre/`** (structura din 5.5) | 1 zi | **Foarte mare** — diferențiatorul cel mai puternic, azi invizibil |
| 13 | **Construiește `/pentru-firme/`** (structura din 5.3) + 301 `/solutii-imm` | 1–2 zile | **Mare** — pilonul care leagă tot |
| 14 | **Rescrie `/servicii/`** cu linkuri către toate cele 12 servicii | 3 ore | **Mare** — repară izolarea paginilor de serviciu |
| 15 | **Rescrie `/despre-noi/`** cu argumentul independenței ca element principal | 4 ore | **Mare** — singurul argument pe care concurența nu-l poate copia |
| 16 | **Publică `/studii-de-caz/` + dosarul NOVEX** (anonimizat dacă e nevoie) | 1 zi | **Foarte mare** — repară golul total de dovadă socială B2B |
| 17 | **Reorganizează `/abonamente/`:** B2B primul, casnicul mutat pe `/abonamente-casnici/` | 1 zi | **Mare** |
| 18 | **Schema Organization + Service + Breadcrumb** | 4 ore | Mediu-mare |
| 19 | **Publică primele 4 articole** (Luna 1 din secțiunea 7) | 4 zile | Mare |
| 20 | **Leagă `smart.reduco.ro/prosumatori`** din meniu, servicii și footer | 1 oră | Mediu |

**Verificare de sfârșit de lună 1:** crawl Screaming Frog complet — zero pagini fără H1, zero lanțuri de redirect, zero pagini orfane, toate paginile de serviciu accesibile în maximum 2 clicuri din homepage.

### 8.3 Trimestrul 1 (lunile 2–3) — extindere

| # | Acțiune | Impact |
| --- | --- | --- |
| 21 | Pagini de serviciu noi: `/energie-reactiva/`, `/conformare-legea-121-2014/`, `/licitatie-furnizare-energie/` | **Mare** — servicii cu preț de proiect, azi fără pagină |
| 22 | Pagini de segment: `/pentru-firme/multi-locatie/`, `/pentru-firme/industrial/` | Mare |
| 23 | 301 `/monitorizarea-inteligenta/` → `/monitorizare-consum-energie/` + rescriere | Mediu |
| 24 | Articolele 5–12 (lunile 2–3 din calendar) | Mare |
| 25 | Actualizează articolul-pilon Legea 121/2014 ca hub de cluster | Mediu-mare |
| 26 | `/intrebari-frecvente/` + FAQPage pe 4 pagini | Mediu |
| 27 | Migrează `smart.reduco.ro/prosumatori` → `reduco.ro/prosumatori/` | Mediu |
| 28 | `/parteneri-contabili/` — activează canalul de recomandări | Mediu-mare (venit, nu trafic) |
| 29 | Colectează 8–10 testimoniale B2B reale (condiție pentru schema Review mai târziu) | Mare |
| 30 | Unifică logo-ul (verde/portocaliu) și cele 3 nuanțe de portocaliu într-un sistem unic | Mediu |

### 8.4 Trimestrul 2 (lunile 4–6) — autoritate

- Articolele 13–24.
- `/optimizare-putere-contractata/`, `/racordare-energie-gaz/energie-electrica/`, `/racordare-energie-gaz/gaze-naturale/`.
- Link building B2B: asociații patronale, camere de comerț, portaluri de contabilitate, presă de business locală. Studiile de caz cu cifre (82.463,75 lei) sunt cel mai bun activ pentru PR digital — sunt o poveste, nu o reclamă.
- Prima evaluare completă în GSC: poziții, CTR pe noile titluri, pagini care aduc leaduri.

### 8.5 Ce se măsoară (definește-le înainte de a începe, nu după)

| Metrică | De ce | Unde |
| --- | --- | --- |
| Nr. de cereri de audit gratuit de la firme (cu CUI completat) | **KPI principal.** Traficul nu plătește salarii. | Formular / CRM |
| Poziții pe cele 6 cuvinte-cheie ancoră ale clusterelor | Progres real vs zgomot | GSC |
| CTR pe homepage și `/audit-facturi/` | Măsoară direct dacă noile title/meta funcționează | GSC |
| Pagini fără H1 | Trebuie să ajungă și să rămână 0 | Screaming Frog lunar |
| URL-uri indexate cu prețuri din 2022 | Trebuie să ajungă 0 în 4–8 săptămâni | GSC → Indexare |
| Raport trafic B2B / B2C pe pagini | Confirmă că repoziționarea prinde | GA4 |

**Notează starea de bază (baseline) în GSC și GA4 înainte de a schimba primul title.** Fără baseline, în 3 luni nu se poate demonstra nimic.

---

## 9. Ce ar trebui verificat și nu am putut verifica

Listă onestă de puncte oarbe, pentru că domeniul a fost blocat de proxy în această sesiune:

1. **Slug-urile exacte ale celor ~14 pagini din 2022** — obligatoriu de exportat înainte de redirecturi.
2. **Dacă `/despre-noi/` și `/cine-suntem/` există amândouă** sau sunt aceeași pagină cu alias. Schimbă recomandarea de redirect.
3. **Structura reală a blogului** (`/blog/` vs articole în rădăcină) — afectează arhitectura clusterelor.
4. **Dacă Rank Math sau Yoast e instalat** — schimbă modul de implementare al meta-urilor și al schemei.
5. **Dacă există deja schema generată de plugin** — risc de duplicat Organization.
6. **Starea Core Web Vitals** — cele 4 popup-uri și chatul sincron sugerează probleme, dar nu am măsurat.
7. **Dacă `smart.reduco.ro` are trafic organic propriu semnificativ** — decide dacă migrarea e 301 sau doar cross-linking.
8. **Volume reale de căutare** — la primul buget disponibil, o lună de Ahrefs sau Semrush validează sau infirmă estimările calitative din secțiunea 1. Ordinea de prioritate din acest document se bazează pe **compoziția SERP** (verificată) și pe **intenție** (raționament), nu pe volum — de aceea rămâne validă chiar dacă volumele diferă.
