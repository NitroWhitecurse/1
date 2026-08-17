# Reduco — Plan de creștere a brandului

**Obiectiv:** creșterea afacerii și aducerea de clienți noi persoană juridică.
**Orizont:** 90 de zile, cu revizuire săptămânală.
**Construit pe:** toate analizele din această sesiune — poziționare, remedierea celor 10 probleme interne, auditul site-ului, cercetarea competitivă (România + UK/Italia/Polonia/Germania), economia celor 5 modele de venit, declanșatoarele de reglementare. Fiecare capitol citează documentul-sursă din același folder.

---

## Cum e construit planul: trei motoare + o fundație

O firmă de 1–3 oameni nu poate rula zece inițiative deodată. Planul are de aceea **o fundație** (ce reparăm ca să nu turnăm apă într-un vas spart) și **trei motoare de clienți noi**, pornite în ordine, fiecare cu data lui de aprindere:

| | Ce | Se aprinde | De ce în această ordine |
|---|---|---|---|
| Fundația | Cele 10 reparații interne (P0–P10) | Săptămâna 1 | Fără grilă de preț, contract corect și evidență, orice lead nou se pierde sau se vinde prost |
| Motorul 1 | Recolta proprie: calendar de reînnoiri + success fee ca ușă de intrare | Săptămâna 1–2 | Cost zero, folosește arhiva existentă de facturi |
| Motorul 2 | Conformarea legală: Legea 121/2014 + comunități de energie | Săptămâna 2–4 | Termenul de 30 septembrie e la ~6 săptămâni; vinde termen, nu promisiune |
| Motorul 3 | Agregarea: grupul de cumpărare Bacău | Săptămâna 4–8 | Cere o relație instituțională; un contract = 10–30 de firme |

---

## Fundația — cele 10 reparații (rezumat; detaliul complet în `plan-remediere.md` / PDF)

Nu reiau aici conținutul — doar ce deblochează fiecare pentru creștere:

1. **P10 Contract de mandat corectat** (azi, juristul) → instrumentul pe care stau toate motoarele. Fără el nu putem reprezenta pe nimeni la volum.
2. **P3 Grila de preț: plafon 30% din economia dovedită + treapta Business Plus 899 lei** (decizie CEO) → oprește și subfacturarea clienților mari (6,3% capturat la GRIDOMA) și vânzarea nesustenabilă la cei mici (economie netă 21 lei la notariat).
3. **P1 Poziționarea „negociem și te reprezentăm — nu comparăm"** → mesajul pe care îl folosesc toate cele trei motoare. Formulările gata de folosit sunt în `pozitionare.md`.
4. **P5+P6 Tabelul de leaduri cu coloana de expirare a contractelor** → devine chiar combustibilul Motorului 1.
5. **P2 Site-ul** → capitol separat mai jos, actualizat cu re-auditul.
6. **P4 Măsurarea (GA4 + eveniment `lead_juridic`)** → fără ea nu știm care motor duduie și care fumegă.
7. **P7 Raport standard în 48h**, **P8 parteneriat auditor atestat**, **P9 al doilea om** → capacitatea de a procesa ce aduc motoarele.

**Regula fundației: nu se lansează Motorul 2 până nu sunt bifate punctele 1, 2 și 4.** O campanie de conformare cu un contract care inversează părțile ne-ar exploda în față.

---

## Motorul 1 — Recolta proprie: reînnoiri + success fee

*Sursa: `economie-modele.md` (Model B + E), `cercetare-piata.md` (mecanismul F — tem.energy, UK).*

### Ideea într-o frază

Cel mai ieftin client nou e cel care ne-a refuzat acum șase luni — dacă știm luna în care contractul lui expiră și îl sunăm exact atunci, cu o ofertă în care nu are nimic de pierdut.

### De ce funcționează, cu dovada din piață

Startup-ul britanic tem.energy (6.000+ locații active, finanțat de Atomico) a construit o companie întreagă pe exact acest mecanism: detectarea momentului optim de reînnoire și acțiune automată. Partea de „AI" e ambalaj — mecanismul de bază e **un calendar de expirări + alerte + ofertă pregătită dinainte**, replicabil cu un tabel și disciplină.

### Cum îl construim (2–4 săptămâni, MVP)

1. Coloana „data expirării contractului" în tabelul de leaduri (P5/P6) — populată **retroactiv din toate facturile din arhivă**, inclusiv de la firmele care ne-au refuzat.
2. Alertă la **90 de zile** înainte de expirare — atât durează o schimbare de furnizor fără grabă.
3. Scriptul apelului (schelet, nu literă): *„Știu că data trecută nu era momentul potrivit. Fereastra dumneavoastră de reînnoire se deschide în mai puțin de 90 de zile — ați primit deja o propunere proactivă de la actualul furnizor, sau v-au lăsat pe prețurile standard?"*
4. Oferta din apel e **success fee, nu abonament**: „nu plătiți nimic înainte — negociem, iar dacă obținem economie, oprim un procent din ea în primul an."

### De ce success fee la intrare (cifrele din `economie-modele.md`)

- E singurul model din cinci în care **clientul nu poate pierde bani** — elimină exact bariera care face firmele să ezite la abonament.
- La clientul mare captează corect valoarea: cazul GRIDOMA ar genera ~13.700 lei/an la 30% success fee, față de maxim 4.788 lei/an pe Premium.
- La clientul mic rămâne proporțional: notariatul ar plăti ~943 lei/an, în loc de un abonament care îi lasă 21 lei net și se anulează după trei luni.
- **Migrare după dovadă:** după 1–2 cicluri de facturare cu economia vizibilă pe factură, propunem trecerea la retainer (grila cu Business Plus) — predictibilitate pentru noi, „liniște" pentru client.
- **Mandatul 8 din contractul existent prevede deja 30% onorariu de succes pe despăgubiri** — nu introducem un model nou, extindem unul semnat și acceptat de clienți.

### Avantajul pe care nu-l știam că îl avem

În UK, reductorul #1 de fricțiune la intrare e „Letter of Authority" — o împuternicire de o pagină prin care brokerul obține direct datele clientului, în loc să-i ceară facturi PDF. **Contractul nostru de mandat este exact acest instrument**, deja redactat, cu temei în art. 2009 Cod civil. De verificat juridic un singur lucru: dacă furnizorii/distribuitorii români eliberează istoricul de consum către mandatar — dacă da, „trimite-mi 3 facturi" devine „semnează o pagină", și rata de abandon la intrare scade masiv.

### Ținte și responsabil

- Calendarul populat retroactiv: **săptămâna 1** (Marian).
- Primele apeluri pe expirări: **săptămâna 2**.
- Țintă luna 1: **15 apeluri de reînnoire, 5 mandate semnate pe success fee.**
- Metrică de sănătate: % din leadurile noi cărora li se înregistrează data de expirare (ținta: 100%).

---

## Motorul 2 — Conformarea legală: vindem termen, nu promisiune

*Sursa: `declansatoare-reglementare.md` (verificat pe surse legale), `plan-remediere.md` P8.*

### Ideea într-o frază

Economia e o promisiune pe care firma o poate amâna oricând; un termen legal cu amendă nu se amână — iar noi putem fi cei care sună înainte de termen, nu după.

### Cele trei declanșatoare, în ordinea aprinderii

**2a. Termenul de 30 septembrie (acum!).** Firmele peste 1.000 TEP/an trebuie să depună Programul de îmbunătățire a eficienței energetice până la 30 septembrie. Suntem la ~6 săptămâni. Campanie țintită: lista firmelor mari consumatoare din Bacău–Neamț–Suceava (industrie, morărit, depozite frigorifice — racordate MT), apel direct: *„aveți Programul depus? Dacă nu, îl pregătim noi cu partenerul nostru auditor."*
→ Cere parteneriatul cu un **auditor energetic atestat** (P8, calea 2): noi aducem clientul și relația, el semnează, împărțim. Prima discuție de parteneriat: săptămâna aceasta.

**2b. Serviciul de conformare permanent.** Toate firmele — inclusiv IMM-urile — datorează declarația anuală de consum. Aproape nimeni nu știe. Depunerea ei, gratuită, ca serviciu de intrare: firma primește conformare, noi primim **legal, cu acord, exact datele de consum** pe care altfel le cerșim sub formă de factură. ⚠️ Termenul exact (30 aprilie vs. 30 iunie — sursele diferă) se confirmă **în scris la Ministerul Energiei înainte de orice comunicare publică**.

**2c. Comunitățile de energie (fereastra nouă).** Ordinul ANRE 50/25.06.2026 a operaționalizat Registrul național — piața are șapte săptămâni de existență și **nimeni nu are încă experiență practică**. Procedura e birocratică; birocrația e produsul nostru (același mușchi ca la racordare/ATR). Un singur proiect-pilot — un parc industrial, un grup de ferme, o primărie mică cu firmele din jur — ne face „primul facilitator de comunități de energie din Moldova" și aduce 10–30 de membri într-un contract.

### Ținte și responsabil

- Parteneriat auditor semnat: **săptămâna 2** (Marian + CEO).
- Campania „30 septembrie": **20 de firme mari contactate până la 1 septembrie**, țintă 3 contracte de conformare.
- Confirmarea scrisă a termenului declarației: cerere trimisă **săptămâna 1**.
- Un proiect-pilot de comunitate de energie identificat până în **luna 2**.

---

## Motorul 3 — Agregarea: grupul de cumpărare Bacău

*Sursa: `cercetare-piata.md` (mecanismul A — Polonia și Italia), `economie-modele.md` (Model D).*

### Ideea într-o frază

În loc să convingem 30 de firme una câte una, convingem o singură structură — o asociație patronală, Camera de Comerț, un parc industrial — și negociem pentru toți membrii ei deodată.

### Dovada din piață

- Polonia: licitația comună a zonei Gdańsk (2012, 1.911 obiective) a economisit ~4 milioane de zloți față de achiziția individuală; mărimea optimă a grupului: **10–30 de entități**.
- Italia: modelul e reglementat de ARERA; Consorzio Gruppo Acquisti (600+ firme membre) trăiește exclusiv din success fee — *„compensul nostru vine doar dacă obținem economie pentru tine."* Exact modelul nostru de la Motorul 1.

### De ce e motorul cu cel mai mare efect pe termen mediu

- **Recrutare 1-la-mulți:** o singură discuție instituțională deschide zeci de firme.
- **Rezolvă clientul mic fără să-l refuzăm:** firmele sub pragul individual de calificare (~1.400–1.900 lei/lună factură) devin rentabile **prin agregare** — singurul model construit pentru ele.
- **Barieră de intrare minimă pentru membru:** „alătură-te unui grup care negociază pentru tine" e mult mai ușor de spus da decât „abonează-te la un consultant".
- **Nimeni nu o face local.** Concurenții naționali (EnergoPartner etc.) sunt impersonali și fără relații în Bacău.

### Cum îl construim (pilot în 4–8 săptămâni)

1. Lista structurilor-țintă: Camera de Comerț Bacău, patronatele locale, administratorii parcurilor industriale din zonă. **O singură relație e suficientă pentru pilot.**
2. Propunerea pentru structură: membru fondator al grupului, vizibilitate, zero cost — structura oferă membrilor un beneficiu concret fără să miște un deget.
3. Pilot: 10–15 firme, o rundă de cerere de ofertă la 3–5 furnizori, fluxul de colectare a datelor = fluxul de audit existent + mandatul semnat de fiecare membru.
4. Venit: success fee din economia fiecărui membru (coerent cu Motorul 1) — de verificat juridic dacă e nevoie de autorizare de broker (CAEN 3540) sau dacă mandatul acoperă negocierea în grup; alternativ, parteneriat cu un broker autorizat care rulează formal ofertarea, noi ținem relația.

### Ținte și responsabil

- Prima întâlnire instituțională: **săptămâna 4** (Marian sau CEO — deschiderea instituțională e treabă de fondator).
- Pilot lansat: **săptămâna 8**, cu minim 10 firme înscrise.
- Verificarea juridică broker/mandat: **luna 1**, împreună cu avocatul care revizuiește contractul (P10.7).

---

## Site-ul — vitrina care trebuie să susțină toate motoarele

*Sursa: `audit-site.md` + re-auditul complet în curs (`re-audit-site.md` — secțiunea se actualizează la sosire).*

Site-ul nu e un motor de creștere în sine la dimensiunea actuală de trafic — e **locul unde cele trei motoare trimit oamenii ca să verifice că suntem reali**. De aceea prioritatea nu e SEO, ci credibilitatea la prima vizită:

1. **Săptămâna 1, fără dezvoltator:** `noindex` pe cele ~14 pagini cu prețuri din 2022; linkuri din `/solutii-imm` spre cele cinci servicii; corectarea descrierii `/abonamente` („Recudo", preț vechi); redirect `/cine-suntem` → `/despre-noi`.
2. **Luna 1, cu dezvoltator:** diagnosticul de viteză (pagina se randează în ~15 secunde — patru popup-uri identice, chat, scripturi); H1 la nivel de șablon; consolidarea celor 14 pagini vechi cu redirecturi 301.
3. **Pagina nouă care servește motoarele:** un landing `/audit-firme` (sau echivalent) cu un singur mesaj — „Trimite factura sau semnează mandatul de o pagină. Negociem noi. Plătești doar din ce economisești." — și formular cu CUI + telefon + upload factură.
4. **Re-auditul în curs** livrează: inventarul complet al URL-urilor cu verdict păstrează/consolidează/șterge, title/meta propuse pagină cu pagină, arborele final al site-ului, harta 301, verdictul pe zona WooCommerce (coșul de cumpărături pentru un serviciu de consultanță B2B e de re-evaluat) și JSON-LD pentru date structurate. Se execută ca listă de lucru pentru dezvoltator.

---

## Sistemul de măsurare — cele 8 numere ale ședinței săptămânale

| # | Indicator | Motorul | Ținta lunii 1 | Ținta lunii 3 |
|---|---|---|---|---|
| 1 | Firme cu data expirării înregistrată | M1 | 100% din arhivă | 100% din leaduri noi |
| 2 | Apeluri de reînnoire efectuate | M1 | 15 | 25/lună |
| 3 | Mandate semnate pe success fee | M1 | 5 | 10/lună |
| 4 | Firme mari contactate pe termenul 30 sept | M2 | 20 | — (campania se închide) |
| 5 | Contracte de conformare / parteneriate auditor | M2 | 1 partener + 3 clienți | 8 clienți conformare |
| 6 | Structuri instituționale în discuție / membri pilot | M3 | 2 discuții | pilot cu ≥10 firme |
| 7 | Facturi/mandate noi primite total (leaduri calde) | toate | 20 | 40/lună |
| 8 | Venit lunar nou semnat (abonament + fee estimat) | toate | de stabilit după prima lună | creștere lună/lună |

**Regula rămâne:** un număr care lipsește se raportează „nu îl avem", nu se estimează.

---

## Calendarul primelor 30 de zile

| Săptămâna | Fundația | Motorul 1 | Motorul 2 | Motorul 3 |
|---|---|---|---|---|
| 1 | Contract mandat corectat (jurist, azi) · grila 30% aprobată (CEO) · noindex + linkuri site · GA4 | Tabel + expirări populate retroactiv | Cerere scrisă la Minister (termen declarație) · listă firme >1.000 TEP | — |
| 2 | Șablonul de raport 48h | Primele 5 apeluri de reînnoire | Prima discuție cu auditor atestat | — |
| 3 | Textele de poziționare pe site | 10 apeluri; primele mandate success fee | Campania „30 septembrie" pornește | Lista structurilor-țintă |
| 4 | Decizia pe al doilea om (P9) | Bilanț: apeluri→mandate | Parteneriat auditor semnat; primele oferte de conformare | Prima întâlnire instituțională |

---

## Deciziile care rămân la CEO

1. **Grila de preț** — plafonul de 30% și treapta Business Plus 899 lei. *(Blochează tot.)*
2. **Rata de success fee** — 20/30/40% din economia primului an; recomandare: **30%**, aliniată cu onorariul de succes deja existent în mandatul 8.
3. **Parteneriatul cu auditorul atestat** — cine, și pe ce împărțire.
4. **Al doilea om** (P9) — prospectarea și evidența nu pot rămâne în aceleași mâini cu auditul și negocierea peste luna 2.
5. **De explorat, fără decizie acum:** autorizarea ca broker (CAEN 3540 + eventuale cerințe ANRE) — necesară doar dacă grupul de cumpărare nu poate rula pe mandat + partener; verdictul vine de la avocat în luna 1.

## Ce NU facem în primele 90 de zile (la fel de important)

- **Coșul angro / contracte flexibile** (mecanismul E din UK) — cere parteneriat cu un trader OPCOM, 6+ luni; rămâne pe lista de termen lung.
- **Parteneriatul SaaS de facturare** (mecanismul C) — bun, dar ciclul de negociere B2B cu o platformă e de 2–3 luni; îl deschidem abia după ce Motorul 1 rulează.
- **Reclame plătite** — nu înainte ca site-ul să convertească și măsurarea să existe; altfel cumpărăm trafic pe care nu-l vedem și nu-l convertim.
- **Comisionul de la furnizor ca model principal** (Model C) — conflict de interese cu poziția „plătiți de client, nu de furnizor", care e chiar diferențiatorul nostru. Cel mult venit secundar, transparent, mai târziu.
