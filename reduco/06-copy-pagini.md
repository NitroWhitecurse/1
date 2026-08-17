# Reduco.ro — copy gata de implementat pentru repoziționare

Sursă: `00-brief-context.md`, `03-platforma-brand.md`, `04-plan-conversie.md`, `05-dovezi-studii-caz.md`.
Nicio cifră, preț sau afirmație de mai jos nu este inventată — toate provin din aceste patru documente.

**Notă de conformitate aplicată în tot documentul.** Dosarul cu facturare retroactivă de ~25 de
luni (Electrica/DEER) este în curs de soluționare, cu un client real. În acest document, mecanismul
juridic apare **doar** descris impersonal, la nivel de tip de problemă rezolvată ("contestăm
facturări retroactive care depășesc termenul legal", fără nume, fără sumă de 82.463,75 lei atribuită
unui caz anume). Cifrele din auditurile de factură publicabile (3.803 lei/lună, 45.646 lei/an,
cabinetul cu 864 kWh) sunt folosite anonimizat și marcate explicit "exemplu real, client anonimizat"
— conform indicației primite. **Rămâne totuși un pas de confirmat înainte de publicare:**
`05-dovezi-studii-caz.md` le listează ca "publicabil cu acord [scris al clientului]", nu ca deja
aprobate. Vezi lista finală de [DE CONFIRMAT].

Format pentru fiecare pagină: mai întâi **Instrucțiuni de implementare** (context, plasare, note),
apoi **Text final** — gata de copiat direct în WordPress.

---

## 1. Homepage

### 1.1 Instrucțiuni de implementare

- Unește cele două secțiuni hero consecutive existente într-una singură (bug identificat în audit).
- CTA principal, identic peste tot: **„Cere auditul gratuit al facturii"**. Niciun alt buton
  „Alege"/„Cumpără"/„Vezi prețuri" pe pagină.
- Hero se adresează în primul rând firmelor, dar fără să respingă persoanele fizice — segmentul
  B2C există și contribuie la reputație/recomandări (vezi 00, secțiunea 5).
- Banda de dovezi folosește doar cifre verificabile din brief. Cifrele din auditul Suceava/Bacău
  sunt marcate „exemplu real, client anonimizat" — nu se prezintă ca „studiu de caz publicat"
  până la obținerea acordului scris (vezi nota de conformitate de mai sus).
- Secțiunea „Cine ne plătește" e obligatorie pe homepage, pe `/pentru-firme/`, pe `/abonamente/`
  și în footer (04, secțiunea 3.6).
- Contrast text: titluri și link-uri portocalii folosesc `#9A3E0A`, niciodată `#F99E0A` ca text.

### 1.2 Text final

**[HERO]**

# Departamentul tău de energie, fără să angajezi pe nimeni

Verificăm în fiecare lună facturile firmei tale, te reprezentăm în litigii cu furnizorii și cu
ANRE și nu luăm niciun leu de comision de la niciun furnizor. Plătiți exclusiv de tine.

**[Cere auditul gratuit al facturii]**

Trimite ultima factură. Primești în 48 de ore prețul unitar real plătit și punctele unde pierzi
bani — primul pas către verificarea lunară a facturilor tale.

*Ești persoană fizică sau prosumator? Facem auditul gratuit și pentru tine — completezi același
formular, mai jos.*

---

**[SECȚIUNEA DE PROBLEMĂ]**

## Un comparator te ajută o dată pe an. Furnizorul greșește în fiecare lună.

Ai comparat ofertele, ai semnat cu furnizorul cel mai bun de pe piață în ziua aceea. Atât. De
atunci, nimeni nu mai verifică dacă:

- tariful de distribuție corespunde nivelului tău real de tensiune;
- puterea contractată e dimensionată corect sau plătești pentru o rezervă pe care n-o folosești;
- consumul de gaz e facturat pe citire reală sau pe estimare, lună după lună;
- apar penalități de energie reactivă pe care nimeni din firmă nu le-a văzut;
- clauzele din contract au rămas cele semnate acum trei ani, chiar dacă piața s-a schimbat.

Fiecare dintre acestea costă bani, în fiecare lună, fără ca cineva din firmă să observe. Un audit
făcut o singură dată prinde o singură greșeală, la un moment dat. Noi verificăm lunar, cât timp
ești abonat.

---

**[CELE 4 FAMILII DE SERVICII]**

## Ce facem, concret

### Control Lunar — Monitorizare & Audit
Verificăm factura lunar, calculăm prețul unitar real plătit, te alertăm când apare o ofertă mai
bună și verificăm orice clauză nouă înainte să semnezi. Baza fiecărui abonament.
[Detalii →]

### Apărare & Recuperare
Te reprezentăm în contestații la furnizori și în fața ANRE — cu acte, nu cu opinii. Recuperăm
compensații legale pentru firma ta, fără efort intern din partea ta.
[Detalii →]

### Racordare & Conformare
Obținem avizele tehnice de racordare pentru energie electrică și gaze. Pentru firmele cu peste
500 MWh/an, coordonăm dosarul de conformare cu Legea 121/2014.
[Detalii →]

### Eficiență & Regenerabile
Găsim pierderile din consumul curent și recomandăm cum le eliminați. Consiliem prosumatorii care
produc și vând energie.
[Detalii →]

---

**[CINE NE PLĂTEȘTE]**

## Cine ne plătește

Reduco nu este furnizor de energie și nu primește niciun comision de la niciun furnizor. Suntem
plătiți exclusiv de tine — printr-un abonament lunar sau printr-un onorariu calculat din
rezultatul obținut.

De aceea putem recomanda plecarea de la orice furnizor, inclusiv de la cel mai mare. Un
comparator clasic e remunerat de furnizori prin comision — noi nu.

---

**[BANDA DE DOVEZI]**

**48 de ore** — durata standard a unui raport de audit, de la primirea facturii.

**0 lei** — comisionul pe care îl luăm de la furnizori. Zero, structural.

**20–30%** — cât reținem din compensațiile pe care le recuperăm pentru tine. Fără succes, fără
plată.

**45.646 lei/an** — economia găsită la un singur punct de consum pe medie tensiune, printr-un
audit de facturi. *(Exemplu real, client anonimizat.)*

---

**[CTA FINAL]**

## Trimite ultima factură. Afli în 48 de ore cât pierzi.

Dacă găsim o economie, îți spunem exact câți lei pe lună. Dacă nu găsim nimic, îți spunem la fel
de clar, în scris — nu inventăm o problemă ca să vindem un abonament.

**[Cere auditul gratuit al facturii]**

---

## 2. /pentru-firme/

### 2.1 Instrucțiuni de implementare

Structură conform `04-plan-conversie.md`, secțiunea 3.2. Este pagina cea mai importantă
comercial — trebuie legată din meniul principal, din `/servicii`, din `/solutii-imm` și din toate
articolele B2B menționate în audit (`/audit-facturi-energie-imm`, `/schimbare-furnizor-energie-firma`).

Grila de prețuri de mai jos este **propunerea internă**, prezentată explicit ca ordin de mărime,
conform recomandării din 04 (secțiunea 3.1): "prețul final depinde de numărul de puncte de
consum". Necesită aprobare finală înainte de publicare — vezi lista de [DE CONFIRMAT].

Secțiunea de studii de caz folosește exemplele publicabile (Suceava, Bacău) marcate "exemplu
real, client anonimizat" și un paragraf **impersonal**, fără sumă și fără nume, despre tipul de
litigii pe care le administrăm — cazul aflat în curs nu apare sub nicio formă identificabilă.

### 2.2 Text final

**[HERO]**

# Managementul energetic al firmei tale, externalizat

Pentru administratori și directori financiari care nu au timp să verifice lunar facturile de
energie și să conteste abuzurile furnizorilor. Verificăm, negociem și apărăm factura firmei tale
în fiecare lună — plătiți exclusiv de tine, niciodată de furnizor.

**[Cere auditul gratuit al facturii]**

Trimite ultima factură a firmei. Primești în 48 de ore prețul unitar real plătit, comparat cu
piața, și lista punctelor unde pierzi bani.

---

**[CÂT PIERDEȚI FĂRĂ SĂ ȘTIȚI]**

## Cele 8 lucruri pe care le verificăm la fiecare audit

1. **Preț peste piață** — comparăm prețul unitar real plătit cu oferta optimă disponibilă pentru
   profilul tău de consum.
2. **Penalități de energie reactivă** — taxe suplimentare pe care multe firme nu le observă pe
   factură.
3. **Componente facturate incorect** — poziții pe factură care nu corespund contractului semnat.
4. **Tarif de distribuție necorespunzător nivelului de tensiune** — locațiile racordate la medie
   tensiune plătesc uneori tarif de joasă tensiune, sau invers.
5. **Putere contractată supradimensionată** — plătești lunar pentru o rezervă de putere pe care
   n-o folosești niciodată.
6. **Depășiri de putere** — penalizări pentru vârfuri de consum care pot fi evitate prin
   renegociere.
7. **Consum de gaz facturat pe estimare** — luni întregi facturate pe estimare, în loc de citire
   reală.
8. **Clauze contractuale dezavantajoase** — condiții semnate acum câțiva ani, nerevizuite de
   atunci, care nu mai reflectă piața actuală.

Găsim aceste opt lucruri o dată, la audit. Le urmărim în fiecare lună, cât timp ești abonat.

---

**[PACHETELE]**

## Abonamente pe punct de consum, nu pe firmă

Unitatea de facturare e punctul de consum. Cu cât ai mai multe locații, cu atât prețul per
locație scade.

| Pachet | Preț | Acoperire |
| --- | --- | --- |
| **Business Start** | de la 149 lei/lună + TVA [DE CONFIRMAT: preț final] | 1 punct de consum — Control Lunar |
| **Business Control** | de la 349 lei/lună + TVA [DE CONFIRMAT: preț final] | până la 4 puncte de consum — Control Lunar + Apărare & Recuperare |
| **Multi-Locație** *(recomandat pentru rețele)* | de la 89 lei/lună/locație + TVA, minimum 595 lei/lună [DE CONFIRMAT: preț final] | de la 5 puncte de consum — Control Lunar + Apărare & Recuperare, pe toată rețeaua |
| **Industrial** | de la 1.500 lei/lună + TVA, ofertă personalizată [DE CONFIRMAT: preț final] | peste 500 MWh/an sau sub incidența Legii 121/2014 — toate cele 4 familii de servicii |

Prețul final depinde de numărul de puncte de consum și de utilitățile incluse (energie, gaz sau
ambele). Îl stabilim exact după primul audit gratuit, nu înainte.

**[Cere auditul gratuit al facturii]**

---

**[SERVICII DE PROIECT]**

## Servicii plătite din rezultat, unde se poate

| Serviciu | Preț | Model |
| --- | --- | --- |
| Audit de factură | Gratuit, o singură dată | Punct de intrare |
| Analiză de energie reactivă și dimensionarea compensării | 1.200–2.500 lei [DE CONFIRMAT: preț final per proiect] | Preț fix |
| Organizarea licitației de furnizare | 15–25% din economia primului an | Plată din rezultat |
| Recuperare de compensații ANRE | 20–30% din suma recuperată | Fără succes, fără plată |
| Dosar de conformare Legea 121/2014 | 2.500–6.000 lei [DE CONFIRMAT: preț final per proiect] | Preț fix pe proiect |

La recuperarea de compensații, câștigi tu întâi: dacă nu recuperăm nimic, nu plătești nimic.

---

**[CINE NE PLĂTEȘTE]**

## Cine ne plătește

Reduco nu este furnizor de energie și nu primește comision de la niciun furnizor. Suntem plătiți
exclusiv de client — abonament lunar sau onorariu din rezultat. De aceea putem recomanda plecarea
de la orice furnizor, inclusiv de la cel mai mare, fără niciun conflict de interese.

---

**[DOVEZI / STUDII DE CAZ]**

## Ce am găsit la audituri reale

**Un singur punct de consum. Cinci facturi analizate. 45.646 lei pe an, care ieșeau din firmă
fără ca cineva să observe.**
Firmă de producție și comerț, un punct de consum pe medie tensiune. Tarif mediu plătit: 1,24
lei/kWh. Prețul optim disponibil pentru același profil de consum: 1,04 lei/kWh. Economie lunară
găsită: 3.803 lei. Proiecție anuală: 45.646 lei — de aproximativ 15 ori costul anual al unui
abonament de management. *(Exemplu real, client anonimizat.)*

**Un cabinet cu 864 kWh pe lună. Nu e o fabrică. Economia anuală a depășit totuși costul
abonamentului de peste zece ori.**
Cabinet profesional, un punct de consum, consum lunar 864 kWh, preț plătit 1,63 lei/kWh cu TVA.
Ofertă optimă identificată pentru același profil: 1,33–1,36 lei/kWh. Economie: 236–262 lei/lună,
2.832–3.143 lei/an. *(Exemplu real, client anonimizat.)*

**Reprezentare în litigii cu furnizorii și cu ANRE.**
Contestăm facturări retroactive care depășesc termenul legal de 3 luni, indici de consum
supraevaluați de câteva ori față de consumul real măsurat, eșalonări sub minimul legal și
penalități calculate pe facturi aflate în contestație. Documentăm fiecare pas cu acte — nu cu
opinii — și mergem până la capăt. [DE CONFIRMAT: studiu de caz dedicat, cu cifre exacte, se
publică doar după soluționarea definitivă a dosarului aflat în curs și acordul scris al
clientului — vezi `05-dovezi-studii-caz.md`.]

---

**[FAQ]**

## Întrebări frecvente

**De ce să plătesc abonament dacă pot compara ofertele gratuit, o dată pe an?**
Pentru că prețul e doar una dintre cele opt cauze de pierdere pe care le verificăm. Un
comparator te ajută să alegi furnizorul o singură dată. Noi verificăm în fiecare lună dacă
furnizorul ales facturează corect.

**Cine plătește Reduco?**
Tu. Nu luăm comision de la niciun furnizor. Așa recomandăm plecarea de la orice furnizor, chiar
și de la cel mai mare, fără să pierdem nimic.

**Ce se întâmplă dacă auditul nu găsește nicio economie?**
Îți spunem clar, în scris. Nu inventăm o problemă ca să vindem un abonament.

**Cât costă abonamentul dacă avem mai multe locații?**
Prețul se calculează per punct de consum, cu preț mai mic per locație pe măsură ce numărul crește.
Pachetul Multi-Locație pornește de la 89 lei/lună/locație [DE CONFIRMAT: preț final], minimum 595
lei/lună.

**Suntem deja în litigiu cu furnizorul sau cu ANRE — ne puteți ajuta?**
Da. Reprezentarea în litigii cu furnizorii și în fața ANRE e unul dintre cele patru servicii de
bază. Trimite-ne documentele existente și îți spunem în ce stadiu e dosarul și ce pași urmează.

**Cât durează până primim raportul de audit?**
Sub 48 de ore de la primirea facturii.

---

**[CTA FINAL]**

## Trimite ultima factură a firmei

Afli în 48 de ore prețul unitar real plătit și punctele unde pierzi bani. Fără obligații.

**[Cere auditul gratuit al facturii]**

---

## 3. /despre-noi/

### 3.1 Instrucțiuni de implementare

Înlocuiește complet `/cine-suntem/`, care conține textul brandului vechi din 2022. Redirect 301
de la `/cine-suntem/` către `/despre-noi/` (04, secțiunea 3.4).

Pagina trebuie să convingă un director financiar înainte de a semna un contract — nu are ton de
prezentare de companie, are ton de explicație directă: cine suntem, ce știm să facem, cum câștigăm
bani. Include povestea repoziționării (reală, nu inventată — plecăm de la diagnosticul din 03),
competența juridică (descrisă generic, fără dosarul în curs), modelul de remunerare, și un loc
pentru echipă cu nume și rol — [DE CONFIRMAT], nu avem nume reale.

### 3.2 Text final

# Despre Reduco

## Am pornit ca instrument de comparare a ofertelor. Am ajuns să reprezentăm firme în litigii de
zeci de mii de lei.

Reduco a început ca un loc unde puteai compara oferte de energie și alege furnizorul potrivit.
Funcționa. Dar am observat un lucru simplu: alegerea furnizorului potrivit rezolvă o singură zi
din contractul tău. Restul contractului — luni și ani de facturare, penalități, clauze, verificări
metrologice — rămâne neverificat, pentru că nimeni din firmă nu are timpul sau competența internă
să-l urmărească lunar.

Așa am devenit ceea ce suntem astăzi: un serviciu de management energetic externalizat. Nu mai
comparăm o dată pe an. Verificăm în fiecare lună fiecare punct de consum al firmei tale și te
reprezentăm în fața furnizorilor și a ANRE, cu acte, nu cu opinii.

---

## Ce știm să facem, concret

Verificăm facturi de energie și gaz în fiecare lună: prețul unitar real plătit, tariful de
distribuție aplicat, puterea contractată, penalitățile de energie reactivă, clauzele contractuale.
Livrăm un raport de audit standardizat, de maximum 2 pagini, în 48 de ore de la primirea facturii.

Reprezentăm firme în contestații la furnizori și în fața ANRE: facturări retroactive care depășesc
termenul legal, indici de consum supraevaluați față de consumul real măsurat, vicii de procedură
la verificarea metrologică, eșalonări sub minimul legal, penalități calculate pe facturi aflate
în contestație. Recuperăm compensații legale, fără efort intern din partea clientului.

Obținem avize tehnice de racordare pentru energie electrică și gaze naturale. Pentru consumatorii
cu peste 500 MWh/an, coordonăm dosarul de conformare cu Legea 121/2014 — declarația anuală de
consum, programul de eficiență, legătura cu managerul energetic atestat. **Reduco nu înlocuiește
managerul energetic atestat cerut de lege peste 500 MWh/an** — găsim, coordonăm și administrăm
partea de proces din jurul lui.

---

## Cum câștigăm bani

Nu suntem furnizor de energie. Nu primim comision de la niciun furnizor. Câștigăm din două surse,
amândouă plătite exclusiv de client:

- **Abonament lunar**, calculat pe numărul de puncte de consum ale firmei — de la 149 lei/lună
  pentru o singură locație [DE CONFIRMAT: preț final].
- **Onorariu din rezultat**, la recuperarea de compensații (20–30% din suma recuperată, fără
  succes fără plată) și la organizarea licitațiilor de furnizare (15–25% din economia primului
  an).

Nu avem niciun motiv comercial să te ținem la un furnizor scump sau la un contract dezavantajos.
Motivul pentru care lucrăm bine este că suntem plătiți doar de tine.

---

## Regula pe care o respectăm chiar și când nu ne convine

Dacă auditul unei facturi nu găsește nicio economie, spunem asta clar, în scris. Nu inventăm o
problemă ca să justificăm un abonament. Prima interacțiune cu Reduco e gratuită și fără obligații
tocmai ca să poți verifica asta singur, înainte de a plăti ceva.

---

## Echipa

[DE CONFIRMAT: nume, roluri și fotografii ale echipei — pagina are nevoie de persoane reale,
verificabile, pentru a convinge un director financiar. Momentan nu avem aceste date.]

---

**[Cere auditul gratuit al facturii]**

---

## 4. /servicii/

### 4.1 Instrucțiuni de implementare

Restructurare completă pe cele 4 familii din `03-platforma-brand.md`, secțiunea 6. Astăzi pagina
nu trimite spre `/recuperare-compensatii` și `/monitorizarea-inteligenta` — corectat mai jos.
Fiecare familie leagă spre cele două pagini de serviciu componente.

Slug-uri confirmate din brief: `/audit-facturi`, `/monitorizarea-inteligenta`, `/litigii-anre`,
`/recuperare-compensatii`, `/racordare-energie-gaz`, `/consultanta-prosumator`. Slug-urile pentru
pagina de eficiență energetică și pentru pagina Legea 121/2014 nu apar explicit în brief — vezi
[DE CONFIRMAT].

### 4.2 Text final

# Servicii de management energetic

Patru familii de servicii, toate plătite exclusiv de tine, niciodată de un furnizor.

---

## Control Lunar — Monitorizare & Audit

Baza fiecărui abonament. Verificăm dacă plătești corect, o dată la audit și apoi în fiecare lună
cât timp ești abonat.

- **[Audit de factură](/audit-facturi)** — livrabil în 48 de ore, gratuit, o singură dată. Calculează
  prețul unitar real plătit și verifică cele 8 cauze frecvente de pierdere.
- **[Monitorizare inteligentă și management de contract](/monitorizarea-inteligenta)** — verificare
  lunară a facturii, alertă când apare o ofertă mai bună, verificarea clauzelor înainte de
  semnare, renegociere, raport lunar pentru conducere.

---

## Apărare & Recuperare

Intervenție juridică activă, nu doar analiză. Ești reprezentat, nu doar informat.

- **[Reprezentare în litigii și relația cu ANRE](/litigii-anre)** — contestăm facturări
  retroactive care depășesc termenul legal, indici de consum supraevaluați, vicii de procedură la
  verificarea metrologică și eșalonări sub minimul legal. Documentăm fiecare pas cu acte.
- **[Recuperare de compensații](/recuperare-compensatii)** — recuperăm compensații legale ANRE
  pentru firma ta, fără efort intern din partea ta. Plătit 20–30% doar din suma recuperată — fără
  succes, fără plată.

---

## Racordare & Conformare

Proceduri administrative și reglementate, cu documentație obligatorie.

- **[Racordare la rețea și ATR](/racordare-energie-gaz)** — obținem avizele tehnice de racordare
  pentru energie electrică și gaze naturale. [DE CONFIRMAT: preț]
- **[Conformare Legea 121/2014](/conformare-legea-121)** [DE CONFIRMAT: slug final al paginii] —
  pentru consumatori peste 500 MWh/an: declarația anuală de consum, programul de eficiență,
  coordonarea auditului energetic, legătura cu managerul energetic atestat. Preț de proiect:
  2.500–6.000 lei [DE CONFIRMAT: preț final]. *Reduco nu înlocuiește managerul energetic atestat
  cerut de lege — coordonăm și administrăm procesul din jurul lui.*

---

## Eficiență & Regenerabile

Reducerea consumului pe termen mediu, nu doar factura curentă.

- **[Eficiență energetică](/eficienta-energetica)** [DE CONFIRMAT: slug final al paginii] —
  analiza consumului curent, identificarea pierderilor și a consumului nejustificat, recomandări
  de reducere. Include și analiza de energie reactivă și dimensionarea compensării (1.200–2.500
  lei [DE CONFIRMAT: preț final]).
- **[Consultanță pentru prosumatori](/consultanta-prosumator)** — pentru firme și persoane fizice
  care produc și vând energie: alegerea furnizorului potrivit în funcție de istoricul de consum
  și de producție.

---

**[Cere auditul gratuit al facturii]**

Toate cele patru familii încep cu același prim pas: trimiți ultima factură, primești în 48 de ore
prețul unitar real plătit și punctele unde pierzi bani.

---

## 5. /audit-facturi/

### 5.1 Instrucțiuni de implementare

Pagina e azi scrisă în registru casnic, deși primește trafic majoritar B2B, din articolele
`/audit-facturi-energie-imm` și `/schimbare-furnizor-energie-firma` (00, secțiunea 6). Rescrisă
mai jos cu o secțiune „Pentru firme" explicită, dar fără să elimine segmentul persoane fizice —
formularul de calificare rutează oricum leadul din primul câmp.

Include obligatoriu cele 8 constatări verificate la fiecare audit (aceleași ca pe `/pentru-firme/`,
pentru consecvență de mesaj).

### 5.2 Text final

# Audit de factură — gratuit, în 48 de ore

Trimite ultima factură de energie sau gaz. Primești un raport de maximum 2 pagini, cu prețul
unitar real plătit — total factură fără TVA, împărțit la kWh facturat — singurul număr comparabil
între oferte, pentru că ofertele comerciale afișează doar componenta de furnizare.

**[Cere auditul gratuit al facturii]**

Răspuns în 48 de ore. Fără obligații. Dacă nu găsim nicio economie, îți spunem clar, în scris —
nu inventăm o problemă ca să vindem un abonament.

---

## Ce verificăm — cele 8 constatări din fiecare audit

1. **Preț peste piață** — comparăm prețul unitar real plătit cu oferta optimă pentru profilul tău
   de consum.
2. **Penalități de energie reactivă** — taxe suplimentare, rar observate pe factură.
3. **Componente facturate incorect** — poziții care nu corespund contractului semnat.
4. **Tarif de distribuție necorespunzător nivelului de tensiune** — locații racordate greșit
   tarifar față de nivelul real de tensiune.
5. **Putere contractată supradimensionată** — rezervă de putere neutilizată, plătită lunar.
6. **Depășiri de putere** — penalizări pentru vârfuri de consum evitabile.
7. **Consum de gaz facturat pe estimare** — luni facturate pe estimare, nu pe citire reală.
8. **Clauze contractuale dezavantajoase** — condiții vechi, nerevizuite de la semnare.

---

## Pentru firme

Dacă administrezi o firmă cu unul sau mai multe puncte de consum, auditul gratuit este primul pas
dintr-un serviciu recurent: verificăm aceleași 8 puncte în fiecare lună, nu o singură dată,
alertăm când apare o ofertă mai bună și te reprezentăm dacă apare o facturare incorectă.

Un exemplu real: la un singur punct de consum pe medie tensiune, am identificat o economie de
3.803 lei/lună — 45.646 lei/an — printr-un audit de cinci facturi consecutive. *(Exemplu real,
client anonimizat.)* Un audit funcționează la fel de bine la consumuri mici: la un cabinet
profesional cu 864 kWh/lună, economia anuală a depășit de peste zece ori costul unui abonament
de management. *(Exemplu real, client anonimizat.)*

Dacă vrei verificare lunară, nu doar o dată, vezi [abonamentele pentru firme](/pentru-firme/).

---

## Persoane fizice

Trimite factura de acasă. Primești același raport de 2 pagini, în 48 de ore, cu prețul real
plătit și cu recomandarea clară dacă merită sau nu să schimbi furnizorul.

---

## Cum funcționează

1. **Trimiți ultima factură** — poza, PDF-ul sau scanul, prin formular.
2. **Analizăm în maximum 48 de ore** — prețul unitar real, cele 8 constatări de mai sus, comparat
   cu piața.
3. **Primești raportul pe email** — clar, cu cifre în lei, fără jargon.
4. **Decizi tu** — rămâi la furnizorul actual, schimbi furnizorul, sau continui cu verificare
   lunară.

---

**[Cere auditul gratuit al facturii]**

---

## 6. Formularul de calificare

### 6.1 Instrucțiuni de implementare

Structură conform `04-plan-conversie.md`, secțiunea 3.3 — se elimină câmpurile reziduale
(„Model și capacitate", „Sunt client Enel"). Câmpul firmă/persoană fizică rutează leadul din
primul clic; câmpul „Denumire firmă + CUI" apare doar dacă utilizatorul alege „Firmă" (afișare
condiționată).

Intervalele de consum lunar de mai jos sunt propuse pentru a separa IMM-ul de consumatorul
industrial (prag 500 MWh/an ≈ 41.667 kWh/lună) — [DE CONFIRMAT: pragurile exacte, validate de
echipa operațională].

### 6.2 Text final — etichete și texte de ajutor

**Pasul 1 din 2**

**Sunteți persoană fizică sau firmă?**
*(comutator: „Persoană fizică" / „Firmă")*
Text de ajutor: Alege „Firmă" dacă factura e pe numele unei companii, indiferent de mărime.

**Denumire firmă și CUI** *(afișat doar dacă „Firmă")*
Text de ajutor: Ne ajută să verificăm rapid datele și să pregătim un raport pe numele corect.

**Câte puncte de consum aveți?**
*(select: „1" / „2–4" / „5–10" / „peste 10")*
Text de ajutor: Un punct de consum = o locație cu contor propriu (magazin, sediu, hală, cabinet).

**Care e consumul lunar aproximativ?**
*(select: „sub 2.000 kWh" / „2.000–10.000 kWh" / „10.000–40.000 kWh" / „peste 40.000 kWh")*
Text de ajutor: O estimare e suficientă — o găsești pe orice factură, la rubrica „Energie
consumată".

**Ce utilități verificăm?**
*(bifă: „Energie electrică" / „Gaze naturale" / „Ambele")*

**Atașează ultima factură** *(opțional)*
Text de ajutor: Poza sau PDF-ul facturii. Fără ea, tot pregătim raportul, dar durează un pas în
plus — te vom contacta să ți-o cerem.

**Pasul 2 din 2**

**Nume și prenume**

**Telefon**
Text de ajutor: Te sunăm doar dacă lipsesc informații din factură.

**Email**
Text de ajutor: Aici trimitem raportul de audit, în maximum 48 de ore.

**[Trimite pentru audit gratuit]** *(buton de submit al formularului — echivalentul „Cere auditul
gratuit al facturii" în context de formular)*

Sub buton: Nu te abonăm automat la nimic. Auditul e gratuit și fără obligații.

---

### 6.3 Mesajul de confirmare după trimitere (pe ecran)

**Am primit datele tale.**

Analizăm factura și îți trimitem raportul de audit — prețul unitar real plătit și punctele unde
pierzi bani — în maximum 48 de ore, pe adresa de email indicată.

Dacă găsim o economie, îți spunem exact câți lei pe lună. Dacă nu găsim nimic, îți spunem la fel
de clar, în scris.

Ai atașat factura? Nu mai trebuie să faci nimic. Nu ai atașat-o? Te contactăm în cel mult o zi
lucrătoare ca să ne-o trimiți.

---

### 6.4 Emailul automat de confirmare

**Subiect:** Am primit factura ta — raportul vine în maximum 48 de ore

Bună [Nume],

Am primit cererea ta de audit gratuit. Iată ce urmează:

1. Analizăm factura pe cele 8 puncte pe care le verificăm la fiecare audit: preț peste piață,
   penalități de energie reactivă, componente facturate incorect, tarif de distribuție greșit,
   putere contractată supradimensionată, depășiri de putere, gaz facturat pe estimare, clauze
   dezavantajoase.
2. Îți trimitem raportul, de maximum 2 pagini, în cel mult 48 de ore lucrătoare, la această
   adresă de email.
3. Dacă găsim o economie, vezi exact câți lei pe lună. Dacă nu găsim nimic, îți spunem clar — nu
   inventăm o problemă ca să vindem un abonament.

Dacă nu ai atașat factura la formular, te contactăm în cel mult o zi lucrătoare la numărul
[telefon] ca să ne-o trimiți.

Întrebări până atunci? Răspunde direct la acest email sau scrie-ne la [DE CONFIRMAT: adresă de
contact] / [DE CONFIRMAT: număr de telefon].

Reduco nu este furnizor de energie și nu ia comision de la niciun furnizor. Suntem plătiți
exclusiv de clienții noștri.

[DE CONFIRMAT: nume expeditor / semnătură echipă]

---

## 7. Microcopy

### 7.1 Instrucțiuni de implementare

Regulă unică pe tot site-ul: **un singur CTA comercial, cu același text de bază** — „Cere auditul
gratuit al facturii" — pentru orice buton care duce spre formularul de calificare, indiferent de
pagină. Se elimină orice buton „Alege" care duce direct în coșul WooCommerce pentru pachetele
Business (03, secțiunea 10; 04, secțiunea 3.1). Coșul rămâne doar pentru abonamentul casnic de
24,20 lei, unde achiziția directă are sens.

Link-urile de navigare secundară (către pagini de serviciu, studii de caz) nu concurează cu CTA-ul
principal — sunt link-uri de text, nu butoane de acțiune comercială.

### 7.2 Text final

**Butoane CTA principale (identice peste tot unde apar):**
- „Cere auditul gratuit al facturii"
- „Trimite pentru audit gratuit" *(pe formular, ca variantă de submit)*

**Link-uri secundare de navigare (text, nu butoane comerciale):**
- „Vezi toate serviciile"
- „Vezi cele 8 constatări"
- „Vezi abonamentele pentru firme"
- „Citește cum calculăm prețul unitar real"
- „Detalii →" *(la finalul fiecărui bloc din cele 4 familii de servicii)*

**Mesaje de eroare de formular:**
- Câmp obligatoriu gol: „Acest câmp e obligatoriu — completează-l ca să continui."
- Email invalid: „Adresa de email nu pare validă. Verific-o și încearcă din nou."
- Telefon invalid: „Numărul de telefon nu pare complet. Foloseşte formatul 07XX XXX XXX."
- CUI invalid (când e afișat câmpul firmă): „CUI-ul nu pare valid. Verifică-l pe factură sau pe
  certificatul de înregistrare."
- Fișier prea mare: „Fișierul depășește 10 MB. Încarcă o poză mai mică sau un PDF comprimat."
  [DE CONFIRMAT: limita reală acceptată de formular]
- Format de fișier neacceptat: „Acceptăm poze (JPG, PNG) sau PDF. Încarcă factura într-unul din
  aceste formate."
- Eroare generală de trimitere: „Nu am putut trimite formularul. Verifică datele de mai sus și
  încearcă din nou — dacă problema persistă, scrie-ne direct la [DE CONFIRMAT: adresă de
  contact]."
- Trimitere reușită fără fișier atașat: „Am primit datele tale. Te contactăm în cel mult o zi
  lucrătoare pentru factură."

**Text din footer despre independență:**

> Reduco nu este furnizor de energie și nu primește niciun comision de la furnizori. Suntem
> plătiți exclusiv de clienții noștri — abonament lunar sau onorariu din rezultat. De aceea putem
> recomanda plecarea de la orice furnizor, inclusiv de la cel mai mare.

---

## 8. Lista completă [DE CONFIRMAT]

1. **Grila de prețuri finală** (Business Start 149 lei, Business Control 349 lei, Multi-Locație
   89 lei/locație, Industrial de la 1.500 lei) — propunere internă, necesită aprobare înainte de
   publicare (`04-plan-conversie.md`, secțiunea 8, punctul 1).
2. **Prețul final** pentru racordare la rețea/ATR — nu apare în brief.
3. **Prețul final** pentru analiza de energie reactivă (interval dat: 1.200–2.500 lei) și pentru
   dosarul Legea 121/2014 (interval dat: 2.500–6.000 lei) — intervale confirmate, preț exact per
   proiect de stabilit.
4. **Prețul/lansarea abonamentului dedicat prosumatorilor** — menționat ca „oportunitate
   identificată", nu ca serviciu deja prețuit.
5. **Slug final al paginii de Eficiență energetică** și **al paginii Legea 121/2014** — nu apar
   explicit în brief.
6. **Pragurile exacte ale intervalelor de consum lunar** din formular — propuse pe baza pragului
   de 500 MWh/an, de validat de echipa operațională.
7. **Limita de dimensiune și formatele acceptate** pentru atașarea facturii în formular.
8. **Nume, roluri și fotografii ale echipei** pentru `/despre-noi/` — pagina cere persoane reale
   pentru a convinge un director financiar; nu avem aceste date.
9. **Date de contact** pentru email-ul automat de confirmare și pentru mesajele de eroare —
   număr de telefon, adresă de email de contact, nume expeditor/semnătură.
10. **Confirmarea scrisă a clienților** din exemplele Suceava și Bacău pentru publicarea cifrelor
    (3.803 lei/lună, 45.646 lei/an, 236–262 lei/lună) — `05-dovezi-studii-caz.md` le listează
    „publicabil cu acord", nu ca deja aprobate. Am folosit cifrele anonimizat conform indicației
    primite, dar acordul scris trebuie obținut înainte de publicarea finală pe site.
11. **Studiul de caz dedicat litigiului aflat în curs** — nu se publică sub nicio formă
    identificabilă (nume, sumă atribuită) până la soluționarea definitivă și acordul scris al
    clientului, conform notei de conformitate din `05-dovezi-studii-caz.md`.
