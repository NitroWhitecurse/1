# Reduco.ro — brief de context pentru repoziționare

Sursă: documente interne Google Drive (august 2026) + informații publice despre reduco.ro.
Scop: repoziționarea brandului din **comparator de prețuri la energie** în **manager energetic**.

---

## 1. Ce este Reduco astăzi (percepția publică)

Titlul actual al site-ului: *„Reduco | Oferte de energie, gaze | Reclamatii ANRE| Racordare"*.
Subdomeniul `smart.reduco.ro` se prezintă drept *„Analiză Facturi Energie și Comparator Furnizori"*.

Percepția rezultată: **un comparator de oferte**, adică un instrument gratuit, tranzacțional,
folosit o dată pe an. Este cea mai slabă poziție posibilă pentru o firmă care vinde abonamente
lunare de management energetic — un comparator nu justifică un abonament recurent.

Pagina `/cine-suntem/` conține încă textul brandului anterior („Comparatot"), nemodificat din 2022.

## 2. Ce face Reduco în realitate (dovedit prin documente interne)

Serviciile reale sunt de **management energetic**, nu de comparare:

### 2.1 Audit de factură (produsul de intrare)
- Livrabil standardizat, max. 2 pagini, în 48 de ore de la primirea facturii.
- Calculează **prețul unitar real plătit** (total factură fără TVA / kWh facturat) — singurul
  număr comparabil între oferte, pentru că ofertele comerciale afișează doar componenta de furnizare.
- Verifică: preț peste piață, penalități de energie reactivă, componente facturate incorect,
  tarif de distribuție necorespunzător nivelului de tensiune, putere contractată supradimensionată,
  depășiri de putere, consum de gaz facturat pe estimare, clauze contractuale dezavantajoase.
- Regulă internă declarată: dacă nu există economie, se spune clar în scris.

### 2.2 Reprezentare în litigii și relația cu ANRE
Cel mai puternic diferențiator, azi aproape invizibil pe site. Exemplu real documentat
(dosar NOVEX SPACE S.R.L. vs Electrica/DEER, 2026):
- Contestarea facturării retroactive pe ~25 de luni (art. 24 alin. 3, Ordinul ANRE 5/2023 —
  facturarea nu poate depăși 3 luni).
- Demontarea unui index supraevaluat de ~4x prin comparație cu consumul real măsurat
  (47,06 kWh/zi „oficial" vs 11,73 kWh/zi real, cu cifre din propriul tabel al furnizorului).
- Vicii de procedură la verificarea metrologică: demontare fără notificarea titularului,
  proces-verbal semnat de o persoană fără calitate, lipsa documentului de custodie.
- Eșalonare sub minimul legal (20 rate oferite vs 25 obligatorii, art. 25 alin. 7).
- Suspendarea penalităților pe factură contestată (art. 29 alin. 5).
- Compensații ANRE calculate și revendicate (~15.000–19.550 lei într-un singur caz).
Total în dispută într-un singur dosar: **82.463,75 lei**.

### 2.3 Recuperare de compensații
Compensații legale ANRE pentru clienți companii, „fără efort intern" din partea clientului.
Model de plată: 20–30% din suma recuperată — **fără succes, fără plată**.

### 2.4 Racordare la rețea și ATR
Energie electrică și gaze naturale — obținerea avizelor tehnice de racordare.

### 2.5 Consultanță pentru prosumatori
Platformă dedicată la `smart.reduco.ro/prosumatori`, azi nelegată de site-ul principal.
Serviciu identificat ca oportunitate: abonament special pentru prosumatori, cu schimbarea
furnizorului în funcție de istoricul de consum/producție.

### 2.6 Eficiență energetică
Analiza consumului curent, identificarea pierderilor și a consumului nejustificat,
recomandări de reducere.

### 2.7 Conformare Legea 121/2014
Pentru consumatori peste 500 MWh/an: declarația anuală de consum, programul de eficiență,
coordonarea auditului energetic, legătura cu managerul energetic atestat.
Preț de proiect: 2.500–6.000 lei.

### 2.8 Monitorizare inteligentă și management de contract
Verificare lunară a facturii, alertă când apare în piață o ofertă mai bună, verificarea
clauzelor înainte de semnare, renegociere, rapoarte pentru conducere.

## 3. Modelul de business și prețurile

### Abonamente actuale (pe site, problematice)
- B2C: 24,20 lei/lună (TVA inclus), 1 locație/utilitate; +10% per serviciu/locație suplimentară.
- B2B: 199 lei + TVA (240,79 lei) pentru 1 locație/utilitate; +10% din bază per locație suplimentară.
- Pachete Business: 99 / 199 / 399 lei — **cu unsprezece beneficii identice**, singura diferență
  fiind numărul de reprezentări juridice. Cumpărătorul nu are motiv să plătească de patru ori mai mult.
- Abonamente: Lunar sau Smart (12 luni + 1 lună gratuită).

### Grila propusă intern (nepublicată încă)
- **Business Start** — 149 lei/lună fără TVA, 1 punct de consum.
- **Business Control** — 349 lei/lună fără TVA, până la 4 puncte de consum.
- **Multi-Locație** — 89 lei/lună per locație, minimum 595 lei/lună, de la 5 puncte de consum.
- **Industrial** — de la 1.500 lei/lună, ofertă personalizată, peste 500 MWh/an sau Legea 121/2014.

Schimbare-cheie a modelului: **unitatea de facturare devine punctul de consum**, nu firma.

### Servicii de proiect, în afara abonamentului
| Serviciu | Preț |
| --- | --- |
| Audit al facturii | gratuit, o singură dată |
| Analiză de energie reactivă și dimensionarea compensării | 1.200 – 2.500 lei |
| Organizarea licitației de furnizare | 15 – 25% din economia primului an |
| Recuperare de compensații | 20 – 30% din suma recuperată |
| Dosar de conformare Legea 121/2014 | 2.500 – 6.000 lei |

## 4. Diferențiatorul structural

**Independența declarată: Reduco nu este furnizor de energie și nu primește comision de la
niciun furnizor.** Este plătit exclusiv de client. De aceea poate recomanda plecarea de la orice
furnizor, inclusiv de la cel mai mare.

Comparatoarele clasice din piață sunt remunerate prin comision de la furnizori — un conflict de
interese structural. Este singurul argument pe care concurența nu îl poate copia fără să-și
schimbe modelul de business. Astăzi nu apare nicăieri vizibil pe site.

Al doilea diferențiator: **competența juridică reală în fața ANRE**, demonstrabilă prin dosare.
Un comparator nu te reprezintă într-un litigiu de 82.000 lei.

## 5. Clientul-țintă

- **Primar (B2B):** IMM-uri și rețele multi-locație — restaurante, hoteluri, magazine, farmacii,
  clinici, săli de fitness, benzinării, ateliere, cabinete. Decident: administrator / director financiar.
- **Secundar (B2B industrial):** consumatori peste 500 MWh/an, cu obligații sub Legea 121/2014.
- **Terțiar (B2C):** persoane fizice și prosumatori — volum mare, valoare mică; util ca pâlnie
  de reputație și recomandări, nu ca motor de venit.
- **Canal de parteneri:** cabinete de contabilitate, ca sursă de recomandări calificate.

## 6. Probleme identificate pe site (audit intern existent)

### Conversie B2B
- Butonul „Alege" de la abonamentele Business duce direct în coșul WooCommerce, nu la o discuție
  de vânzări. Pentru ~4.000 lei/an cu aprobare internă, asta ucide leadul.
- Formularul de contact nu diferențiază persoană fizică de firmă (fără câmp Companie/CUI).
- Formularul conține câmpuri reziduale irelevante („Model și capacitate", „Sunt client Enel").
- `/abonamente/` deschide cu secțiunea „Casnici" — vizitatorul de firmă trebuie să deruleze tot.
- Zero dovadă socială B2B: un singur testimonial pe tot site-ul, pe `/recuperare-compensatii`.
- Argumentul „onorariu doar din succes" (30%) nu apare vizibil nicăieri.

### SEO
- ~14 pagini cu prețuri din 2022 (`/juridic-*`, `/casnic-*`, `/oferta-*`) încă indexate.
- `/cine-suntem/` conține brandul vechi, nemodificat din 2022.
- Title și meta description pe pagina principală nu conțin „firmă", „IMM" sau „business".
- Meta description pe `/abonamente` conține brandul scris greșit („Recudo") și un preț vechi.
- **H1 lipsește pe aproape tot site-ul** — setare greșită în șablonul Elementor, nu erori izolate.
- `/solutii-imm` nu trimite spre niciun serviciu (`/audit-facturi`, `/litigii-anre`,
  `/racordare-energie-gaz`, `/consultanta-prosumator`, `/recuperare-compensatii`).
- `/servicii` nu trimite spre `/recuperare-compensatii` și `/monitorizarea-inteligenta`.
- `/audit-facturi` e scrisă în registru casnic, deși articolele care îi trimit trafic
  (`/audit-facturi-energie-imm`, `/schimbare-furnizor-energie-firma`) sunt integral B2B.
- `smart.reduco.ro/prosumatori` e o platformă separată, fără link din pagina principală.
- Viteză: patru popup-uri identice + chat încărcat sincron.

### Brand și accesibilitate
- Logo cu două culori diferite: verde în header, portocaliu în footer.
- Trei nuanțe de portocaliu/galben folosite fără sistem.
- H1 portocaliu pe fundal deschis: contrast 1.86:1, sub minimul WCAG de 4.5:1.
- Logo footer, stele testimoniale, iconițe galbene: 2.0–2.1:1 vs. 3:1 necesar.
- Fix propus intern: `#9A3E0A` pentru text pe fundal deschis, `#F99E0A` doar pentru butoane
  cu text închis deasupra.
- Homepage are două secțiuni hero consecutive cu mesaj similar.

## 7. Constrângere de mediu

Domeniul reduco.ro este blocat de proxy-ul de rețea în sesiunea curentă. Toate concluziile despre
site provin din auditurile interne din Drive (august 2026) și din rezultate de căutare publice.
Orice recomandare tehnică trebuie verificată pe site înainte de implementare.
