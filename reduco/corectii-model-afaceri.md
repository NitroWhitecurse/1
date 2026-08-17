# Corecții la modelul de afaceri — verificate direct pe site și în contract

Trei greșeli din planul anterior, corectate acum cu surse verificate chiar acum (site live + contractul de mandat). Fiecare corecție are: ce am scris greșit → ce e adevărat, cu dovada → ce se schimbă concret, cu link unde e nevoie de modificare.

---

## Corecția 1 — Abonamentul e o asigurare, nu un „success fee la intrare"

### Ce am scris greșit

În `economie-modele.md` și `plan-crestere-brand.md` (Motorul 1) am recomandat success fee-ul ca „ușă de intrare" pentru serviciul general de negociere — adică am tratat 30% ca fiind modul normal de a plăti pentru orice negociere de tarif.

### Ce e adevărat, verificat acum

Am citit live **[reduco.ro/abonamente](https://reduco.ro/abonamente)** (actualizată 2 septembrie 2025). Toate cele trei trepte Business includ deja, incluse în preț:

| | Basic 99 lei | Standard 199 lei | Premium 399 lei |
|---|---|---|---|
| Audit detaliat facturi/lună | ✅ | ✅ | ✅ |
| Consultanță în litigiile comerciale | ✅ | ✅ | ✅ |
| **Reprezentare juridică inclusă** | **1 caz/an** | **1 caz/an** | **3 cazuri/an** |

Și pe **[reduco.ro/litigii-anre](https://reduco.ro/litigii-anre)**, la întrebări frecvente: *„Este acest serviciu contra cost? În majoritatea cazurilor, NU. Dacă ai apelat deja la un alt serviciu Reduco, asistența la litigiu este gratuită."* Pe **[reduco.ro/audit-facturi](https://reduco.ro/audit-facturi)**, la fel: *„Acest serviciu este gratuit? Da, pentru clienții care folosesc deja alte servicii Reduco."*

**Modelul e exact ca la asigurarea auto**: clientul plătește o primă lunară, și dacă are un incident — o factură greșită, un litigiu cu furnizorul — e deja acoperit, până la 1 sau 3 cazuri pe an, fără facturare suplimentară per caz. Nu e „plătești doar dacă avem rezultat" (asta e alt produs, mai jos). E „plătești lunar ca să fii protejat, ai sau nu nevoie de reprezentare anul acesta."

### Unde apare 30% și doar acolo

Am recitit contractul de mandat (`Contract de mandat juridic REDUCO.docx`). Există **două mandate diferite** în același contract:

- **Mandatele 1–7** — reprezentare, **cu titlu gratuit**: negociere, schimbare furnizor, ATR, sesizări, reclamații, chiar și cereri în instanță. Acestea sunt incluse în abonament.
- **Mandatul 8** — un mandat separat, **„fără reprezentare, cu titlu oneros"**, doar pentru situația în care Reduco **solicită și încasează despăgubiri** de la transportator/distribuitor/furnizor. Aici, și doar aici, contractul prevede *„o remunerație în cuantum de 30% din valoarea despăgubirilor încasate cu orice titlu, reprezentând onorariu de succes"*.

**Deci 30% nu e prețul negocierii unui tarif mai bun — e comisionul pe banii recuperați ca despăgubire**, un produs separat, care se activează *în plus* față de abonament, nu în locul lui.

### Ce se schimbă concret

1. **În discursul de vânzare:** nu se mai vinde abonamentul cu „plătești doar dacă avem rezultat". Se vinde cu analogia de asigurare: *„Plătești lunar, și dacă ai un incident cu furnizorul, ești deja acoperit — până la 3 cazuri pe an, fără cost suplimentar."* 30% se menționează separat, doar când în auditul lunar inclus se găsește o sumă recuperabilă ca despăgubire: *„Am găsit X lei pe care furnizorul ți-i datorează. Îi recuperăm — reținem 30% din suma recuperată, restul e al tău, imediat."*
2. **Pe site, verificare de făcut la persoana care administrează [reduco.ro/abonamente](https://reduco.ro/abonamente):** cele trei trepte Business au azi **liste de beneficii aproape identice** — diferă doar prețul și numărul de reprezentări incluse (1/1/3). Managementul contractelor și „suportul prioritar + 1 audit energetic complet/an" apar la toate cele trei trepte, deși logic ar trebui să fie exclusiv Premium. **De verificat dacă e o greșeală de copiere a textului între trepte** (probabil e — pare un șablon Elementor copiat de 3 ori fără diferențiere) — dacă da, se corectează astfel încât treptele să se diferențieze real, nu doar prin preț.
3. **Discrepanță internă de rezolvat:** fișierul din Drive „abonamente reduco business" (folosit ca sursă în analizele anterioare) arată Basic **fără** reprezentare juridică inclusă (❌), în timp ce site-ul live arată Basic **cu** 1 reprezentare/an. Documentul din Drive e mai vechi. **De decis cu CEO: care versiune e cea corectă azi** — dacă site-ul, actualizăm și documentele interne; dacă Drive-ul, corectăm site-ul.

---

## Corecția 2 — Nu există calendar de expirare a contractelor de furnizare ale clienților

### Ce am scris greșit

În `plan-remediere.md` (P6) și `plan-crestere-brand.md` (Motorul 1) am propus un „calendar de expirări", populat retroactiv din facturile din arhivă, **inclusiv pentru firme care ne-au refuzat oferta** — cu alerte la 90 de zile înainte de expirare, ca mecanism central de recoltare a leadurilor.

### Ce e adevărat

Fondatorul confirmă direct: **nu avem de unde ști când expiră contractele de energie/gaze ale clienților sau prospecților.** Motivul e simplu și l-am ratat: pentru un prospect care a refuzat oferta, **nu avem niciodată factura lui** — deci nu putem ști ce dată de expirare să înregistrăm pentru cineva ale cărui documente nu le-am văzut. Mecanismul era construit pe o presupunere falsă.

### Ce se schimbă concret

**Se elimină din plan** orice referire la „calendar de expirare a contractelor de furnizare ale clienților" ca sursă de leaduri. **Se păstrează, corectat**, doar ce Reduco chiar controlează:

- **Data proprie de reînnoire a abonamentului** — Reduco știe exact când expiră relația contractuală cu fiecare client al său (lunar, sau „Smart" 12+1 luni), pentru că e propriul contract, nu al furnizorului clientului.
- **Durata mandatului — 3 ani de la semnare**, prevăzută explicit în contractul de mandat: *„Mandatul este dat pentru o perioadă de 3 ani începând cu data semnării."* E un reper real de recontact, controlat de noi.
- **Upsell pe portofoliul propriu:** clienții aflați azi pe Basic (1 reprezentare/an) sunt candidați naturali pentru trecerea la Premium (3 reprezentări/an) — nu e nevoie de nicio dată externă, e informație pe care o avem deja în evidența proprie.

Detaliul operațional — cum arată exact recoltarea din portofoliul propriu fără acest mecanism fals — e în lucru cu agentul de business development (mai jos).

---

## Corecția 3 — Motorul 2 (conformarea legală), verificare mai adâncă în curs

Ai cerut o verificare mai aprofundată a datelor de la Motorul 2 (Legea 121/2014), ținând cont de ce face Reduco efectiv. Am identificat deja, doar din verificarea de mai sus, o distincție pe care planul anterior o trecea prea ușor:

**„Audit facturi" (ce face Reduco azi, per [reduco.ro/audit-facturi](https://reduco.ro/audit-facturi)) nu e același lucru cu „audit energetic" (cerut de Legea 121/2014).** Primul e o verificare a facturilor deja emise — tarife, suprataxări, erori de index. Al doilea e o analiză tehnică a circuitului de consum, făcută obligatoriu de un auditor energetic atestat. Planul anterior recomanda parteneriat cu un auditor atestat pentru partea tehnică — corect — dar nu separa suficient de clar ce poate face Reduco singur, cu mandatul existent, chiar de mâine, față de ce are nevoie de partener.

Un agent de cercetare verifică acum, cu surse legale directe (legislatie.just.ro, anre.ro): dacă declarația anuală de consum poate fi depusă de Reduco sub mandatul existent fără atestare nouă, termenul exact al declarației (sursele erau contradictorii — 30 aprilie vs. 30 iunie), și confirmarea fermă a termenului de 30 septembrie. Rezultatul, cu tabel simplu „ce putem face acum / ce cere partener", vine în `verificare-motor2-conformare.md`.

## Ce urmează

Un al doilea agent (business development) construiește chiar acum planul de acțiune pas cu pas, pe 30 de zile, cu scripturile corectate pe modelul de asigurare și fără mecanismul de calendar inexistent — în `plan-business-development.md`. Ambele documente se integrează în `plan-crestere-brand.md` de îndată ce se întorc, cu link-uri exacte oriunde e nevoie de o modificare pe site.
