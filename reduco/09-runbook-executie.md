# Reduco — runbook de execuție a mutării de branding

Instrucțiuni pas cu pas. Fiecare pas are: ce faci, unde, cât durează, cum verifici că a mers.
Ordinea contează — pașii de mai jos sunt așezați astfel încât nimic să nu strice ce s-a făcut înainte.

**Regula de aur a întregii operațiuni:** nu schimbi mesajul înainte să repari infrastructura.
Dacă publici copy nou pe un site fără H1-uri, cu brandul vechi în titluri și cu butoane care duc
în coșul de cumpărături, ai cheltuit efort pe un mesaj pe care nimeni nu-l va vedea corect.

---

# FAZA 0 — Înainte să atingi orice (o zi)

Nimic din faza asta nu se vede pe site. Tot ce urmează depinde de ea.

## Pas 0.1 — Backup complet

**Unde:** panoul de hosting + WordPress.

1. Snapshot complet din panoul de hosting (cPanel / Plesk → Backup).
2. În WordPress, instalează **UpdraftPlus** (dacă nu există) și fă un backup manual complet:
   fișiere + bază de date. Descarcă arhiva local, nu o lăsa doar pe server.
3. Notează data și ora backup-ului într-un document.

**Verificare:** ai arhiva descărcată pe calculatorul tău și poți deschide fișierul .zip.

**De ce contează:** pașii 1.1 și 1.3 modifică șabloane și baza de date. Fără backup, o greșeală
înseamnă reconstrucție manuală.

## Pas 0.2 — Site de staging

**Unde:** panoul de hosting (majoritatea au „Staging" cu un click) sau plugin WP Staging.

Creează o copie a site-ului la o adresă de test. **Toate modificările structurale din Faza 1 se
fac întâi acolo.**

**Verificare:** poți deschide staging-ul într-un browser și arată identic cu site-ul live.

**Dacă nu ai staging:** se poate lucra direct pe live, dar atunci pașii se fac
**unul câte unul, cu verificare după fiecare**, niciodată în lot.

## Pas 0.3 — Fotografia de start (baseline)

Fără asta, peste trei luni nu poți demonstra nimic.

**În Google Search Console:**
1. Performance → Search results → interval **ultimele 3 luni** → Export → Google Sheets.
   Salvează ca „GSC baseline [data]".
2. Pages → Export lista completă de pagini indexate.
3. Notează separat: total clicuri/lună, total afișări, CTR mediu, poziție medie.

**În Google Analytics 4:**
1. Reports → Acquisition → Traffic acquisition → ultimele 3 luni → Export.
2. Notează: sesiuni organice/lună, rata de conversie pe formularul de contact,
   număr de trimiteri de formular/lună.

**Verificare:** ai două fișiere exportate, cu dată în denumire, salvate într-un folder
„Baseline repoziționare".

## Pas 0.4 — Inventarul real al site-ului

**Unealta:** Screaming Frog SEO Spider (versiunea gratuită merge până la 500 de URL-uri).

1. Rulează un crawl complet pe `reduco.ro`.
2. Exportă în Excel și creează coloane: **URL / Titlu / Meta description / H1 / Cod de răspuns /
   Decizie**.
3. La coloana Decizie, marchează fiecare pagină cu: **PĂSTREZ / REScriu / REDIRECT / ȘTERG**.
4. Rulează separat filtrul **H1 → Missing**. Notează câte pagini apar. Aceasta e cifra pe care
   o vei compara după Pasul 1.1.

**Verificare:** ai un fișier cu toate URL-urile și o decizie lângă fiecare.

**Notă importantă:** acesta este momentul în care confirmi sau infirmi lista celor ~14 pagini cu
prețuri din 2022. Nu te baza pe memorie sau pe documentul intern — crawl-ul e sursa adevărului.

## Pas 0.5 — Decizia care blochează tot restul

**Cine decide:** tu, nu un executant.

Răspunde în scris, într-un document, la întrebarea: **câștigă Reduco bani din vânzarea
centralelor termice, panourilor fotovoltaice și a iluminatului LED?**

- **DA** → afirmația de independență se reformulează strict: *„nu primim comision de la niciun
  furnizor **de energie**"*, iar modelul de venit din echipamente se declară separat și vizibil.
- **NU, e doar intermediere fără marjă** → se spune explicit pe site, altfel arată identic cu DA.
- **E linie reziduală de la modelul vechi** → intră în lista de ȘTERG la Pasul 0.4.

**Nu treci la Faza 3 fără acest răspuns.** Tot copy-ul despre independență depinde de el.

---

# FAZA 1 — Reparații invizibile (săptămâna 1)

Nimic din faza asta nu schimbă mesajul. Sunt reparații de infrastructură. Se pot face în orice
ordine, dar 1.1 primul, pentru că are cel mai mare efect.

## Pas 1.1 — Repară H1 pe tot site-ul

**Cel mai bun raport efort/impact din tot proiectul.** O setare, toate paginile.

**Unde:** WordPress → Templates → Theme Builder (sau Elementor → Theme Builder).

1. Deschide fiecare șablon din listă: **Single Post**, **Single Page**, **Archive**, și orice
   șablon personalizat.
2. În fiecare, găsește widgetul **Post Title** (sau **Heading** folosit ca titlu principal).
3. Selectează-l → panoul din stânga → tab **Content** → câmpul **HTML Tag** → schimbă în **H1**.
4. Update.
5. Repetă pentru fiecare șablon.

**Atenție:** dacă o pagină e construită manual în Elementor (nu prin șablon), verifică widgetul
Heading din hero — trebuie să fie H1, și **doar unul singur** per pagină.

**Verificare:** rulează din nou Screaming Frog, filtrul H1 → Missing. Cifra trebuie să fie
aproape de zero. Compară cu ce ai notat la Pasul 0.4.

**Timp:** 1–2 ore.

## Pas 1.2 — Repară culorile și contrastul

**Unde:** Elementor → hamburger stânga-sus → Site Settings → Global Colors.

1. Definește exact două roluri pentru portocaliu:
   - **Accent text** = `#9A3E0A` — pentru orice text colorat pe fundal deschis.
   - **Accent fill** = `#F99E0A` — **exclusiv** fundal de buton, cu text închis deasupra.
2. Șterge celelalte nuanțe de portocaliu/galben din paletă. Elementor îți va arăta unde erau
   folosite; înlocuiește-le cu unul din cele două de mai sus.
3. Titlul H1 principal: schimbă culoarea în `#9A3E0A`.
4. Iconițele galbene, stelele de testimoniale, logo-ul din footer: treci-le pe varianta închisă.

**Verificare:** deschide webaim.org/resources/contrastchecker, introdu culoarea textului și
culoarea fundalului. Trebuie **minimum 4.5:1** pentru text normal, **3:1** pentru elemente grafice.

**Timp:** 1–2 ore.

## Pas 1.3 — Elimină brandul vechi de peste tot

**Unealta:** plugin **Better Search Replace** (gratuit).

1. Instalează-l. WordPress → Tools → Better Search Replace.
2. Rulează pe rând, cu **„Run as dry run" BIFAT prima dată**, următoarele căutări:
   - `Comparatot`
   - `Compară Tot`
   - `Compara Tot`
   - `Recudo`
3. Dry run îți arată câte apariții există și în ce tabele. **Citește rezultatul înainte de a
   rula pe bune.**
4. Debifează dry run și rulează efectiv, înlocuind cu `Reduco`.
5. **Verifică manual și separat**, pentru că plugin-ul nu acoperă tot:
   - Titlurile și meta descrierile din Yoast/RankMath (pagina `/centrale-termice-rate/`
     are „Compară Tot" în titlu).
   - Textele alt ale imaginilor: Media → Library → caută în alt text.
   - Numele fișierelor media încărcate.
   - Meniul principal și footer.

**Verificare:** caută în Google `site:reduco.ro comparatot` și `site:reduco.ro "compara tot"`.
Rezultatele vor dispărea în câteva zile-săptămâni, după reindexare.

**Timp:** 1 oră + verificări.

## Pas 1.4 — Curăță formularul de contact

**Unde:** plugin-ul de formulare (Contact Form 7, WPForms, Elementor Forms — depinde ce e instalat).

**Șterge:**
- câmpul „Model și capacitate"
- câmpul „Sunt client Enel"
- orice alt câmp rezidual care nu are legătură cu energia

**Adaugă, în această ordine:**
1. Comutator / butoane radio: **Persoană fizică** sau **Firmă** (primul câmp, obligatoriu)
2. **Denumire firmă** + **CUI** (apar doar dacă a ales Firmă)
3. **Număr de puncte de consum** — listă: 1 / 2-4 / 5-10 / peste 10
4. **Consum lunar aproximativ** — listă cu intervale
5. **Utilități** — bife: energie electrică / gaze / ambele
6. **Atașează ultima factură** — upload, opțional, max 10 MB, PDF/JPG/PNG
7. **Nume**, **telefon**, **email**

**Verificare:** trimite un test cu date reale de-ale tale. Verifică: ajunge emailul? Se vede
fișierul atașat? Câmpurile condiționate apar corect?

**Timp:** 1 oră.

## Pas 1.5 — Viteză: elimină balastul

1. **Popup-uri:** găsește-le în plugin-ul de popup (Elementor Popups sau similar). Din cele patru
   identice, **dezactivează trei**. Păstrează unul singur, cel mai performant.
2. **Chat:** dacă e încărcat sincron, treci-l pe încărcare amânată. La majoritatea soluțiilor
   există opțiune „load after page load" sau „load on interaction". Dacă nu, cere dezvoltatorului
   să mute scriptul la finalul body cu atributul `defer`.

**Verificare:** rulează PageSpeed Insights pe pagina principală, înainte și după. Notează
ambele scoruri.

**Timp:** 2 ore.

---

# FAZA 2 — Metadatele și primul semnal de repoziționare (săptămâna 2)

Aici site-ul începe să comunice altceva. Se face **după** ce Faza 1 e terminată și verificată.

## Pas 2.1 — Rescrie titlurile și descrierile

**Unde:** Yoast SEO sau RankMath, în editorul fiecărei pagini, secțiunea de la baza paginii.

Textele sunt deja scrise în `02-strategie-seo.md`, secțiunea 4 — gata de copiat, pentru 16 pagini.

**Ordinea, de sus în jos:**
1. Pagina principală
2. `/servicii/`
3. `/abonamente/` — **atenție, aici e eroarea „Recudo"**
4. `/audit-facturi/`
5. `/litigii-anre/`
6. `/recuperare-compensatii/`
7. `/racordare-energie-gaz/`
8. `/solutii-imm/`
9. restul

**Regula:** title maximum ~60 de caractere, meta description ~155. Yoast îți arată bara colorată —
trebuie să rămână verde.

**Verificare:** după fiecare pagină, folosește previzualizarea Google din Yoast. Citește-o ca și
cum ai fi un client. Ai da click?

**Timp:** 3–4 ore.

## Pas 2.2 — Repară subdomeniul

**Unde:** `smart.reduco.ro`, în panoul lui de administrare.

Schimbă titlul care conține „Comparator Furnizori". Propunere:
`Analiză facturi și monitorizare consum — Reduco`

**De ce:** e absurd să repoziționezi site-ul principal în timp ce propriul subdomeniu se declară
comparator, în Google, sub același brand.

**Timp:** 30 de minute.

## Pas 2.3 — Schimbă butonul care ucide leadurile B2B

**Unde:** pagina `/abonamente/`, secțiunea Business.

1. Găsește butoanele „Alege" de la pachetele Business.
2. Schimbă textul în: **„Cere auditul gratuit al facturii"**.
3. Schimbă linkul: **nu** mai duce în coșul WooCommerce, ci către formularul de calificare
   (pagina de contact sau o ancoră către formular).
4. Pentru abonamentul casnic de 24,20 lei, coșul poate rămâne — acolo achiziția directă are sens.

**Verificare:** click pe buton într-o fereastră incognito. Trebuie să ajungi la formular,
nu în coș.

**Timp:** 2 ore.

## Pas 2.4 — Redirecturile

**Unealta:** plugin **Redirection** (gratuit) sau direct în `.htaccess`, dacă ai acces.

1. Ia lista de la Pasul 0.4, coloana Decizie = REDIRECT.
2. Pentru fiecare, adaugă o regulă **301** către destinația din `02-strategie-seo.md`, secțiunea 3.
3. Regula generală: paginile vechi cu prețuri din 2022 merg către `/solutii-imm/` sau către
   comparatoarele curente; `/cine-suntem/` merge către `/despre-noi/`.
4. **Nu redirecta totul către pagina principală.** Un redirect către o pagină irelevantă e tratat
   ca eroare 404 și pierzi valoarea linkului.

**Verificare:** deschide fiecare URL vechi într-o fereastră incognito. Trebuie să ajungi pe pagina
nouă, iar în bara de adresă să apară URL-ul nou. Verifică apoi în Screaming Frog că nu ai
**lanțuri** de redirect (A → B → C); trebuie să fie direct A → C.

**Timp:** 2–3 ore.

---

# FAZA 3 — Mesajul nou (luna 1)

Copy-ul e deja scris în `06-copy-pagini.md`. Aici doar îl implementezi.

**Condiție de intrare:** Pasul 0.5 are răspuns. Fără el, nu publica textele despre independență.

## Pas 3.1 — Ordinea paginilor

Se rescriu în această ordine, nu alta:

| # | Pagina | De ce în acest moment |
| --- | --- | --- |
| 1 | `/audit-facturi/` | Primește deja trafic B2B pe care îl pierde. Cea mai rapidă recuperare |
| 2 | `/litigii-anre/` | Diferențiatorul cel mai puternic, azi invizibil |
| 3 | `/pentru-firme/` (nouă) | Pilonul comercial care leagă tot restul |
| 4 | `/despre-noi/` | Pagina pe care o verifică un director financiar înainte să semneze |
| 5 | `/servicii/` | Regrupată pe cele 4 familii, cu linkuri către toate serviciile |
| 6 | `/abonamente/` | Reorganizată: business primul, casnicul pe pagină separată |

**Pentru fiecare pagină, procedura e aceeași:**
1. Deschide pagina în Elementor.
2. Copiază textul din `06-copy-pagini.md`, secțiunea corespunzătoare.
3. Verifică structura: **un singur H1**, apoi H2 pentru secțiuni, H3 pentru subsecțiuni.
4. Adaugă linkuri interne către celelalte pagini de serviciu.
5. Adaugă CTA-ul: „Cere auditul gratuit al facturii".
6. Update → verifică pe mobil → verifică pe desktop.

## Pas 3.2 — Creează pagina `/pentru-firme/`

**Structura, în ordine, de sus în jos:**
1. Hero: promisiunea pentru firme + CTA
2. „Ce verificăm pe factura dumneavoastră" — cele 8 constatări
3. Cele 4 pachete, cu Multi-Locație marcat vizual ca recomandat
4. Serviciile de proiect, cu modelele de plată la succes
5. **„Cine ne plătește"** — declarația de model de venit (vezi Pasul 0.5)
6. Studii de caz cu cifre
7. Întrebări frecvente
8. CTA final

**După publicare:** redirect 301 de la `/solutii-imm/` către `/pentru-firme/`.

## Pas 3.3 — Corectează afirmația de 10–55%

Pe `/solutii-imm/` (sau pe noua `/pentru-firme/`), scoate „economii medii între 10% și 55%".

Înlocuiește cu o cifră reală și specifică: *„La un punct de consum pe medie tensiune din județul
Suceava, diferența dintre tariful plătit și prețul disponibil în piață era de 3.803 lei pe lună."*

O cifră exactă dintr-un caz real convinge un director financiar. Un interval de la 10 la 55%
îl face suspicios.

## Pas 3.4 — Secțiunea „Cine ne plătește"

Apare pe: pagina principală, `/pentru-firme/`, `/abonamente/` și în footer.

Textul depinde de răspunsul de la Pasul 0.5. Nu improviza aici — e afirmația cea mai atacabilă
de pe tot site-ul și singura pe care concurența nu o poate copia.

## Pas 3.5 — Leagă subdomeniul

Adaugă linkuri către `smart.reduco.ro/prosumatori` din: meniul principal, pagina `/servicii/`,
pagina `/consultanta-prosumator/` și footer.

Astăzi e o platformă separată, la care nu se ajunge din site-ul principal.

---

# FAZA 4 — Verificare finală (sfârșitul lunii 1)

Rulează un crawl complet Screaming Frog și verifică fiecare rând:

| Ce verifici | Ținta |
| --- | --- |
| Pagini fără H1 | 0 |
| Pagini cu mai multe H1 | 0 |
| Lanțuri de redirect (A→B→C) | 0 |
| Pagini orfane (fără link intern către ele) | 0 |
| Titluri duplicate | 0 |
| Apariții „Comparatot" / „Recudo" | 0 |
| Pagini de serviciu la mai mult de 2 clicuri de homepage | 0 |
| Erori 404 interne | 0 |

**În Google Search Console:**
1. Trimite sitemap-ul actualizat.
2. Cere indexarea manuală pentru paginile rescrise (URL Inspection → Request Indexing).
3. Verifică Coverage → paginile vechi trebuie să treacă în „Redirect", nu să rămână indexate.

---

# FAZA 5 — Măsurarea (începe imediat, se citește la 3 luni)

**Nu judeca rezultatele mai devreme de 8–12 săptămâni.** Repoziționarea trece printr-o perioadă
în care traficul poate scădea, pentru că pierzi vizitatori care căutau un comparator gratuit.
Aceștia nu cumpărau nimic. E o curățare, nu o pierdere.

**Indicatorul principal, cel care contează cu adevărat:**
numărul de **cereri de audit gratuit venite de la firme, cu CUI completat**, pe lună.

Traficul nu plătește salarii. Un site cu jumătate din trafic dar cu cinci ori mai multe cereri
B2B calificate este un site mai bun.

**Ce mai urmărești lunar:**
- Rata formular văzut → formular trimis (ținta: peste 20%)
- Ponderea leadurilor de firmă în total leaduri (trebuie să crească lună de lună)
- Poziția pe cuvintele-cheie ancoră (GSC)
- CTR pe paginile cu titluri noi (GSC) — arată direct dacă noile titluri funcționează

---

# Dacă ceva merge prost

| Simptom | Cauza probabilă | Ce faci |
| --- | --- | --- |
| Traficul scade brusc după redirecturi | Redirecturi greșite sau lanțuri | Verifică în Screaming Frog; corectează destinațiile |
| Paginile nu se mai afișează corect | Modificare de șablon la Pasul 1.1 | Restaurează șablonul din backup-ul de la 0.1 |
| Formularul nu mai trimite emailuri | Câmp obligatoriu greșit configurat | Testează cu toate câmpurile completate; verifică setările SMTP |
| Google arată încă textele vechi | Reindexare în curs | Normal. Durează 2–6 săptămâni. Cere indexare manuală |
| Scade numărul total de leaduri, dar cresc cele B2B | **Funcționează corect** | Nu interveni. Asta e ținta |

**Punct de retragere:** dacă după patru săptămâni ceva e clar mai rău și nu identifici cauza,
restaurezi backup-ul de la Pasul 0.1 și reiei pas cu pas, cu verificare după fiecare.
De aceea backup-ul e Pasul 0.1 și nu Pasul 5.

---

# Cine face ce

| Pas | Cine | Poate fi delegat? |
| --- | --- | --- |
| 0.1–0.4 pregătire | Dezvoltator sau tu | Da |
| **0.5 decizia pe modelul de venit** | **Tu** | **Nu** |
| 1.1–1.2 Elementor | Dezvoltator | Da |
| 1.3 brand vechi | Dezvoltator, cu verificare de la tine | Parțial |
| 1.4 formular | Dezvoltator | Da |
| 1.5 viteză | Dezvoltator | Da |
| 2.1–2.2 metadate | Tu sau un om de marketing | Da |
| 2.3 buton CTA | Dezvoltator | Da |
| 2.4 redirecturi | Dezvoltator | Da |
| 3.1–3.5 copy | Tu, cu textele deja scrise | Parțial |
| **3.4 „Cine ne plătește"** | **Tu** | **Nu** |
| 4 verificare | Dezvoltator + tu | Parțial |
| 5 măsurare | Tu | Nu |

**Estimare de efort tehnic total pentru Fazele 0–2:** aproximativ 20–25 de ore de dezvoltator.
Faza 3 depinde de cât de repede validezi copy-ul, nu de efortul tehnic.
