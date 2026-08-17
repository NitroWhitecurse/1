# Reduco.ro — plan de conversie și implementare pe site

Acest document acoperă **mecanica** repoziționării: pâlnia B2B, formularele, pagina de prețuri,
dovada socială, accesibilitatea și măsurarea. Poziționarea și mesajele sunt în `03-platforma-brand.md`,
partea de SEO în `02-strategie-seo.md`.

---

## 1. Problema centrală de conversie

Reduco vinde astăzi un abonament de 149–1.500 lei/lună printr-un buton „Alege" care duce
direct în coșul WooCommerce. Este o eroare de potrivire între produs și mecanism:

| Ce vinde Reduco | Ce presupune mecanismul actual |
| --- | --- |
| Serviciu de consultanță recurentă, ~4.000 lei/an | Achiziție impulsivă, ca un produs de e-commerce |
| Decizie cu aprobare internă (administrator, CFO) | Decizie individuală, pe loc |
| Preț care depinde de numărul de puncte de consum | Preț fix, afișat înainte de a ști nevoia |
| Încredere construită prin dovezi | Zero dovadă socială B2B pe site |

Nimeni nu cumpără un abonament de consultanță energetică la prima vizită pe site. Pâlnia
trebuie reconstruită în jurul **auditului gratuit de factură** ca produs de intrare — Reduco
îl are deja standardizat, cu livrare în 48 de ore.

## 2. Pâlnia B2B propusă

```
Trafic organic B2B (blog + pagini de serviciu)
        │
        ▼
Pagina de serviciu relevantă (/audit-facturi, /litigii-anre, /recuperare-compensatii)
        │
        ▼
CTA unic: „Cere auditul gratuit al facturii"
        │
        ▼
Formular de calificare (6 câmpuri, sub 60 de secunde)
        │
        ▼
Raport de audit în 48h  ──►  cifra economiei anuale, în lei, pe prima pagină
        │
        ▼
Discuție de vânzare consultativă
        │
        ├──► Abonament lunar (venit recurent)
        └──► Serviciu de proiect (litigiu, compensații, Legea 121, reactivă)
```

Regula: **un singur CTA principal pe tot site-ul pentru B2B** — auditul gratuit. Orice alt
buton („Alege", „Cumpără", „Vezi prețuri") concurează cu el și diluează conversia.

## 3. Modificări pe pagini, în ordinea impactului

### 3.1 Înlocuirea checkout-ului B2B cu lead calificat — impact maxim
- Butonul „Alege" de la pachetele Business → **„Cere auditul gratuit al facturii"**.
- Se elimină complet fluxul WooCommerce pentru pachetele Business. Coșul rămâne, dacă e util,
  doar pentru abonamentul casnic de 24,20 lei, unde achiziția directă are sens.
- Prețurile rămân afișate — dar ca **ordin de mărime**, cu mențiunea „prețul final depinde de
  numărul de puncte de consum". Aceasta e și recomandarea internă existentă: opțiunea de a
  personaliza crește valoarea medie a contractului.

### 3.2 Pagina dedicată `/pentru-firme/`
Astăzi vizitatorul de firmă aterizează pe `/abonamente/`, care deschide cu secțiunea „Casnici",
și trebuie să deruleze tot tabelul rezidențial. O pagină dedicată rezolvă simultan conversia și SEO.

Structura recomandată:
1. Hero cu promisiunea pentru firme + CTA audit gratuit.
2. „Cât pierdeți fără să știți" — cele 8 constatări din auditul de factură, ca listă de verificare.
3. Cele 4 pachete, cu Multi-Locație marcat vizual ca recomandat.
4. Serviciile de proiect, cu modelele de plată la succes.
5. „Cine ne plătește" — declarația de independență.
6. Studii de caz cu cifre.
7. FAQ.
8. CTA final.

### 3.3 Formularul de calificare
Se elimină câmpurile reziduale („Model și capacitate", „Sunt client Enel").

Câmpuri noi, în această ordine:
| Câmp | Tip | De ce |
| --- | --- | --- |
| Sunteți persoană fizică sau firmă? | Comutator | Rutează leadul din primul clic |
| Denumire firmă + CUI | Text | Calificare și verificare prealabilă |
| Număr de puncte de consum | Select (1 / 2-4 / 5-10 / 10+) | Determină pachetul și prețul |
| Consum lunar aproximativ | Select (intervale) | Separă industrialul de IMM |
| Utilități | Bifă (energie / gaze / ambele) | Domeniul auditului |
| Factură atașată | Upload, opțional | Scurtează ciclul cu o rundă întreagă |
| Nume + telefon + email | Text | Contact |

Regula: fiecare câmp în plus scade rata de completare. Șase câmpuri obligatorii este pragul
rezonabil pentru un lead B2B care primește în schimb un audit real de 48 de ore.

### 3.4 Rescrierea `/cine-suntem/` → `/despre-noi/`
Pagina conține încă textul brandului anterior, nemodificat din 2022. Este pagina pe care o
verifică un director financiar înainte de a semna. Trebuie să conțină: povestea repoziționării,
competența juridică demonstrată, modelul de remunerare, echipa cu nume și rol.
Redirect 301 de la `/cine-suntem/`.

### 3.5 Dovada socială B2B
Astăzi există un singur testimonial pe tot site-ul, pe `/recuperare-compensatii`.
Minimum necesar înainte de a împinge trafic plătit sau outreach:
- **3 studii de caz** cu structura: sector, dimensiune, situația inițială, ce am făcut, rezultat în lei.
  Dosarele reale există deja (litigiul cu facturare retroactivă pe 25 de luni, index supraevaluat
  de 4x, compensații ANRE). Se pot publica anonimizat — „rețea de farmacii veterinare, județul X".
- **Datele care contează pentru un CFO:** suma recuperată, procentul de reducere a prețului unitar,
  durata până la rezultat.
- Pe fiecare pagină de serviciu, cazul relevant pentru acel serviciu.

### 3.6 „Cine ne plătește" — secțiune permanentă
Independența (zero comision de la furnizori) este singurul argument pe care concurența nu îl
poate copia fără să-și schimbe modelul de business. Trebuie să apară: pe homepage, pe
`/pentru-firme/`, pe `/abonamente/` și în footer. Astăzi nu apare nicăieri vizibil.

### 3.7 Legarea `smart.reduco.ro`
Platforma de prosumatori și comparatorul trăiesc pe un subdomeniu fără link din pagina
principală. Se leagă din meniul principal și din `/consultanta-prosumator`.
Notă strategică: după repoziționare, comparatorul devine **un instrument din serviciu**,
nu produsul. Se prezintă ca „instrumentul pe care îl folosim pentru dumneavoastră", nu ca ofertă.

## 4. Accesibilitate — de reparat înainte de orice campanie

| Element | Contrast actual | Minim necesar | Fix |
| --- | --- | --- | --- |
| H1 portocaliu pe fundal deschis | 1.86:1 | 4.5:1 | `#9A3E0A` pentru text |
| Logo footer | ~2.0:1 | 3:1 | Varianta închisă a logo-ului |
| Stele testimoniale | ~2.1:1 | 3:1 | Nuanță închisă |
| Iconițe galbene | ~2.0:1 | 3:1 | Nuanță închisă |

Regula propusă: `#F99E0A` rămâne exclusiv culoare de fundal pentru butoane, cu text închis
deasupra. Orice text colorat pe fundal deschis folosește `#9A3E0A`.

Alte reparații de bază: unificarea logo-ului (azi verde în header, portocaliu în footer),
reducerea la două nuanțe cu roluri clare, fuzionarea celor două secțiuni hero consecutive
de pe homepage.

## 5. Viteză

- Se elimină cele patru popup-uri identice.
- Chatul se încarcă amânat (după interacțiune sau după `load`).
- Diagnostic complet de viteză: 6–12 ore de lucru estimate intern.

Viteza contează dublu aici: este factor de clasare și, pe mobil, principala cauză de abandon
înainte de a vedea formularul.

## 6. Măsurare — ce urmărim după lansare

| Indicator | De ce contează | Ținta de referință |
| --- | --- | --- |
| Cereri de audit gratuit / lună | Intrarea în pâlnie, singurul CTA | de stabilit după prima lună |
| Rata formular văzut → trimis | Sănătatea formularului | peste 20% |
| Audit trimis → discuție de vânzare | Calitatea raportului | peste 40% |
| Discuție → abonament sau proiect | Eficiența vânzării | de stabilit |
| Ponderea leadurilor de firmă în total | Progresul repoziționării B2B | în creștere lună de lună |
| Poziția pe cuvintele-cheie B2B | Progresul SEO | vezi `02-strategie-seo.md` |
| Valoarea medie a contractului | Efectul facturării pe punct de consum | în creștere |

Configurare minimă: eveniment separat pentru trimiterea formularului B2B vs B2C, urmărirea
sursei leadului (organic / LinkedIn / recomandare contabil), și un câmp „de unde ați aflat".

## 7. Ordinea de execuție

### Săptămânile 1–2 — oprim pierderile
1. `noindex` temporar pe cele ~14 pagini cu prețuri din 2022.
2. Corectarea meta description de pe `/abonamente` — conține „Recudo" scris greșit și un preț vechi.
3. Fix contrast H1 (o singură setare în șablon).
4. Înlocuirea butonului „Alege" cu „Cere auditul gratuit al facturii" pe pachetele Business.
5. Curățarea formularului de câmpurile reziduale.

### Luna 1 — construim baza
6. Pagina `/pentru-firme/`.
7. Rescrierea `/cine-suntem/` → `/despre-noi/` cu poziționarea nouă.
8. Formularul de calificare complet.
9. Redirecturile 301 pentru paginile vechi.
10. Repararea H1 în șablonul Elementor, pe tot site-ul.
11. Link-uri interne din `/solutii-imm` și `/servicii` spre toate paginile de serviciu.
12. Secțiunea „Cine ne plătește".

### Trimestrul 1 — creștem
13. Cele 3 studii de caz B2B.
14. Noua grilă de abonamente, cu facturare pe punct de consum.
15. Legarea `smart.reduco.ro`.
16. Diagnosticul de viteză.
17. Programul de conținut B2B (vezi `02-strategie-seo.md`).
18. Canalul de parteneri-contabili.

## 8. Decizii care necesită confirmarea ta

Acestea nu pot fi luate din documente — depind de operațiuni și de capacitatea de livrare:

1. **Prețurile noi** (149 / 349 / 89-per-locație / 1.500+) sunt propuneri interne. Trebuie
   calibrate cu timpul real de livrare per client înainte de publicare.
2. **Politica de perioadă minimă contractuală** — documentul intern o marchează „de confirmat".
3. **Ce se întâmplă cu comparatorul** ca produs public: rămâne gratuit și deschis ca instrument
   de generare de leaduri, sau devine beneficiu pentru abonați? Documentele interne conțin ambele idei.
4. **Capacitatea de livrare** — câte audituri gratuite pe lună pot fi livrate în 48 de ore
   fără a rupe promisiunea. Promisiunea de viteză nerespectată face mai mult rău decât lipsa ei.
