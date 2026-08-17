# Reduco — planul executiv al repoziționării

Documentul de sinteză. Celelalte șase documente conțin detaliul; acesta conține **deciziile,
contradicțiile rezolvate și ordinea de execuție**.

| Document | Ce conține |
| --- | --- |
| `00-brief-context.md` | Inventarul de servicii, prețuri, ICP, probleme identificate |
| `01-cercetare-piata.md` | Harta competitivă verificată, spațiul liber, 7 concluzii de poziționare |
| `02-strategie-seo.md` | Cuvinte-cheie, arhitectură, redirecturi, title/meta, schema, 24 de articole |
| `03-platforma-brand.md` | Poziționarea, categoria, pilonii, tonul, sistemul vizual |
| `04-plan-conversie.md` | Pâlnia B2B, formularul, accesibilitatea, măsurarea |
| `05-dovezi-studii-caz.md` | Dovezile disponibile și regulile de publicare |
| `06-copy-pagini.md` | Copy gata de implementat pentru 5 pagini + formular + microcopy |

---

## 1. Concluzia care schimbă miza

Repoziționarea nu mai este o opțiune strategică. **Statul a preluat produsul.**

POSF.ro, platforma ANRE, oferă astăzi gratuit, oficial, cu semnătură electronică și schimbare
de furnizor în 24 de ore, exact funcția pe care o îndeplinește un comparator privat. Poziția de
comparator se erodează indiferent ce face Reduco — nu din slăbiciune competitivă, ci pentru că
funcția a fost naționalizată.

Asta transformă întrebarea din „ar trebui să ne repoziționăm?" în „cât de repede".

În paralel, cercetarea a confirmat că teritoriul-țintă este liber. Pe două axe — cine plătește
serviciul și ce fel de angajament — cadranul „plătit de client + relație continuă + accesibil
IMM-ului" nu are niciun ocupant. Consultanții industriali (Servelect, SENYS, TÜV SÜD, Adrem)
sunt calibrați pe consumatori mari și nu coboară rentabil la un IMM cu 1–10 puncte de consum.
Avocații contestă facturi, dar nu recalculează prețul unitar real. Comparatoarele nu pot revendica
independența, pentru că modelul lor de venit o interzice.

**Niciun competitor identificat nu are simultan cele trei elemente pe care Reduco le are:**
independență structurală față de furnizori, competență juridică demonstrată în fața ANRE,
și abonament recurent cu preț public. Combinația nu poate fi copiată fără ca imitatorul
să-și schimbe modelul de business.

## 2. Deciziile luate

| # | Decizia | Motivul |
| --- | --- | --- |
| 1 | Categoria revendicată: **„management energetic externalizat"** | „Manager energetic" e rol atestat sub Legea 121/2014. Revendicarea directă e atacabilă. „Externalizat" e o categorie deja familiară (ca „contabilitate externalizată") |
| 2 | Tagline: **„Departamentul tău de energie."** | Comunică relație continuă și responsabilitate delegată, fără să atingă termenul reglementat |
| 3 | CTA unic pe tot site-ul: **„Cere auditul gratuit al facturii"** | Nimeni nu cumpără consultanță de 4.000 lei/an la prima vizită. Auditul e produsul de intrare, deja standardizat la 48h |
| 4 | Cele 8 servicii se regrupează în **4 familii comerciale** | Lista actuală pare o înșiruire disparată. Familiile se mapează direct pe treptele de abonament |
| 5 | Unitatea de facturare devine **punctul de consum**, nu firma | Prețul per firmă lasă bani pe masă la rețelele multi-locație |
| 6 | Se publică **prima grilă de preț B2B din piață** | Zero competitori afișează preț recurent. Primul care publică definește ancora |
| 7 | Comparatorul rămâne, dar ca **unealtă**, nu ca identitate | Util pentru captarea de trafic; dezastruos ca poziționare |
| 8 | Dovezile juridice se folosesc **anonimizat și impersonal** | Dosarul principal e litigiu în curs, cu client real |

## 3. Contradicții între rapoarte — și cum le-am rezolvat

Rapoartele au fost produse independent. Trei puncte au intrat în conflict:

**3.1 Publicarea dosarului de litigiu.** Platforma de brand recomanda un studiu de caz dedicat,
cu numele clientului și suma exactă, ca „cea mai puternică piesă de conținut". Strategia SEO îl
programa în luna 1, „anonimizat dacă e nevoie".

*Decizia:* nu se publică. Este litigiu în curs. Se folosește exclusiv **mecanismul juridic
generic**, impersonal, fără sumă atribuibilă și fără nume — exact cum a fost scris copy-ul.
Publicarea completă devine posibilă după soluționarea definitivă, cu acord scris al clientului
și aviz juridic. Nu „dacă e nevoie" — obligatoriu.

**3.2 Pragul Legii 121/2014.** Documentul intern de copy B2B folosea „peste 500 MWh/an".
Articolul-pilon intern folosea corect „1.000 tep/an ≈ 11.630 MWh/an". Cele două documente
interne se contraziceau.

*Decizia:* pragul corect este **1.000 tep/an**. Eroarea e de două ordine de mărime și ar fi
promis conformare unor firme fără obligație — exact în fața clientului cel mai valoros.
Corectată în `00` și `03`. Regulă generală: niciun prag numeric în copy comercial fără
verificare la textul legii.

**3.3 Poziționarea vs. traficul.** Platforma de brand construiește în jurul „managementului
energetic". Cercetarea a arătat că **nimeni nu caută acest termen** — clienții caută „factură
prea mare la energie", „cum contest factura", „cum îmi recuperez banii".

*Decizia:* se separă cele două. „Management energetic externalizat" este **ce suntem** — apare
în poziționare, pe homepage, pe /despre-noi. Limbajul durerii este **cum intră omul** — apare
în blog, în paginile de serviciu și în title tags. A confunda cele două înseamnă să câștigi
identitatea și să pierzi traficul.

## 4. Primele două săptămâni — nimic nu necesită conținut nou

Ordonate strict după raport impact/efort. Toate sunt reparații, nu creație.

| # | Acțiune | Efort |
| --- | --- | --- |
| 1 | Repară H1 în Elementor Theme Builder (Post Title → HTML Tag = H1) | 1–2 ore |
| 2 | Șterge brandul vechi: „Comparatot" de pe `/cine-suntem/`, „Recudo" din meta pe `/abonamente/` | 1 oră |
| 3 | Înlocuiește butonul „Alege" al pachetelor Business cu „Cere auditul gratuit al facturii" | 2 ore |
| 4 | Curăță formularul: adaugă Companie + CUI, șterge „Model și capacitate" și „Sunt client Enel" | 1 oră |
| 5 | Rescrie title + meta pe cele 16 pagini prioritare | 3–4 ore |
| 6 | Schimbă title/meta pe `smart.reduco.ro` — scoate „Comparator Furnizori" | 30 min |
| 7 | Exportă lista completă de URL-uri din GSC, identifică paginile din 2022 | 2 ore |
| 8 | Implementează redirecturile 301/410 | 2–3 ore |
| 9 | Elimină 3 din cele 4 popup-uri, încarcă chatul asincron | 2 ore |
| 10 | Aplică fixul de contrast în Elementor → Global Colors | 1–2 ore |

**Notează baseline-ul în GSC și GA4 înainte de a schimba primul title.** Fără el, în trei luni
nu se poate demonstra nimic.

Punctul 1 merită subliniat: H1 lipsește pe aproape tot site-ul pentru că e o setare greșită de
șablon, nu erori izolate. O singură modificare repară toate paginile deodată. Este cel mai bun
raport impact/efort din tot planul.

Punctul 2 este mai grav decât pare. `comparatot.ro` nu este doar un brand vechi — este un
comparator **activ** în piață. Site-ul asociază astăzi Reduco cu exact modelul de care fuge.

## 5. Luna 1 — structura B2B

Copy-ul e deja scris pentru toate acestea, în `06-copy-pagini.md`.

1. Rescrie `/audit-facturi/` în registru B2B — primește deja trafic de firme pe care îl pierde.
2. Rescrie `/litigii-anre/` — diferențiatorul cel mai puternic, azi invizibil.
3. Construiește `/pentru-firme/` + redirect 301 de la `/solutii-imm`.
4. Rescrie `/servicii/` pe cele 4 familii, cu linkuri către toate paginile de serviciu.
5. Rescrie `/cine-suntem/` → `/despre-noi/`, cu independența ca argument principal.
6. Reorganizează `/abonamente/`: B2B primul, casnicul pe pagină separată.
7. Schema Organization + Service + Breadcrumb.
8. Primele 4 articole din calendarul editorial.
9. Leagă `smart.reduco.ro/prosumatori` din meniu, servicii și footer.
10. Secțiunea „Cine ne plătește", pe homepage și în footer.

**Verificare de sfârșit de lună:** crawl complet — zero pagini fără H1, zero lanțuri de redirect,
zero pagini orfane, toate paginile de serviciu la maximum 2 clicuri din homepage.

## 6. Oportunitățile pe care le-am găsit și pe care nimeni nu le ocupă

**„Audit de factură" este o categorie liberă.** Căutarea „audit factură energie firmă" returnează
exclusiv *audit energetic tehnic* — ENGIE, TÜV SÜD, Enel X, Servelect. Nimeni nu servește intenția
reală: „verifică-mi factura și spune-mi prețul real per kWh". Reduco poate crea și deține categoria.

**Zona ANRE / litigii este nepăzită.** Rankează astăzi portaluri generaliste și bloguri personale.
Zero jucători B2B. Reduco are dosare reale, cu articole de lege citabile.

**„Putere contractată" și „depășire de putere"** — concurență aproape inexistentă, pentru o
problemă care costă firmele bani în fiecare lună.

**Reforma Legii 121/2014 aduce clientul-țintă prin lege.** Noua versiune, care transpune
Directiva 2023/1791, extinde obligațiile de la marii consumatori la firme mici și mijlocii.
Exemplele citate public — hoteluri medii, platforme industriale mici, spitale, firme de transport
cu flote modeste — sunt literalmente lista de clienți-țintă a Reduco. Jucătorii industriali nu vor
coborî rentabil la acest nivel. Fereastra e deschisă acum.

**Transparența de preț.** Nimeni nu publică o grilă de abonament B2B. Primul care o face
definește ancora la care ceilalți vor fi forțați să răspundă.

## 7. Riscurile de gestionat

| Risc | Gestionare |
| --- | --- |
| Confuzia „manager energetic" cu rolul atestat legal | Formularea e „coordonăm conformarea și lucrăm cu manager energetic atestat", niciodată „suntem" |
| Publicarea unui dosar în curs | Doar mecanism generic, impersonal. Publicare completă după soluționare + acord scris + aviz juridic |
| Praguri legale greșite în copy comercial | Verificare la textul legii înainte de publicare. Pragul e 1.000 tep, nu 500 MWh |
| Câștigi poziționarea, pierzi traficul | Poziția și poarta de intrare rămân separate — vezi 3.3 |
| Promisiunea de 48h nerespectată | Se calibrează capacitatea de livrare înainte de a promite public |
| Trafic pe pagini fără dovezi | Nicio campanie plătită înainte de minimum 3 dovezi publicate |

## 8. Ce am nevoie de la tine ca să merg mai departe

Acestea nu se pot decide din documente — depind de operațiuni:

1. **Grila de prețuri finală.** 149 / 349 / 89-per-locație / 1.500+ sunt propuneri interne,
   necalibrate cu timpul real de livrare per client.
2. **Capacitatea de livrare a auditurilor gratuite.** Câte pe lună pot fi livrate în 48 de ore
   fără a rupe promisiunea? O promisiune de viteză nerespectată face mai mult rău decât lipsa ei.
3. **Acordul scris al celor doi clienți** (Suceava și Bacău) pentru studiile de caz anonimizate.
   Momentul cu cea mai mare rată de acceptare a trecut deja — dar merită cerut.
4. **Politica de perioadă minimă contractuală** — documentul intern o marchează „de confirmat".
5. **Ce se întâmplă cu comparatorul** ca produs public: rămâne gratuit și deschis ca poartă de
   intrare, sau devine beneficiu pentru abonați? Documentele interne conțin ambele variante.
6. **Echipa** — nume, roluri, fotografii pentru `/despre-noi/`. Un director financiar verifică
   pagina asta înainte de a semna.

Lista completă de puncte marcate `[DE CONFIRMAT]` este în `06-copy-pagini.md`, secțiunea 8.

## 9. O limită de care să ții cont

Domeniul reduco.ro a fost **blocat integral** de proxy-ul de rețea în această sesiune. Tot ce am
scris despre starea actuală a site-ului provine din auditurile interne din Drive (august 2026) și
din rezultate de căutare publice. Nimic nu a putut fi reconfirmat direct pe site.

Înainte de implementare, verifică pe site: structura exactă a URL-urilor, ce pagini mai există,
dacă H1-urile lipsesc într-adevăr pe tot site-ul, și lista reală a paginilor cu prețuri din 2022.
Anexa din `01-cercetare-piata.md` listează încă 8 puncte care necesită verificare manuală.
