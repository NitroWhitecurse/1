# Cercetare de piață — poziționare competitivă Reduco

**Data:** 17 august 2026
**Autor:** analiză de piață pentru repoziționarea reduco.ro din „comparator de oferte" în „manager energetic"
**Document sursă:** `00-brief-context.md`

---

## 0. Metodologie, limite și cum să citești acest raport

### 0.1 Ce am putut și ce nu am putut face

| Instrument | Stare | Consecință |
| --- | --- | --- |
| WebSearch | Funcțional | Sursa principală de date |
| WebFetch / curl direct pe site-uri | **Blocat de proxy pe aproape toate domeniile testate** (energolexconsulting.com, adremlink.ro, consultanta-energie.ro, tuvsud.com, senys.ro) | Nu am putut citi paginile competitorilor direct |
| reduco.ro | Blocat explicit de proxy (confirmat: `403 la CONNECT`) | Zero verificare pe propriul site |
| Firecrawl | Fără credite, neutilizat | — |
| Google Keyword Planner / Ahrefs / Semrush | Indisponibile | **Nu am date de volum de căutare. Nicăieri în raport nu veți găsi cifre de volum.** |

### 0.2 Convenția de încredere folosită în tot documentul

- **[VERIFICAT]** — informația provine din conținutul paginii competitorului, așa cum a fost redat de motorul de căutare, cu URL. Atenție: fiind redare de motor, nu citire directă a paginii, formulările pot fi parafrazate. Tratați-le ca „foarte probabil corecte, dar de reconfirmat înainte de a le cita public".
- **[INFERENȚĂ]** — concluzia mea, construită pe baze verificate, marcată ca atare.
- **[NEVERIFICAT]** — n-am găsit sursă. Spun explicit.

### 0.3 Regula pe care am respectat-o

Nu am inventat niciun nume de firmă, niciun preț și nicio cifră de piață. Unde nu am găsit date — în special la **prețurile abonamentelor de management energetic** și la **volumele de căutare** — scrie explicit că nu am găsit.

---

## 1. Cine ocupă azi termenul „management energetic" în România

### 1.1 Constatarea principală

Termenul „management energetic" **este ocupat, dar nu de cine v-ați aștepta și nu pentru clientul pe care îl țintiți.**

În România, „management energetic" este astăzi, în mod covârșitor, un **termen tehnic de conformare industrială**, nu un termen comercial pentru IMM-uri. El înseamnă, în limbajul pieței:

1. un **atestat ANRE / Ministerul Energiei** deținut de o persoană fizică („manager energetic pentru industrie" sau „manager energetic pentru localități");
2. o **obligație legală** a operatorilor economici mari (Legea 121/2014);
3. un **contract tehnic** de monitorizare consum + bilanțuri energetice + rapoarte, vândut ca proiect industrial.

Nimeni din cei identificați nu vinde „management energetic" ca **serviciu administrativ recurent, cu preț afișat, pentru un restaurant cu 3 locații.** Aceasta este observația centrală a raportului.

### 1.2 Cadrul de reglementare care definește termenul

Atestarea persoanelor fizice ca manager energetic pentru industrie / pentru localități și agrearea societăților prestatoare de servicii energetice se fac de **Departamentul pentru Eficiență Energetică din cadrul ANRE (ANRE-DEE)**. [VERIFICAT — [portal.anre.ro/PublicLists/Atestate?menu=Eficiency](https://portal.anre.ro/PublicLists/Atestate?menu=Eficiency), [Regulamentul din 17.12.2014](https://legislatie.just.ro/Public/DetaliiDocumentAfis/165535), [energie.gov.ro — Regulament Manageri Energetici](https://energie.gov.ro/wp-content/uploads/2020/12/Regulament-Manageri-Energetici-1.pdf)]

Există liste publice oficiale, deschise:
- Auditori / manageri energetici atestați — [portal.anre.ro](https://portal.anre.ro/PublicLists/Atestate?menu=Eficiency)
- Societăți prestatoare de servicii energetice agreate — [portal.anre.ro/PublicLists/ListeEficienta/PrestatoriServiciiPJEF](https://portal.anre.ro/PublicLists/ListeEficienta/PrestatoriServiciiPJEF)

**Numărul exact de manageri energetici atestați și de societăți agreate: [NEVERIFICAT].** Listele sunt publice și accesibile, dar nu am putut deschide portalul din această sesiune. **Recomandare operațională: descărcați ambele liste manual — ele sunt, simultan, harta concurenței directe și lista de potențiali parteneri/subcontractori pentru segmentul Industrial.**

### 1.3 Categoria A — Consultanță tehnică industrială și ESCO

Aceștia sunt „proprietarii" actuali ai termenului. Profil comun: vechime mare, portofoliu industrial greu, livrabile tehnice, **zero prețuri afișate**, ciclu de vânzare lung.

**Servelect (Cluj-Napoca)** — [VERIFICAT]
- Fondată în 2005, se poziționează ca „furnizor de economii de energie" cu proiecte integrate de performanță energetică.
- Portofoliu de servicii ESCO: schimbare de tensiune, cogenerare/trigenerare, compensarea energiei reactive, modernizare iluminat, sisteme de monitorizare energetică, automatizări industriale, surse regenerabile, finanțare ESCO, audit energetic, management energetic, implementare ISO 50001, studii de fezabilitate, mentenanță preventivă.
- Clienți industriali citați public: Kronospan, Pehart Tec, MOL România, Holcim Turda, Philips Orăștie, Becotek, Grandemar.
- **Prestator de servicii energetice agreat de Ministerul Energiei, autorizația nr. 0012/26.05.2021.**
- Surse: [servelect.ro/en/about-us](https://servelect.ro/en/about-us/), [servelect.ro/en/energy-manager](https://servelect.ro/en/energy-manager/), [servelect.ro/en/projects-portfolio](https://servelect.ro/en/projects-portfolio/)
- **Preț afișat: niciunul.**

**SENYS (departament al Quartz Matrix)** — [VERIFICAT]
- Peste 15 ani în eficiență energetică; **peste 250 de audituri energetice** realizate.
- Clienți citați: Continental Powertrain România, Delphi Diesel Systems România, OMV Petrom Gas.
- **Auditor energetic / manager energetic autorizat conform Legii 121/2014.**
- Platformă proprie EMS/EnMS: **QLEAP ENEF** (monitorizare consum în timp real, analiză, raportare) și un pachet numit **SEMS — Smart Energy Management Services**, descris ca traseu „de la audit energetic la monitorizare inteligentă".
- Surse: [senys.ro](https://senys.ro/en/), [senys.ro — audit energetic industrial](https://senys.ro/en/audit-energetic-industrial-bilant-energetic/), [senys.ro — manager energetic](https://senys.ro/en/manager-energetic/), [senys.ro — SEMS](https://senys.ro/en/smart-energy-management-services-sems/)
- **Preț afișat: nu pe pagina de serviciu.** Însă SENYS publică intervale de preț în articolele sale de tip ghid (vezi secțiunea 4) — este singurul competitor identificat care face asta.
- **Notă de risc competitiv:** SENYS este cel mai apropiat de un „manager energetic complet" — audit + manager atestat + monitorizare software + conținut SEO de conformare. Este cel mai serios competitor de conținut, chiar dacă țintește industria grea, nu IMM-ul.

**TÜV SÜD România** — [VERIFICAT]
- Se descrie ca **prestator de servicii energetice agreat de Ministerul Energiei / ANRE**, care poate furniza servicii specifice de manager energetic pentru consumatori industriali.
- Activități declarate: elaborarea declarației de consum energetic și a chestionarului, elaborarea programelor de îmbunătățire a eficienței energetice, monitorizarea lunară a consumurilor de resurse energetice, **asistență în selecția furnizorului și negocierea contractelor**.
- Surse: [tuvsud.com — management energetic](https://www.tuvsud.com/ro-ro/industrii/energie/eficienta-energetica/management-energetic), [tuvsud.com — operatori industriali și localități](https://www.tuvsud.com/ro-ro/industrii/energie/management-energetic-pentru-operatori-industriali-si-localitati)
- **Preț afișat: niciunul.**
- **Observație importantă:** TÜV SÜD este singurul jucător din categoria tehnică găsit care menționează explicit **asistență în selecția furnizorului și negociere de contract** în același pachet cu managementul energetic. Adică se apropie de teritoriul Reduco — dar dinspre conformare industrială, nu dinspre factură.

**Adrem Link** — [VERIFICAT, parțial]
- Vinde explicit **„Servicii manager energetic"** externalizat: organizarea și gestionarea proceselor energetice, validarea și gestionarea fluxurilor de documente pentru raportarea la ANRE, asistență la declarația anuală de consum și la chestionarul de analiză, elaborarea programelor de îmbunătățire a eficienței energetice.
- Sursă: [adremlink.ro/en/servicii-manager-energetic](https://adremlink.ro/en/servicii-manager-energetic/) (pagină blocată la fetch direct; conținut redat de motorul de căutare)
- Grupul Adrem are și o linie separată de eficiență energetică cu pagină dedicată **HoReCa**: [eficientaenergetica.adrem.ro/solutii-de-eficientizare-energetica-pentru-horeca](https://eficientaenergetica.adrem.ro/solutii-de-eficientizare-energetica-pentru-horeca/) — [VERIFICAT că pagina există și țintește HoReCa; conținutul exact NEVERIFICAT]
- **Preț afișat: [NEVERIFICAT].**
- **Acesta este competitorul cel mai apropiat funcțional de „manager energetic externalizat" și singurul care atinge și verticala HoReCa.** Merită monitorizat prioritar.

**Alți jucători din categoria tehnică, identificați dar neaprofundați** [VERIFICAT doar la nivel de existență și descriere generală]:
- Enegav / [consultanta-energie.ro](https://consultanta-energie.ro/servicii/management-energetic-pentru-industrie/) — „management energetic pentru industrie"
- [energymanagementaudit.ro](https://energymanagementaudit.ro/en/) — „Audit Energetic București | Consultanță și Management Energetic"
- [Infowatt](https://new.infowatt.ro/managementul-energetic/) — „managementul energetic"
- [ING.GREEN](https://www.ing-green.ro/en/home/) — consultanță energii verzi pentru IMM și administrație publică
- [Konsulting](https://konsulting.ro/) — eficiență energetică, declarat dedicat instituțiilor publice
- [Romanian Garden](https://romanian-garden.com/services/energy-consulting) — audit, optimizare, certificare energetică
- [Ensev](https://ensev.ro/servicii/servicii-de-consultanta-in-eficienta-energetica), [CIGA Energy](http://cigaenergy.ro/consultanta/), [Energo Saving](https://www.energosaving.com/), [QMB Energ](https://qmbenerg.com/consultanta-energetica/), [Alsen](https://www.alsen.ro/)
- ESCO-uri: [Elsaco ESCO](http://www.elsaco-esco.ro/servicii.html), [4envigo](https://4envigo.com/servicii-esco/), [CO-GENERGYA](https://co-genergya.ro/esco/), [Esco City](https://escocity.ro/esco-city/?lang=en); asociația de ramură [ESCOROM](https://escorom.com/)
- [Schneider Electric România — Efficiency Consulting](https://www.se.com/ro/ro/work/services/se-advisory-services/efficiency-consulting/) — consultanță de decarbonizare pentru corporate

**Niciunul dintre cei de mai sus nu afișează un preț de abonament. [VERIFICAT prin absență pe toate paginile parcurse.]**

### 1.4 Cadrul ESCO — de ce nu este concurentul vostru

Ministerul Energiei a publicat în februarie 2024 modele de contract-cadru de performanță energetică (Ordinul nr. 173/19.02.2024), în baza HG nr. 1329/2023, ca reformă asumată prin PNRR. Elementul definitoriu al contractului ESCO este **garantarea economiei de energie, cu rambursarea integrală a costului proiectului din economiile realizate**. [VERIFICAT — [energie.gov.ro/category/esco](https://energie.gov.ro/category/esco/), [arenaconstruct.ro](https://arenaconstruct.ro/activitatea-societatilor-de-servicii-energetice-tip-esco-reglementata/), [escorom.com](https://escorom.com/)]

[INFERENȚĂ] Modelul ESCO presupune **investiție de capital în echipamente** (iluminat, cogenerare, automatizări, fotovoltaic) recuperată în ani. Este structural incompatibil cu un IMM cu 4 puncte de consum închiriate. Reduco nu concurează cu ESCO-urile; **ele sunt canal de parteneriat**, nu concurență — un ESCO nu se deplasează pentru un client de 30 MWh/an, dar poate primi de la Reduco lead-uri industriale calificate și poate trimite înapoi clienți prea mici pentru el.

### 1.5 Categoria B — Brokerii și negociatorii plătiți din economie

Aceștia **nu** folosesc termenul „management energetic". Se numesc „consultanță în energie" și vând un singur lucru: preț mai bun la furnizare.

**Energy Consulting ([energyconsulting.ro](https://energyconsulting.ro/))** — [VERIFICAT]
- Peste 12 ani de experiență pe piața de energie.
- Promisiune: reducerea costurilor la energie electrică și gaze, cu **economii medii de peste 10% din factura lunară**, prin negociere profesională și selecția celor mai avantajoase oferte.
- **Model de plată declarat public: comision de succes, perceput exclusiv din economia demonstrată** („comision doar din economie — model win-win, fără risc").
- Sursă: [energyconsulting.ro](https://energyconsulting.ro/)

**Consultant Energie ([consultantenergie.ro](https://consultantenergie.ro/))** — [VERIFICAT parțial]
- Poziționare: „Completează formularul și redu-ți facturile".
- Afirmă că a ajutat **peste 10.000 de clienți** să reducă costurile energetice. [VERIFICAT ca afirmație publicată; nu ca fapt]
- Operatorul ar fi Blue Star Trading SRL. [NEVERIFICAT — apare într-o redare de motor de căutare, nu am putut confirma pe site]

**Brokeraj propriu-zis** — [VERIFICAT]
- Există o piață de intermediere reglementată de facto post-liberalizare, inclusiv brokeraj prin **Bursa Română de Mărfuri** pentru achiziția de energie și gaze, cu licitații publice. [Exemplu de contract public: [licitatia.ro](https://www.licitatia.ro/servicii-de-brokeraj-pentru-achizitia-de-energie-electrica-si-gaze-naturale-prin-ctr----------------8569726-restricted.html)]
- Există și jucători care se numesc explicit broker, ex. ALL ENERGY BROKER SRL ([LinkedIn](https://www.linkedin.com/company/all-energy-broker-srl)). [VERIFICAT doar existența entității]

### 1.6 Categoria C — Furnizorii care vând „servicii de management"

Furnizorii mari oferă instrumente de monitorizare, dar **legate de propriul contract de furnizare**:
- **ENGIE** — „Soluții monitorizare fluxuri energetice" pentru business, cu prognoză și analiză de consum per consumator. [VERIFICAT — [engie.ro/business/solutii-monitorizare](https://www.engie.ro/business/solutii-monitorizare/)]
- **PPC Energy** — cont/aplicație myPPC pentru contracte, facturi, prețuri, istoric de consum. [VERIFICAT — [ppcenergy.ro/business](https://www.ppcenergy.ro/business/energie-electrica/)]

[INFERENȚĂ] Acesta este cel mai important lucru de înțeles din secțiunea 1: **pentru IMM-ul mediu din România, „managerul energetic" de facto este chiar furnizorul de energie** — cel care are conflictul de interese maxim. Nu un consultant. Nu un comparator. Furnizorul. Iar furnizorul nu va spune niciodată clientului că plătește prea mult, că are putere contractată supradimensionată sau că e facturat pe nivel greșit de tensiune.

### 1.7 Ce am găsit despre prețuri în categoria „management energetic"

| Ce | Preț public găsit | Sursă |
| --- | --- | --- |
| Abonament lunar de management energetic pentru IMM | **NIMIC. Zero rezultate.** Niciun competitor din România nu afișează un preț recurent pentru management energetic B2B. | căutări repetate, toate negative |
| Monitorizare energetică software, abonament lunar | Există ca produs (BlueMonitor — abonament lunar de monitorizare consumuri în cloud), dar valoarea abonamentului nu apare în rezultat | [scada-shop.ro](https://www.scada-shop.ro/cumpara/bluemonitor-abonament-lunar-monitorizare-consumuri-energetice-in-cloud-7368841) |
| Consultanță de negociere furnizor | Comision de succes din economie (procent nespecificat public la Energy Consulting) | [energyconsulting.ro](https://energyconsulting.ro/) |

**Aceasta este cea mai exploatabilă descoperire comercială a raportului: piața nu are ancoră de preț pentru abonamentul de management energetic. Cine publică primul o grilă clară, o definește.**

---

## 2. Comparatoarele de energie din România

### 2.1 Peisajul

Comparatoare private identificate [VERIFICAT ca existență și poziționare declarată]:

| Site | Poziționare declarată |
| --- | --- |
| [comparatorenergie.ro](https://comparatorenergie.ro/) | „Compară rapid ofertele la energie și gaze naturale"; interfață modernă, algoritmi de calcul, prețuri actualizate |
| [economielaenergie.ro](https://economielaenergie.ro/) | „Comparator Tarife Energie Electrica & Gaze [GRATUIT]"; promite economii de până la 2.300 lei/an |
| [tarifmic.ro](https://www.tarifmic.ro/) | „Comparator Energie Electrica 2026 | Pret kWh si Oferte"; sortare după cost lunar + calculator gaze |
| [economisi.ro](https://economisi.ro/comparator) | comparator + zonă de conținut editorial pe prețuri și componente de factură |
| [comparatot.ro](https://www.comparatot.ro/) | comparator multi-categorie: energie, gaze, telecom, echipamente |
| [energie-comparator.ro](https://energie-comparator.ro/) | oferte orientative pe județe |
| pretcurent.ro, solutiiverzi.ro | menționate ca platforme de comparare cod poștal + consum |

**Observație de brand, importantă intern:** `comparatot.ro` este un comparator activ, funcțional, sub exact numele vechi de brand pe care `/cine-suntem/` îl mai poartă în text din 2022 (per `00-brief-context.md`). [VERIFICAT că site-ul comparatot.ro există și funcționează ca comparator]. Orice vizitator care caută „Comparatot" ajunge la un comparator generalist de utilități — asociere de brand exact opusă repoziționării dorite. **De curățat urgent.**

### 2.2 Comparatorul oficial, gratuit, al statului — factorul care ucide categoria

ANRE operează **POSF.ro**, platforma online națională de schimbare a furnizorului, cu comparator oficial integrat. Caracteristici confirmate: instrument **gratuit, oficial, actualizat**; clientul compară ofertele, semnează electronic și **schimbarea furnizorului se finalizează în maximum 24 de ore, fără costuri și fără birocrație**. ANRE a lansat inclusiv un asistent virtual („EVA") pentru utilizarea platformei.
[VERIFICAT — [anre.ro — lansare EVA/POSF](https://anre.ro/anre-lanseaza-asistentul-virtual-eva-pentru-utilizarea-platformei-online-de-schimbare-a-furnizorului-de-energie-electrica-si-gaze-naturale-la-nivel-national-posf/), [posf.ro/comparator](https://posf.ro/comparator?comparatorType=electric), [arhiva.anre.ro](https://arhiva.anre.ro/ro/info-consumatori/comparator-de-tarife)]

În plus, art. 62 alin. (5) din Legea 123/2012 stabilește dreptul clienților casnici, al întreprinderilor mici și al microîntreprinderilor de a schimba furnizorul **fără niciun comision de schimbare**. [VERIFICAT — [Legea 123/2012, text publicat](https://www.engie.ro/wp-content/uploads/2024/04/Legea-nr.-123.2012-energiei-electrice-si-a-gazelor-naturale.pdf)]

[INFERENȚĂ — cu grad ridicat de încredere] **Statul a comoditizat comparația.** Un comparator privat nu mai poate concura pe „îți arăt prețurile" cu un instrument oficial, gratuit, cu semnătură electronică și schimbare în 24 h. Rămân doar UX-ul și marketingul. Aceasta este condamnarea structurală a poziției actuale a Reduco și cel mai puternic argument intern pentru repoziționare: **nu plecați dintr-o poziție bună, plecați dintr-o poziție care se erodează indiferent ce faceți.**

### 2.3 Cum sunt remunerate comparatoarele — răspunsul direct la întrebare

**Aceasta este cea mai valoroasă descoperire pentru mesajul de independență al Reduco.**

**economielaenergie.ro își declară public modelul de venit** [VERIFICAT — [economielaenergie.ro/despre](https://economielaenergie.ro/despre/)]:
- este un comparator comercial care **obține venituri din vânzarea de prospecți/potențiali clienți către furnizorii de energie electrică și gaze naturale**;
- colectează contactele consumatorilor cu acordul acestora și **le livrează furnizorilor în timp real**;
- **încasează o taxă fixă plătită de furnizorul de energie pentru fiecare potențial client** care se arată interesat să fie contactat despre ofertele afișate în comparator;
- se descrie ca **„canal de marketing indirect" pentru industria de energie și gaze**.

Traducere în limbaj de vânzare: **comparatorul nu este plătit de tine. Este plătit ca să te dea mai departe.** Iar aceasta nu este o acuzație — este autodescrierea publică a unui comparator din piață.

**Practica de comision de la furnizor este documentată și la nivel de brokeraj** [VERIFICAT]:
- Este practică obișnuită ca furnizorii de energie să plătească brokerilor un comision pentru fiecare contract încheiat în numele clienților lor; în multe cazuri, clientul final **nu este informat** despre aceste comisioane, dar le amortizează plătind tarife mai mari la energie. [[energylitigation.com/ro/intrebari-frecvente](https://energylitigation.com/ro/intrebari-frecvente/)]
- Codul fiscal definește comisionul ca orice plată în bani sau în natură făcută unui broker sau agent comisionar general pentru servicii de intermediere într-o operațiune comercială.

**Există deja un litigiu de masă construit exact pe acest conflict de interese** [VERIFICAT]:
- **Harcus Parker**, firmă de litigii din Londra specializată în acțiuni colective, operează [energylitigation.com](https://energylitigation.com/), **inclusiv cu pagini în limba română** ([energylitigation.com/ro](https://energylitigation.com/ro/)).
- Teza campaniei: comisioanele ascunse plătite brokerilor sunt, în majoritatea cazurilor, **mită ilegală**, iar clienții au dreptul la restituirea ei plus dobânzi și daune. Ținta acțiunii sunt furnizorii, pentru că au resurse mai mari decât brokerii. Comisioanele erau de regulă calculate pe consum, deci **organizațiile cu consum mare au fost cele mai afectate**.
- Model de plată: **damages-based agreement — fără câștig, fără plată**, fără costuri inițiale la înscriere.

[INFERENȚĂ] Faptul că o firmă britanică de litigii investește în conținut **în limba română** pe tema comisioanelor ascunse din energie arată că problema este percepută ca relevantă și pe piața românească. Reduco poate revendica public argumentul independenței **fără să inventeze nimic** — poate cita autodescrierea unui comparator românesc (economielaenergie.ro) și cadrul de litigiu deja existent.

### 2.4 Limitele structurale ale comparatoarelor — de ce Reduco NU este asta

Sintetizat, verificabil, utilizabil direct în copy:

1. **Compară doar componenta de furnizare.** Comparatoarele afișează prețul ofertei comerciale, nu prețul unitar real plătit (total factură fără TVA / kWh facturat) — vezi metodologia internă Reduco în `00-brief-context.md`. Nu văd distribuția, nu văd energia reactivă, nu văd puterea contractată, nu văd depășirile.
2. **Nu văd factura.** Nu detectează erori de facturare, tarif de distribuție necorespunzător nivelului de tensiune, facturare pe estimare, componente facturate greșit.
3. **Sunt tranzacționale, nu recurente.** Le folosești o dată pe an, la reînnoire.
4. **Nu contestă nimic.** Un comparator nu depune plângere la ANRE, nu invocă art. 24 alin. (3) din Ordinul ANRE 5/2023, nu recuperează compensații.
5. **Sunt remunerate de partea opusă a mesei** (verificat la economielaenergie.ro; practică documentată la brokeraj).
6. **Sunt înlocuite de stat.** POSF.ro face gratuit și oficial exact ceea ce fac ele.

---

## 3. Consultanța juridică pe energie — cine reprezintă clienții în fața ANRE

### 3.1 Cadrul procedural care creează cererea

Există un traseu de plângere formalizat, obligatoriu pentru furnizori:
- **Ordinul ANRE nr. 16/2015** stabilește procedura-cadru privind obligația furnizorilor de energie electrică și gaze de a soluționa plângerile clienților finali — cu formular de înregistrare a plângerii, comunicarea numărului de înregistrare cel târziu în ziua lucrătoare următoare, și obligația furnizorului de a publica pe site rapoarte despre activitatea de soluționare a plângerilor. [VERIFICAT — [Ordinul ANRE nr. 16/2015, text publicat](https://www.engie.ro/wp-content/uploads/2020/07/Ordinul-ANRE-nr-16-2015.pdf)]
- Dacă furnizorul nu răspunde sau răspunsul nu satisface, clientul se poate adresa **ANRE** și **ANPC**; ANRE are formular online de depunere petiție. [VERIFICAT — [spv.anre.ro/depune-petitie](https://spv.anre.ro/depune-petitie/), [arhiva.anre.ro — soluționarea plângerilor](https://arhiva.anre.ro/ro/info-consumatori/faq/gaze-naturale1386850583/solutionarea-plangerilor1565255212)]
- La contestarea valorii facturii, furnizorul e obligat să analizeze temeinicia și, dacă plângerea e întemeiată, **să storneze factura și să restituie sumele cu penalități egale cu cele pe care le-ar fi perceput el de la client**. [VERIFICAT — [arhiva.anre.ro — contracte și facturare](https://arhiva.anre.ro/ro/info-consumatori/faq/energie-electrica1386850595/contracte-si-facturare), Regulamentul de furnizare, [Ordinul ANRE 5/2023](https://www.engie.ro/wp-content/uploads/2023/02/Ordinul-ANRE-nr.-5.2023-Regulamentul-de-furnizare-a-energiei-electrice-la-clien%C5%A3ii-finali-%C8%99i-modificaea-unor-ordine-ANRE-actualizat-07.02.2023.pdf)]
- Regula de 3 luni la facturarea retroactivă pe consum măsurat este confirmată public. [VERIFICAT — surse ANRE de mai sus, coroborat cu `00-brief-context.md`]

### 3.2 Cine ocupă spațiul astăzi

**Trei tipologii distincte, niciuna suprapusă peste Reduco:**

**(a) Case de avocatură corporate, energie ca practică de industrie** [VERIFICAT ca existență și arie de practică]
- [Pavel, Mărgărit și Asociații](https://avocatpavel.ro/service/energie-si-resurse-naturale/) — consultanță pe cerințe de reglementare în energie, inclusiv reglementarea prețurilor de către ANRE și strategii operaționale
- [HPLegal](https://hplegal.ro/ro/energy-and-renewables/) — energie și regenerabile
- [Rolegal](https://rolegal.com/ro/avocati-energie-verde/) — energie verde
- Zamfirescu Racoți Vasile & Partners — a reprezentat clienți în litigii semnificative de reziliere a contractelor de furnizare [VERIFICAT indirect prin presă: [economica.net](https://www.economica.net/decizie-uriasa-a-justitiei-intr-un-proces-dintre-un-furnizor-de-energie-si-un-client-impact-pentru-toti-clientii-din-romania_968081.html), [e-nergia.ro](https://e-nergia.ro/decizie-importanta-a-justitiei-intr-un-proces-dintre-un-furnizor-de-energie-si-un-client-precedent)]
- **Model: proiect / onorariu de avocat. Prețuri: neafișate. [VERIFICAT prin absență]**
- **Țintă: dezvoltatori, producători, traderi, corporate — NU IMM-ul cu factură umflată.**

**(b) Avocați de contestare a facturii, orientați spre consumator** [VERIFICAT]
- **Cuculis și Asociații** — pagini dedicate: „Factura la curent — cum o contest", „Contestare factură PPC Energie SA", contestații la executare pe facturi de utilități devenite titlu executoriu. Avocatul Adrian Cuculis a anunțat public intenția unui **proces colectiv** împotriva facturilor de regularizare la energie. [[indrumari-juridice.eu](https://indrumari-juridice.eu/indrumarijuridice/factura-la-curent-cum-o-contest/), [evz.ro](https://evz.ro/procedura-de-contestare-a-facturilor-la-energie-recomandarile-avocatului-adrian-cuculis.html), [ziare.com](https://ziare.com/factura-energie-electrica/factura-energie-avocat-adrian-cuculis-proces-colectiv-1761842)]
- **avocat-alexandrov.ro** — dosar câștigat pe acuzații de intervenții neautorizate la energie; oferă reprezentare în litigii cu furnizori și distribuitori. [[avocat-alexandrov.ro](https://avocat-alexandrov.ro/interventii-neautorizate-energie/)]
- [Cabinet Strinu](https://strinu.ro/contestarea-facturii/) — contestarea facturii
- **Model: caz cu caz, reactiv, declanșat de o criză. Prețuri: neafișate.**
- **Registru: predominant casnic / consumator, nu B2B multi-locație.**

**(c) Hibridul juridico-energetic — singurul competitor structural direct identificat**

**EnergoLex Consulting** — [VERIFICAT parțial; pagină blocată la fetch direct, conținut redat de motorul de căutare]
- Se autodescrie ca **„Consilier juridico-energetic ANRE"**.
- Arii declarate: racordare la rețea, contestații de facturi de energie, servicii pentru prosumatori, **reprezentare în litigii cu operatorii de distribuție**, îndrumare pe legislația energetică cu „rezultate dovedite în recuperări și soluționări de dispute".
- Contact public: 0730 353 847 | energolexconsulting@gmail.com
- Sursă: [energolexconsulting.com/despre-mine](https://energolexconsulting.com/despre-mine)
- **Preț afișat: [NEVERIFICAT] — nu apare în rezultate. Model de plată: [NEVERIFICAT].**

[INFERENȚĂ] EnergoLex acoperă **aproape exact aceeași combinație de servicii ca Reduco** — racordare + contestații facturi + prosumatori + reprezentare în fața distribuitorilor. Diferența probabilă: URL-ul paginii („despre-**mine**") și adresa de contact Gmail sugerează un **practician individual**, fără platformă, fără abonament, fără produs standardizat. [Inferență din indicii, nu verificată.] **Este validarea că nișa există și că cineva o testează deja — dar nu la scară de produs.** De monitorizat activ.

### 3.3 Răspunsul la întrebare: vândut separat sau împachetat?

**Vândut separat, aproape fără excepție.** [VERIFICAT prin structura ofertelor parcurse]

- Casele de avocatură vând juridic pur. Nu ating factura tehnic.
- Firmele de consultanță energetică (Servelect, SENYS, TÜV SÜD, Adrem) vând tehnic pur. Nu am găsit **niciuna** care să declare reprezentare juridică în fața ANRE ca parte din serviciu. [VERIFICAT prin absență în toate paginile de serviciu parcurse]
- Comparatoarele nu vând nici tehnic, nici juridic.
- Singura excepție parțială identificată: EnergoLex.

**Concluzie operațională: împachetarea „tehnic + juridic + recurent" este, pe baza a ceea ce am putut verifica, neocupată la nivel de produs în România.**

---

## 4. Piața de conformare Legea 121/2014

### 4.1 CORECȚIE FACTUALĂ IMPORTANTĂ pentru brief-ul intern

`00-brief-context.md`, secțiunea 2.7 și grila de prețuri, definește segmentul Industrial ca **„peste 500 MWh/an sau Legea 121/2014"**.

**Pragul legal real este de 1.000 tep/an.** [VERIFICAT — art. 9 alin. (1) din Legea 121/2014: [textul legii pe energie.gov.ro](https://energie.gov.ro/old/wp-content/uploads/2021/05/Lege-121-2014-actualizata-in-30-aprilie-2021.pdf), [lege5.ro — art. 9](https://lege5.ro/Gratuit/gqydcobtga/art-9-programe-de-masuri-lege-121-2014?dp=gy4demrxgi3tk), [textul publicat de ENGIE](https://www.engie.ro/wp-content/uploads/2019/02/Legea-nr.-121.2014-actualizata-14.2.19.pdf)]

La factorul standard de conversie (1 tep ≈ 11,63 MWh), **1.000 tep ≈ 11.630 MWh/an**. Adică pragul real este de aproximativ **23 de ori mai mare** decât cel din brief. Un consumator de 500 MWh/an **nu** intră sub obligațiile art. 9.

**Consecință directă asupra deciziei de poziționare:** dacă pachetul „Industrial — de la 1.500 lei/lună, peste 500 MWh/an sau Legea 121/2014" ajunge public în forma actuală, promite conformare unor clienți care nu au obligația și ratează, ca dimensionare, clienții care chiar o au. **De corectat înainte de publicare.** Un client de 500 MWh/an este un client bun de Multi-Locație, nu de Industrial.

[NEVERIFICAT] Există în lege și un prag inferior (des citat în piață ca 200 tep/an) pentru obligații de raportare mai ușoare. Nu am putut confirma textul exact al alineatului în această sesiune. **De verificat direct în lege înainte de a-l folosi comercial.**

### 4.2 Obligațiile confirmate la peste 1.000 tep/an [VERIFICAT]

Operatorii economici cu consum anual peste 1.000 tep au obligația să:
- **a)** realizeze **audit energetic o dată la 4 ani**, pe întregul profil de consum, elaborat de persoană fizică sau juridică autorizată de Ministerul Energiei / ANRE, ca bază pentru măsurile de eficiență;
- **b)** elaboreze **programe de îmbunătățire a eficienței energetice** cu măsuri pe termen scurt, mediu și lung;
- **c)** **numească un manager energetic atestat** de Departamentul pentru Eficiență Energetică **sau să încheie un contract de management energetic** cu o persoană fizică atestată ori cu o societate prestatoare de servicii energetice agreată;
- **d)** transmită Direcției Eficiență Energetică din Ministerul Energiei, **până la 30 iunie** al fiecărui an, **declarația de consum total anual de energie** și **chestionarul de analiză a consumatorului de energie**.

**Regulă foarte relevantă pentru clientul multi-locație:** pentru operatorii economici cu **subunități** (sucursale, puncte de lucru, alte sedii secundare) situate în puncte geografice diferite și **nelegate direct funcțional sau prin rețele energetice**, fiecare subunitate din locație geografică diferită **se consideră separat** din perspectiva obligațiilor. [VERIFICAT — art. 9, surse de mai sus]

[INFERENȚĂ] Această regulă este un cârlig comercial excelent și complet neexploatat în comunicarea de piață găsită: pentru un lanț cu 30 de locații, întrebarea „intru sau nu sub obligație?" nu se pune pe total firmă, ci **per locație** — exact structura de facturare pe punct de consum pe care Reduco vrea s-o adopte. Argumentul comercial și argumentul legal se aliniază.

### 4.3 SCHIMBAREA MAJORĂ: reforma din 2026

**Aceasta este cea mai importantă descoperire de timing din tot raportul.**

Noua versiune a Legii 121/2014, care transpune **Directiva UE 2023/1791 (EED recast)**, **intră în vigoare în 2026** și **extinde obligațiile de eficiență energetică de la marii consumatori către companiile mijlocii și mici**. [VERIFICAT — [business24.ro](https://business24.ro/eficienta-energetica/reforma-legii-eficienta-energetica-firme-mici-mijlocii-directiva-1651577), coroborat cu [servelect.ro — Noua Directivă UE și Legea 121](https://servelect.ro/noua-directiva-ue-legea-eficientei-energetice-121/)]

Elemente confirmate:
- Se introduc **audit energetic o dată la 4 ani, raportarea consumului și implementarea de măsuri de eficiență** pentru firme mult mai mici decât până acum.
- Categorii de entități numite explicit ca fiind atrase în perimetrul obligației: **platforme industriale mici cu ~50 de angajați, hoteluri de dimensiune medie, spitale medii, firme de transport cu flote modeste.**
- Directiva propune **două praguri noi**, exprimate în terajouli: societățile cu consum de peste **85 TJ (peste ~2.030 tep/an)** trebuie să implementeze un **sistem de management energetic certificat până la 11 octombrie 2027**.
- [NEVERIFICAT în această sesiune] Al doilea prag din EED recast, cel care declanșează obligația de audit energetic, este citat uzual la 10 TJ. **Nu am putut confirma valoarea și transpunerea ei exactă în textul românesc. De verificat obligatoriu înainte de a construi campanie pe el.**

**Ce înseamnă asta pentru Reduco** [INFERENȚĂ, dar cu bază solidă]:
1. Segmentul-țintă declarat — **hoteluri medii, platforme mici, clinici, transport** — este exact lista de exemple din analiza reformei. Nu este o coincidență favorabilă; este piața primară a Reduco care devine, prin lege, obligată să facă ceea ce Reduco vinde.
2. Se creează, în 2026–2027, un **val de cerere de conformare într-un segment pe care jucătorii industriali (Servelect, SENYS, TÜV SÜD) nu îl deservesc rentabil** — sunt calibrați pe Kronospan și OMV, nu pe un hotel de 60 de camere.
3. Fereastra de ocupare a termenului „conformare energetică pentru IMM" este **acum**, înainte ca acei jucători să coboare în piață sau ca o serie de firme noi să apară.

### 4.4 Prețurile de conformare — ce este public

| Serviciu | Preț public | Sursă | Încredere |
| --- | --- | --- | --- |
| **Audit energetic obligatoriu conform Legii 121/2014**, repetat la 4 ani | **8.000 – 25.000 lei + TVA** | [senys.ro — ghid conformare 2026](https://senys.ro/obligatiile-companiilor-privind-eficienta-energetica-in-2026-ghid-complet-pentru-conformare-cu-legea-121-2014/) | [VERIFICAT] |
| **Consultanță ISO 50001** (alternativă care exceptează de la auditul obligatoriu), 4–8 luni | **12.000 – 50.000 lei + TVA**, în funcție de consumul anual | [isopedia.ro](https://isopedia.ro/ghid/consultanta-iso-50001-eficienta-energetica/) | [VERIFICAT] |
| Audit energetic de clădire (RAE, altă categorie — MDLPA, nu ANRE) | de la 1.500 lei; București-Ilfov: 1.500–4.000 lei case, 3.500–7.000 lei blocuri, **4.000–25.000 lei clădiri comerciale și publice** | [cpeproiect.ro](https://www.cpeproiect.ro/audit-energetic-bucuresti/) | [VERIFICAT] |
| Certificat energetic (clădiri) | 250–800 lei apartamente, 400–1.200 lei case | [energieacasa.ro](https://energieacasa.ro/ghid/certificat-energetic-pret-2026) | [VERIFICAT] |

**Atenție la o confuzie de piață pe care o puteți exploata:** există **două „audituri energetice" complet diferite**, cu autorități, atestate și prețuri diferite — auditul de clădire (auditori atestați MDLPA, ~850 cu drept de practică valabil în 2026, sursă [energieacasa.ro](https://energieacasa.ro/ghid/certificat-energetic-pret-2026)) și auditul energetic industrial pentru Legea 121/2014 (auditori autorizați Ministerul Energiei / ANRE). Clienții le confundă sistematic. [INFERENȚĂ din suprapunerea rezultatelor de căutare pentru aceeași expresie.] Un articol care lămurește diferența este conținut de captare cu concurență scăzută.

### 4.5 Cum se poziționează Reduco față de prețurile de conformare

Prețul intern propus pentru **dosarul de conformare Legea 121/2014: 2.500–6.000 lei** (`00-brief-context.md`).

[INFERENȚĂ] Acesta **nu concurează** cu auditul de 8.000–25.000 lei — și e bine că nu concurează. Reduco nu vinde auditul; vinde **coordonarea conformării**: declarația anuală, chestionarul, programul de măsuri, legătura cu managerul energetic atestat, respectarea termenului de 30 iunie. Este poziționare de **project manager de conformare**, nu de auditor. Mesajul corect nu este „mai ieftin decât auditul", ci **„auditul este o dată la 4 ani; obligația este în fiecare an, până la 30 iunie"**.

---

## 5. Limbajul real al pieței

### 5.1 Avertisment metodologic, explicit

**Nu am date de volum de căutare.** Nu am avut acces la Keyword Planner, Ahrefs, Semrush sau echivalent. Orice cifră de volum pe care aș produce-o ar fi inventată, deci nu produc niciuna.

Ce pot livra: o **hartă a ocupării termenilor** construită din compoziția reală a rezultatelor de căutare pentru fiecare expresie — cine apare, ce tip de pagină apare, cât de comercială este intenția. Este un indicator solid de **dificultate competitivă**, nu de volum.

### 5.2 Harta termenilor

| Termen | Cine ocupă rezultatele | Tip de pagini dominante | Dificultate estimată | Potrivire cu Reduco |
| --- | --- | --- | --- | --- |
| **„audit energetic"** | Auditori de clădiri (MDLPA), platforme de certificat energetic, + SENYS pe partea industrială | Pagini de serviciu foarte comerciale, cu prețuri afișate | **Cea mai mare.** Piață matură, cu preț, cu volum evident | Slabă. Nu sunteți auditor. Termen ambiguu, atrage trafic de clădiri |
| **„consultanță energetică" / „consultanță în energie"** | Foarte aglomerat: Schneider, TÜV SÜD, Servelect, Romanian Garden, Konsulting, Ensev, CIGA, Energo Saving, QMB, energyconsulting.ro | Pagini corporate generice, fără preț | **Mare, dar difuză.** Mulți jucători, mesaj nediferențiat | Medie. Termenul e devalorizat prin suprautilizare |
| **„management energetic" / „manager energetic"** | Cadru ANRE + jucători industriali grei (Servelect, SENYS, TÜV SÜD, Adrem, Infowatt) | Pagini tehnice de conformare industrială | **Medie.** Puțini jucători, dar autoritari | **Bună — cu o condiție.** Termenul e ocupat *pentru industrie*, nu pentru IMM |
| **„optimizare costuri energie"** | Mix confuz: consultanți, ESCO, furnizori, fotovoltaice | Articole de blog, landing-uri de generare de lead-uri | **Medie-mică**, dar intenție neclară | Medie. Prea vag pentru a susține un abonament |
| **„comparator energie" / „compară oferte energie"** | Comparatoare private + **POSF.ro (ANRE)** | Instrumente gratuite | **Mare și în deteriorare** — statul concurează gratuit | **De abandonat ca poziționare.** Păstrat cel mult ca unealtă de captare |
| **„contestare factură energie"** | Avocați (Cuculis, Strinu, Alexandrov), presă, ghiduri ANPC/ANRE | Pagini juridice reactive, registru casnic | **Mică-medie în registru B2B** | **Foarte bună.** Nimeni nu o tratează B2B |
| **„conformare Legea 121/2014"** | SENYS (dominant), servelect.ro, presă de business, IsoPedia | Ghiduri lungi de conformare | **Mică**, dar **crește rapid din cauza reformei 2026** | **Excelentă, dacă intrați acum** |

### 5.3 Termenii pe care i-am găsit efectiv folosiți de clienți (limbaj natural)

Din formulările care apar în paginile orientate spre client și în presa de consum [VERIFICAT ca formulări publicate]:
- **„factură prea mare la energie"** — [pandabot.ro](https://pandabot.ro/energie-electrica/ghid/factura-prea-mare), [conso.ro](https://www.conso.ro/energie-electrica/factura-la-curent-prea-mare-ce-poti-sa-faci), [stirileprotv.ro](https://stirileprotv.ro/divers/ce-sa-faci-daca-ai-primit-o-factura-prea-mare-la-gaze-sau-energie.html)
- **„cum contest factura"**, **„factura la curent — cum o contest"** — [indrumari-juridice.eu](https://indrumari-juridice.eu/indrumarijuridice/factura-la-curent-cum-o-contest/)
- **„cum îmi recuperez banii"** — [playtech.ro](https://playtech.ro/2025/cum-faci-o-reclamatie-la-anre-daca-furnizorul-de-energie-te-a-taxat-incorect-si-vrei-sa-ti-recuperezi-banii/)
- **„energie reactivă"** / **„penalități energie reactivă"** — termen tehnic pe care clientul îl caută **după** ce îl vede pe factură

[INFERENȚĂ] Clientul **nu caută „management energetic"**. Caută **„de ce e factura asta atât de mare"**. Aceasta este o distincție de arhitectură, nu de copywriting: **„manager energetic" este poziția, nu poarta de intrare.** Poarta de intrare trebuie construită pe limbajul durerii; poziția se comunică după ce omul e înăuntru. Un site care își pune „manager energetic" pe H1 și nimic altceva va fi corect strategic și mort din punct de vedere al traficului.

### 5.4 Răspunsul direct la întrebarea din brief

- **Cel mai mare volum, aproape sigur: „audit energetic".** [INFERENȚĂ pe baza densității comerciale a SERP-ului, a numărului de furnizori și a faptului că este singurul termen din listă la care piața afișează prețuri.] Este și cel mai contestat și cel mai puțin potrivit pentru voi.
- **Cea mai mică concurență, cu relevanță comercială reală: „conformare Legea 121/2014" în registru IMM și „contestare factură energie" în registru B2B.** [INFERENȚĂ pe baza compoziției SERP: primul e dominat de un singur jucător, SENYS; al doilea e dominat exclusiv de avocați care vorbesc consumatorilor casnici.]
- **Termenul cu cel mai bun raport poziție/dificultate: „manager energetic pentru firme / pentru IMM"** — adică termenul existent, **calificat spre segmentul neocupat**.

---

## 6. Spațiul liber de poziționare

### 6.1 Harta pieței pe două axe

Am poziționat toți jucătorii identificați pe două axe: **cine plătește serviciul** (client vs. furnizor) și **ce fel de angajament** (tranzacție punctuală vs. relație continuă).

```
                    PLĂTIT DE FURNIZOR
                            │
   comparatoare private     │
   (economielaenergie,      │
   comparatorenergie,       │   furnizorii înșiși
   tarifmic, comparatot)    │   (ENGIE monitorizare,
   brokeri pe comision      │    PPC myPPC, Adrem)
                            │
 TRANZACȚIE ────────────────┼──────────────── RELAȚIE CONTINUĂ
 PUNCTUALĂ                  │
                            │
   avocați de contestare    │   consultanță industrială
   (Cuculis, Alexandrov,    │   și ESCO
   Strinu)                  │   (Servelect, SENYS,
   case de avocatură        │   TÜV SÜD, Adrem Link)
   (Pavel Mărgărit, HPLegal)│   — dar numai >1.000 tep
   auditori energetici      │
   EnergoLex (hibrid, mic)  │        ◄── ZONA GOALĂ:
                            │            relație continuă
                    PLĂTIT DE CLIENT        + plătit de client
                                            + accesibil IMM
```

**Cadranul din dreapta-jos este ocupat exclusiv de firme calibrate pe industrie grea.** Pentru un IMM cu 1–10 puncte de consum, cadranul este **gol**. [INFERENȚĂ, dar susținută de absența totală, în toate căutările, a vreunui abonament de management energetic cu preț afișat pentru IMM.]

### 6.2 Teritoriul revendicabil

**„Managerul energetic extern al firmelor care nu-și permit unul intern."**

Argumentul de deținere se sprijină pe trei elemente pe care **niciun competitor identificat nu le are simultan**:

| Element | Cine îl mai are | Verificare |
| --- | --- | --- |
| **Independență declarată — zero comision de la furnizori** | Nimeni în energie nu îl comunică explicit ca argument central. Am găsit structura de mesaj folosită în România, dar în alt sector (consultanță AI: [neuroai.ro](https://neuroai.ro/consultanta-ai/) — „nu primim comisioane de la furnizori, onorariile vin exclusiv de la client"). Modelul opus — plătit de furnizor — este autodeclarat de economielaenergie.ro. | [VERIFICAT prin absență la competitorii de energie + [VERIFICAT] pentru modelul opus |
| **Competență juridică reală în fața ANRE, cu dosare** | Avocații (fără competență tehnică pe factură). EnergoLex (hibrid, dar aparent practician individual, fără produs). **Zero firme de consultanță energetică.** | [VERIFICAT prin absență pe toate paginile de serviciu ale consultanților] |
| **Abonament lunar cu preț public** | **Nimeni.** Nu am găsit niciun preț de abonament de management energetic B2B afișat public în România. | [VERIFICAT prin absență, căutări repetate] |

### 6.3 De ce funcționează combinația (și de ce e greu de copiat)

[INFERENȚĂ]
- Un **comparator** nu poate revendica independența — modelul lui de venit o interzice. Ar trebui să-și schimbe business-ul.
- Un **consultant tehnic** nu poate revendica reprezentarea în fața ANRE — nu are competența juridică și nu are dosare.
- Un **avocat** nu poate revendica auditul de factură — nu recalculează prețul unitar real, nu identifică nivelul de tensiune greșit, nu dimensionează compensarea reactivei.
- Un **furnizor** nu poate revendica niciuna dintre cele trei.

Este singura combinație din piață care nu poate fi copiată fără schimbarea modelului de business al copiatorului. Exact ce spune și `00-brief-context.md` — cu diferența că acum e verificată împotriva pieței, nu doar afirmată intern.

### 6.4 Riscuri de poziționare identificate

1. **Termenul „management energetic" atrage așteptare de conformare industrială.** Un client care aude „manager energetic" poate presupune atestat ANRE și obligație legală. Dacă Reduco nu are manager energetic atestat propriu (`00-brief-context.md` menționează „legătura cu managerul energetic atestat", ceea ce sugerează colaborare externă), **acest lucru trebuie declarat explicit**, altfel apare o problemă de credibilitate exact în fața clientului industrial. **Formulare recomandată: „coordonăm conformarea și lucrăm cu manager energetic atestat" — nu „suntem manager energetic atestat", dacă nu sunteți.**
2. **Eroarea de prag din brief (500 MWh vs 1.000 tep)** — dacă ajunge publică, distruge credibilitatea tehnică în fața exact a clientului cel mai valoros. Vezi 4.1.
3. **Comparatot.ro** — brand vechi, comparator activ, asociere greșită. Vezi 2.1.
4. **Termenul de poziționare nu e termen de trafic.** Vezi 5.3. Riscul e să câștigați poziționarea și să pierdeți traficul.

---

## 7. Concluzii pentru poziționare

**1. Renunțați la comparator ca poziționare, nu din strategie, ci din necesitate — statul v-a luat produsul.**
POSF.ro oferă gratuit, oficial, cu semnătură electronică și schimbare în 24 h, exact ceea ce face un comparator privat ([anre.ro](https://anre.ro/anre-lanseaza-asistentul-virtual-eva-pentru-utilizarea-platformei-online-de-schimbare-a-furnizorului-de-energie-electrica-si-gaze-naturale-la-nivel-national-posf/), [posf.ro](https://posf.ro/comparator?comparatorType=electric)). Poziția de comparator nu se erodează pentru că sunteți voi slabi, ci pentru că a fost naționalizată. Comparatorul rămâne unealtă de captare de trafic; încetează să fie identitate. Curățați și asocierea reziduală cu „Comparatot" — [comparatot.ro](https://www.comparatot.ro/) este un comparator generalist activ, iar `/cine-suntem/` încă poartă acel nume.

**2. Faceți din independență o afirmație verificabilă, nu un slogan — și numiți modelul opus.**
Nu spuneți „suntem independenți". Spuneți: *„Nu primim comision de la niciun furnizor. Suntem plătiți exclusiv de client. Comparatoarele gratuite sunt plătite de furnizori pentru fiecare contact pe care îl transmit — unul dintre ele o declară public."* Puteți susține afirmația cu autodescrierea economielaenergie.ro ([economielaenergie.ro/despre](https://economielaenergie.ro/despre/)) și cu practica documentată a comisioanelor ascunse din brokerajul de energie ([energylitigation.com/ro](https://energylitigation.com/ro/intrebari-frecvente/)). **Nu numiți competitori în copy** — descrieți modelul. E la fel de eficient și fără risc juridic.

**3. Competența juridică nu este un serviciu în plus — este dovada că restul e real. Mutați-o pe prima pagină.**
Nicio firmă de consultanță energetică din România identificată nu declară reprezentare în fața ANRE; niciun avocat nu recalculează prețul unitar real din factură. Singurul jucător care combină cele două — EnergoLex ([energolexconsulting.com](https://energolexconsulting.com/despre-mine)) — pare un practician individual, fără produs standardizat. Dosarul de 82.463,75 lei nu este un testimonial; este demonstrația că „managerul energetic" nu e un cuvânt de marketing. Un comparator nu te reprezintă într-un litigiu. Un consultant tehnic nici atât.

**4. Publicați primii o grilă de preț pentru abonamentul de management energetic — piața nu are ancoră.**
Zero competitori afișează un preț recurent. Servelect, SENYS, TÜV SÜD, Adrem — toți cer ofertă. În absența unei ancore, primul care publică o grilă credibilă o definește, iar ceilalți sunt forțați să răspundă la ea. Grila internă propusă (149 / 349 / 89-per-locație / de la 1.500) este exploatabilă exact pentru că nimeni nu are cu ce s-o compare. **Corolar obligatoriu:** eliminați pachetele Business 99/199/399 cu unsprezece beneficii identice — o grilă în care singura diferență e numărul de reprezentări juridice contrazice chiar mesajul de la punctul 3.

**5. Reforma Legii 121/2014 din 2026 vă aduce clientul-țintă prin lege. Poziționați-vă acum, nu în 2027.**
Noua versiune, care transpune Directiva 2023/1791, extinde obligațiile de eficiență energetică de la marii consumatori la **firme mici și mijlocii**, cu exemple explicite: **hoteluri medii, platforme industriale mici cu ~50 de angajați, spitale medii, firme de transport cu flote modeste** ([business24.ro](https://business24.ro/eficienta-energetica/reforma-legii-eficienta-energetica-firme-mici-mijlocii-directiva-1651577), [servelect.ro](https://servelect.ro/noua-directiva-ue-legea-eficientei-energetice-121/)). Aceasta este, aproape literal, lista voastră de clienți-țintă. Jucătorii industriali nu vor coborî rentabil la acest nivel. Fereastra de ocupare a termenului **„conformare energetică pentru IMM"** este deschisă acum și se închide când primul competitor publică un ghid bun.

**6. Corectați pragul de 500 MWh înainte de orice publicare — este o eroare de două ordine de mărime.**
Pragul legal al art. 9 din Legea 121/2014 este de **1.000 tep/an ≈ 11.630 MWh/an**, nu 500 MWh/an ([textul legii](https://energie.gov.ro/old/wp-content/uploads/2021/05/Lege-121-2014-actualizata-in-30-aprilie-2021.pdf), [lege5.ro](https://lege5.ro/Gratuit/gqydcobtga/art-9-programe-de-masuri-lege-121-2014?dp=gy4demrxgi3tk)). Pachetul „Industrial" descris ca „peste 500 MWh/an sau Legea 121/2014" promite conformare unor firme care nu au obligația. În schimb, exploatați regula reală și mult mai valoroasă: **subunitățile din locații geografice diferite, nelegate funcțional, se evaluează separat** — logica legii se suprapune perfect peste decizia voastră de a factura pe punct de consum, nu pe firmă.

**7. Separați poziția de poarta de intrare, altfel câștigați identitatea și pierdeți traficul.**
Clientul nu caută „management energetic" — caută **„factură prea mare la energie"**, **„cum contest factura"**, **„cum îmi recuperez banii"**, **„energie reactivă"** ([pandabot.ro](https://pandabot.ro/energie-electrica/ghid/factura-prea-mare), [indrumari-juridice.eu](https://indrumari-juridice.eu/indrumarijuridice/factura-la-curent-cum-o-contest/), [playtech.ro](https://playtech.ro/2025/cum-faci-o-reclamatie-la-anre-daca-furnizorul-de-energie-te-a-taxat-incorect-si-vrei-sa-ti-recuperezi-banii/)). „Manager energetic" este ce **sunteți**; auditul gratuit de factură pe limbajul durerii, în registru B2B, este cum **intră omul**. Terenul de captare cel mai ieftin identificat: contestarea facturii **pentru firme** — spațiu ocupat astăzi exclusiv de avocați care vorbesc consumatorilor casnici — și lămurirea confuziei dintre auditul energetic de clădire (MDLPA) și auditul industrial Legea 121/2014 (ANRE), pe care piața o perpetuează.

---

## Anexă — ce nu am putut verifica și ar trebui verificat manual

| Nr. | De verificat | Cum |
| --- | --- | --- |
| 1 | **Prețurile afișate de EnergoLex, Adrem Link, Servelect, SENYS, TÜV SÜD** | Deschidere manuală a paginilor (blocate de proxy în această sesiune) |
| 2 | **Numărul de manageri energetici atestați și de societăți prestatoare agreate** | Descărcare din [portal.anre.ro](https://portal.anre.ro/PublicLists/ListeEficienta/PrestatoriServiciiPJEF) — dublă utilitate: hartă a concurenței + listă de potențiali parteneri |
| 3 | **Pragul secundar din Legea 121/2014 (des citat ca 200 tep)** și **al doilea prag EED (10 TJ)** | Citire directă a textului legii actualizate și a proiectului de transpunere |
| 4 | **Data exactă de intrare în vigoare a noii Legi 121 și textul final** | Monitorul Oficial / energie.gov.ro — condiționează calendarul de campanie |
| 5 | **Dacă EnergoLex este practician individual sau firmă cu echipă** | Verificare CUI / termene.ro / listele ANRE |
| 6 | **Structura reală a paginii `/despre` de la comparatoarele concurente** | Fetch manual — pentru a confirma dacă și altele își declară modelul de venit, ceea ce ar întări argumentul de la punctul 2 |
| 7 | **Prețul de 3.000–8.000 lei pentru compensare reactivă globală (20–50 kVAr)** — apare în ghidurile publice pe temă, dar nu am putut confirma sursa exactă | Verificare pe [economisi.ro](https://economisi.ro/energie/solutii-casa/energie-reactiva) și [senys.ro](https://senys.ro/en/compensare-energie-reactiva/) — relevant pentru calibrarea serviciului de 1.200–2.500 lei |
| 8 | **Toate afirmațiile despre reduco.ro** din `00-brief-context.md` | Domeniul a fost blocat integral; nimic din audit nu a putut fi reconfirmat |
