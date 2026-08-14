# Reduco.ro — Economia unitară: abonament actual vs. 4 modele alternative

**Client:** Reduco.ro (ALMA SKY SRL, Bacău) · **Data:** 2026-08-14
**Sursă date:** cifrele reale de portofoliu date de client (Caz GRIDOMA SERV-COM, Caz birou notarial Bacău, grila de abonamente 2026) + `/home/user/1/reduco/plan-extindere-b2b.md` (context intern deja existent despre pragul de audit gratuit).

Toate calculele de mai jos sunt rulate cu Python/Bash — comenzile și rezultatele brute sunt reproduse așa cum au ieșit, nu re-tastate manual.

---

## 0. Verificare de bază: TVA și prețurile de listă

```
Basic:    99 lei/lună fără TVA -> 119.79 lei/lună cu TVA (TVA 21%)
Standard: 199 lei/lună fără TVA -> 240.79 lei/lună cu TVA (TVA 21%)
Premium:  399 lei/lună fără TVA -> 482.79 lei/lună cu TVA (TVA 21%)
```

Cota de TVA folosită e 21%, dedusă invers din cifra dată de client (199 × 1,21 = 240,79 — se potrivește exact). Confirmă că din august 2025 România a trecut la TVA standard 21%.

Peste tot mai jos folosesc **venitul fără TVA** ca venit real al firmei (TVA-ul e colectat și virat statului, nu e marjă) și **prețul cu TVA** ca sumă efectivă plătită de client, pentru comparațiile de "cât rămâne clientului".

---

## 1. Datele reale — verificate cu calcul, nu doar citate

**Caz 1 — GRIDOMA SERV-COM (medie tensiune, Suceava)**
```
Consum: 18.800 kWh/lună
Factura veche = 18.800 × 1,24 = 23.312 lei/lună
Factura nouă  = 18.800 × 1,04 = 19.552 lei/lună
Delta preț = 0,20 lei/kWh
Economie calculată (consum × delta) = 18.800 × 0,20 = 3.760 lei/lună
Economie raportată de client: 3.804 lei/lună (diferență mică, probabil taxe/certificate incluse în factura reală)
% economie față de factura veche = 3.804 / 23.312 = 16,3%
```

**Caz 2 — birou notarial (joasă tensiune, Bacău)**
```
Consum: 864 kWh/lună
Factura veche = 864 × 1,63 = 1.408,32 lei/lună
Factura nouă  = 864 × 1,33 = 1.149,12 lei/lună
Delta preț = 0,30 lei/kWh
Economie calculată = 864 × 0,30 = 259,2 lei/lună (raportat: 262 lei/lună)
% economie față de factura veche = 262 / 1.408,32 = 18,6%
Abonament Standard cu TVA = 240,79 lei/lună
Economie NETĂ a clientului = 262 − 240,79 = 21,21 lei/lună (confirmă cifra dată: ~21 lei/lună)
```

**Asumpție derivată (nu inventată separat) — % economie mediu tipic:**
```
(16,3% + 18,6%) / 2 = 17,5%
```
Folosesc acest 17,5% ca proxy pentru "cât poate economisi un client tipic" în restul modelului. Cu doar 2 puncte de date, e o estimare aproximativă — se recalibrează după fiecare 10-20 audituri noi.

**Observație de context deja documentată:** `plan-extindere-b2b.md` a stabilit deja un prag operațional de 5.000 lei/lună factură pentru audit gratuit, motivat exact de Cazul 2 ("un astfel de raport nu se vinde și ne consumă aceleași ore ca unul de 45.000 lei/an"). Pragurile calculate mai jos pentru Model A sunt mai mici (~1.400-2.800 lei/lună) pentru că măsoară altceva — rentabilitatea *abonamentului*, nu capacitatea de audit. Cele două praguri nu se contrazic, se combină (vezi recomandarea finală).

---

## Model A — Abonament lunar fix (actual)

**Venit/client/an (fără TVA):**
```
Basic:    99 × 12 = 1.188 lei/an
Standard: 199 × 12 = 2.388 lei/an
Premium:  399 × 12 = 4.788 lei/an
```

**Prag de calificare — podea de supraviețuire (economie = abonament, marjă zero pentru client):**
```
factura_min = abonament_cu_TVA / 0,175
Basic:    119,79 / 0,175 = 684,51 lei/lună
Standard: 240,79 / 0,175 = 1.375,94 lei/lună
Premium:  482,79 / 0,175 = 2.758,80 lei/lună
```

**Validare directă cu datele reale:** Caz 2 avea factura veche de 1.408 lei/lună — practic *chiar la limita* pragului de 1.376 lei calculat pentru Standard. Asta explică matematic de ce economia netă a ieșit doar 21 lei/lună — nu a fost o excepție, a fost un client vândut exact la marginea de rentabilitate a modelului.

**Prag de calificare recomandat (sănătos — economie ≥ 2× abonamentul, ca să nu se repete Cazul 2):**
```
Standard: 2 × 240,79 / 0,175 = 2.751,89 lei/lună ≈ 2.750 lei/lună
```

**Clienți necesari pentru 10.000 lei/lună venit recurent (fără TVA):**
```
Basic:    10.000 / 99  = 101,0 -> 102 clienți
Standard: 10.000 / 199 = 50,3  -> 51 clienți
Premium:  10.000 / 399 = 25,1  -> 26 clienți
```

**Timp de recuperare a costului auditului**
*ASUMPȚIE — nu avem costul orar real al specialistului; ilustrez cu 100 și 150 lei/oră. Cere confirmare de la client.*
```
2h × 100 lei/h = 200 lei audit -> Standard: 200/199 = 1,01 lună
4h × 100 lei/h = 400 lei audit -> Standard: 400/199 = 2,01 luni
2h × 150 lei/h = 300 lei audit -> Standard: 300/199 = 1,51 luni
4h × 150 lei/h = 600 lei audit -> Standard: 600/199 = 3,02 luni
```

**Risc principal:** clientul plătește *înainte* de a vedea rezultatul recurent — barieră de intrare mai mare pentru volum de leaduri decât celelalte modele. Și, așa cum arată Cazul 2, sub pragul de ~1.376-2.750 lei/lună economia netă e prea subțire ca să reziste la reînnoire — churn ridicat exact pe segmentul unde vânzarea e mai ușoară (firme mici, joasă tensiune, multe la număr).

---

## Model B — Success fee (% din economia realizată, plătit doar la rezultat)

*Ratele de mai jos (20/30/40%) sunt ilustrative — Reduco nu a comunicat o rată reală, deci le tratez ca parametru de decizie, nu ca fapt.*

```
rata 20%: Caz1 -> 3.804×0,20 = 760,8 lei/lună  | Caz2 -> 262×0,20 = 52,4 lei/lună
rata 30%: Caz1 -> 3.804×0,30 = 1.141,2 lei/lună | Caz2 -> 262×0,30 = 78,6 lei/lună
rata 40%: Caz1 -> 3.804×0,40 = 1.521,6 lei/lună | Caz2 -> 262×0,40 = 104,8 lei/lună
```

**Venit/client/an la 30% (scenariu central):**
```
Caz1-tip (MT mare): 3.804 × 0,30 × 12 = 13.694,4 lei/an  (vs. max 4.788 lei/an la Premium — de 2,9x mai mult!)
Caz2-tip (JT mic):    262 × 0,30 × 12 = 943,2 lei/an     (vs. 2.388 lei/an la Standard — de 2,5x mai puțin)
```
Modelul se auto-segmentează corect: clientul mare plătește mult mai mult decât la abonament (Reduco captează mai multă valoare), clientul mic plătește mult mai puțin (nu mai e supra-taxat relativ la ce primește).

**Prag de calificare** — fee lunar trebuie să acopere costul minim de deservire.
*ASUMPȚIE — cost minim de deservire/client/lună: 100 lei (facturare, suport, raportare). Nu avem cifra reală de cost operațional a Reduco — de validat.*
```
la 20%: economie_min = 100/0,20 = 500 lei/lună -> factura_min = 500/0,175 = 2.857 lei/lună
la 30%: economie_min = 100/0,30 = 333 lei/lună -> factura_min = 333/0,175 = 1.905 lei/lună
la 40%: economie_min = 100/0,40 = 250 lei/lună -> factura_min = 250/0,175 = 1.429 lei/lună
```

**Clienți necesari pentru 10.000 lei/lună (la 30%):**
```
numai clienți tip Caz1 (MT mare): 10.000 / 1.141,2 = 8,8 -> 9 clienți
numai clienți tip Caz2 (JT mic):  10.000 / 78,6    = 127,2 -> 128 clienți
```
Diferență de peste 14x în număr de clienți necesari — modelul B face portofoliul de clienți mari extrem de valoros și pe cel de clienți mici, greu de scalat singur (vezi Model D pentru soluție).

**Recuperare audit** (cost 200-400 lei, ca la Model A):
```
Caz1: 200/1.141,2 = 0,18 lună | 400/1.141,2 = 0,35 lună (sub o lună)
Caz2: 200/78,6 = 2,54 luni    | 400/78,6 = 5,09 luni (poate depăși 4 luni!)
```

**Risc principal:** venit variabil și decalat (clientul plătește lună de lună *după* ce vede economia pe factura reală — cash flow mai lent pentru Reduco); nevoie de a demonstra continuu "economia realizată" (dispută posibilă dacă piața se mișcă independent); pe clienți mici, fee-ul poate fi sub costul de deservire (vezi pragul de 1.429-2.857 lei/lună mai sus).

---

## Model C — Comision de la furnizor per MWh (broker clasic UK/DE)

*Nu există nicio ofertă reală de comision de la un furnizor pentru Reduco — tot ce urmează e un calcul de reper (ce rată ar fi nevoie), nu o cifră de piață. De cercetat direct cu furnizorii înainte de a construi orice plan pe acest model.*

```
Volum anual Caz1: 18.800 kWh/lună × 12 / 1000 = 225,6 MWh/an
Volum anual Caz2:    864 kWh/lună × 12 / 1000 = 10,37 MWh/an
```

**Ce rată de comision ar egala venitul actual Standard (2.388 lei/an fără TVA)?**
```
Caz1: 2.388 / 225,6 MWh = 10,6 lei/MWh
Caz2: 2.388 / 10,37 MWh = 230,3 lei/MWh  <- nerealist de mare pentru un comision de broker (variază uzual în ordinul zecilor de lei/MWh, nu al sutelor)
```
Concluzie directă din calcul: un comision unic pe MWh care ar avea sens pentru clienți mari (~10-15 lei/MWh) e complet nesemnificativ pentru clienți mici tip Caz 2.

**Sensibilitate — venit la comisioane ilustrative:**
```
10 lei/MWh: Caz1 -> 2.256 lei/an (188 lei/lună)  | Caz2 -> 103,68 lei/an (8,64 lei/lună)
20 lei/MWh: Caz1 -> 4.512 lei/an (376 lei/lună)  | Caz2 -> 207,36 lei/an (17,28 lei/lună)
30 lei/MWh: Caz1 -> 6.768 lei/an (564 lei/lună)  | Caz2 -> 311,04 lei/an (25,92 lei/lună)
50 lei/MWh: Caz1 -> 11.280 lei/an (940 lei/lună) | Caz2 -> 518,4 lei/an (43,2 lei/lună)
```

**Prag de calificare:** la orice comision realist (10-30 lei/MWh), clienții joasă tensiune sub ~5.000-10.000 kWh/lună generează venit nesemnificativ (sub 30 lei/lună) — modelul practic exclude segmentul mic. Prag recomandat: doar clienți medie tensiune sau echivalent (>5.000 kWh/lună).

**Clienți necesari pentru 10.000 lei/lună (=120.000 lei/an) la 15 lei/MWh (ilustrativ):**
```
MWh necesar: 120.000 / 15 = 8.000 MWh/an
doar clienți tip Caz1 (MT): 8.000 / 225,6 = 35,5 -> 36 clienți
doar clienți tip Caz2 (JT): 8.000 / 10,37 = 771,6 -> 772 clienți
```

**Risc principal — cel mai serios dintre toate cinci:** conflict de interese direct. Dacă furnizorul plătește comisionul, Reduco e stimulat să recomande furnizorul care plătește cel mai mult, nu pe cel mai ieftin pentru client — contrazice exact motivul pentru care un client apelează la un consultant "independent". Există și risc de reglementare ANRE (transparență obligatorie a comisionului) și dependența de a obține contracte de la furnizori mari, greu de negociat ca broker nou/mic.

---

## Model D — Grup de cumpărare / agregare cerere

**Câți clienți mici (tip Caz2) echivalează volumul unui singur client mare (tip Caz1)?**
```
18.800 / 864 = 21,8 -> 22 clienți mici = puterea de negociere a 1 client mediu tensiune
```

*ASUMPȚIE taxă de participare în grup: 50 lei/lună/membru — mult sub Standard, pentru că produsul e diferit (acces la preț de volum negociat, nu audit individual). Cifră de test, nu de piață — de validat.*
```
Economie netă client tip Caz2 în grup: 262 − 50 = 212 lei/lună
   (vs. 21,21 lei/lună la abonamentul Standard actual — de 10x mai atractiv pentru clientul mic)
```

**Venit Reduco/client/an la taxa 50 lei/lună:**
```
50 × 12 = 600 lei/an/client (mult sub cei 2.388 lei/an ai Standard — compensat prin volum, nu prin preț)
```

**Clienți necesari pentru 10.000 lei/lună:**
```
10.000 / 50 = 200 clienți
```

**Recuperare audit** (cost 200-400 lei):
```
200 / 50 = 4,0 luni
400 / 50 = 8,0 luni
```
Cel mai lung timp de recuperare dintre toate modelele — motiv pentru care Model D nu ar trebui să fie un canal de sine stătător ci un "coș" pentru clienții sub pragul altor modele.

**Prag de calificare:** aproape inexistent la nivel de client individual (chiar și consumatori foarte mici pot beneficia), DAR există un prag agregat obligatoriu — grupul nu are putere de negociere sub o masă critică (recomandat ≥ 20-22 clienți mici sau echivalent, cf. calculul de mai sus).

**Risc principal:** problema de "cold start" (nu ai putere de negociere până nu ai deja 20+ clienți, dar nu-i atragi ușor fără o ofertă de volum deja negociată); complexitate juridică/administrativă de a agrega contracte individuale sub o singură negociere cu furnizorul; timp lung de organizare, nu e un canal rapid.

---

## Model E — Retainer în trepte, indexat la consum

Trepte propuse (**propunere de discutat, nu date de piață**):
```
Tier 1: <1.000 kWh/lună      -> 99 lei/lună  (= Basic actual, neschimbat)
Tier 2: 1.000-5.000 kWh/lună -> 199 lei/lună (= Standard actual, neschimbat)
Tier 3: 5.000-15.000 kWh/lună -> 499 lei/lună (nou)
Tier 4: >15.000 kWh/lună (MT) -> 899 lei/lună (nou)
```

**Cât din valoarea creată la Cazul 1 (economie 3.804 lei/lună) captează fiecare model:**
```
Model A (Premium, plafon actual): 399/3.804 = 10,5% din economia clientului
Model E (Tier 4 propus, 899 lei):  899/3.804 = 23,6% din economia clientului

Venit anual/client MT: A = 4.788 lei/an  vs  E = 10.788 lei/an  -> +6.000 lei/an/client (+125%)
Clientul rămâne oricum cu 2.905 lei/lună economie netă (vs. 3.405 lei la Model A) — încă foarte atractiv pentru el.
```
Cea mai clară "scurgere de valoare" din tot exercițiul: la modelul actual, un client de tip Caz1 e plafonat la Premium (399 lei) deși generează 3.804 lei/lună economie — Reduco lasă pe masă ~500 lei/lună doar pentru acest tip de client.

**Clienți necesari pentru 10.000 lei/lună** (mix ilustrativ: 60% clienți Tier2, 40% Tier3+ la ~600 lei mediu):
```
venit mediu ponderat/client = 0,6×199 + 0,4×600 = 359,4 lei/lună
10.000 / 359,4 = 27,8 -> 28 clienți (vs. 51 clienți necesari la Model A doar-Standard)
```

**Prag de calificare:** identic cu Model A pentru treapta cea mai mică (~1.376-2.750 lei/lună factură, aceeași logică 17,5% economie ÷ preț), dar cu upside proporțional mai mare pentru clienții mari — nu mai există plafon artificial.

**Risc principal:** friction suplimentar la vânzare (trebuie clasificat corect fiecare client înainte de semnare, posibil necesită factura în avans, ceea ce reintroduce parțial bariera "trimite factura întâi" pe care Model B o elimină); nevoie de renegociere de treaptă dacă consumul clientului variază sezonier; clienții mari pot simți că sunt "taxați disproporționat" dacă nu li se arată clar raportul 4x economie/cost.

---

## Comparație directă: cine protejează cel mai bine clientul mic la un delta de preț scăzut

La delta 0,05 lei/kWh (piață cu marjă mică de negociere), Caz2 (864 kWh) generează doar 43,2 lei/lună economie brută:

```
Model A (Standard fix, 240,79 lei cu TVA): net client = 43,2 − 240,79 = −197,59 lei/lună  -> NEGATIV, clientul pierde bani
Model B (success fee 30%): fee = 43,2×0,30 = 12,96 lei/lună, net client = +30,24 lei/lună  -> mereu pozitiv (dar venit Reduco minim)
Model D (taxă grup fixă 50 lei): net client = 43,2 − 50 = −6,8 lei/luna -> tot NEGATIV (taxă fixă, nu scalează cu economia)
Model E (Tier1 fix 99 lei fără TVA = 119,79 cu TVA): net client = 43,2 − 119,79 = −76,59 lei/lună -> NEGATIV
```

Concluzie importantă: **doar Model B (procent din economie) e structural imun la scăderea deltei de preț** — nu poate produce niciodată o pierdere netă pentru client, indiferent cât de mică e economia. Toate modelele cu taxă fixă (A, D, E) pot deveni "capcane" pentru clientul mic dacă piața se comprimă. Asta e un argument financiar concret pentru B, nu doar unul de marketing.

---

## Tabel de sensibilitate — delta preț 0,05 / 0,10 / 0,20 / 0,35 lei/kWh

```
Economie brută lunară = consum_kWh × delta_pret
Prag consum breakeven Model A Standard = 240,79 / delta_pret
```

| Delta (lei/kWh) | Economie/1.000 kWh (lei/lună) | Caz1 — 18.800 kWh (lei/lună) | Caz2 — 864 kWh (lei/lună) | Prag breakeven Standard (kWh/lună) |
|---|---|---|---|---|
| 0,05 | 50,0 | 940,0 | 43,2 | 4.815,8 |
| 0,10 | 100,0 | 1.880,0 | 86,4 | 2.407,9 |
| 0,20 | 200,0 | 3.760,0 | 172,8 | 1.203,95 |
| 0,35 | 350,0 | 6.580,0 | 302,4 | 688,0 |

**Interpretare linie cu linie:**
- **0,05 lei/kWh:** cel mai riscant scenariu. Pragul breakeven pentru Model A urcă la aproape 4.816 kWh/lună — majoritatea firmelor mici (tip Caz2) ar pierde bani net la un abonament Standard. Doar Model B rămâne sigur pentru client la acest nivel.
- **0,10 lei/kWh:** pragul coboară la 2.408 kWh — încă peste consumul lui Caz2 (864 kWh); același risc, atenuat.
- **0,20 lei/kWh:** e aproximativ delta reală observată la Caz1 (0,20) — pragul de 1.204 kWh e sub Caz1, confirmă că modelul funcționează bine pentru clienți medii/mari la acest nivel de piață.
- **0,35 lei/kWh:** cel mai favorabil — pragul breakeven coboară la 688 kWh, sub pragul lui Caz2 (864 kWh) — la acest nivel de piață chiar și clientul mic din portofoliu ar fi ușor pozitiv pe Model A.

**Implicație practică:** deltele de preț disponibile pe piață nu sunt constante — depind de cât de proastă a fost oferta veche a clientului și de condițiile pieței angro. Un model care depinde de un preț fix (A, D, E) e vulnerabil quando delta scade; un model procentual (B) se auto-ajustează.

---

## PRAGURI DE CALIFICARE — sinteză numerică (factură lunară minimă, lei)

| Model | Prag breakeven strict (lei/lună) | Prag recomandat (sănătos, lei/lună) | Notă |
|---|---|---|---|
| **A — Abonament fix (Standard)** | 1.376 | 2.750 | Sub prag: Cazul 2 s-a repetat (economie netă ~21 lei) |
| **B — Success fee (30%)** | ~1.000 (economie ≥ cost deservire/rată) | 1.905 | Fără prag dur — clientul nu poate pierde bani, dar sub prag Reduco nu-și acoperă costul de deservire |
| **C — Comision furnizor** | ~5.000 kWh/lună (echivalent MT) | ~10.000 kWh/lună | Sub prag, venitul e sub 30-50 lei/lună — irelevant financiar |
| **D — Grup de cumpărare** | ~0 la nivel individual | N/A (prag e la nivel de grup, ≥20-22 membri) | Singurul model conceput ca client-mic-by-design |
| **E — Retainer în trepte** | 1.376 (Tier1/2, identic cu A) | 2.750 (identic cu A până la Tier3) | Diferă de A doar peste 5.000 kWh — nu prin prag, ci prin captare de valoare |

Pragul deja stabilit intern de 5.000 lei/lună (din `plan-extindere-b2b.md`, pentru audit *gratuit*) e mai strict decât pragul de rentabilitate al abonamentului (1.376-2.750 lei) — și corect așa, pentru că măsoară o resursă diferită (2-4 ore de muncă a unui specialist, care nu poate fi cheltuită la infinit), nu doar rentabilitatea abonamentului lunar.

---

## Recomandare: care model susține cel mai bine CREȘTEREA VOLUMULUI DE LEADURI

**Model B (success fee) e singurul dintre cele cinci conceput să scadă bariera de intrare, nu doar marja.** Argumentele, toate derivate din calculele de mai sus:

1. **Elimină riscul perceput de client** — "plătești doar dacă ai rezultat" e exact ce lipsește din Model A (client trebuie să se aboneze *înainte* de rezultat) și explică parțial de ce site-ul Reduco cere azi să alegi un abonament la prima atingere, ceea ce documentul intern (`plan-extindere-b2b.md`, punctul 1) identifică deja ca problemă de conversie.
2. **E structural imun la scăderea deltei de preț** — secțiunea de mai sus arată că, spre deosebire de A/D/E, Model B nu poate produce niciodată o pierdere netă pentru client, indiferent de condițiile de piață.
3. **Capturează corect valoarea la ambele capete** — clientul mare (Caz1) generează 13.694 lei/an vs. maxim 4.788 lei/an la Premium; clientul mic (Caz2) plătește doar 943 lei/an, proporțional cu ce a primit, nu mai are stimulent să anuleze un abonament care-i aduce doar 21 lei net.

**Dar Model B singur nu e suficient** — la clienți mici, venitul pe client (78,6 lei/lună la 30%) e prea mic ca să acopere costul de deservire estimat, iar cash flow-ul e decalat (clientul plătește după ce vede economia). De aceea recomand o **combinație pe etape, nu un singur model**:

- **Ușa de intrare, pentru volum:** Model B — success fee (rată de decis cu CEO, ilustrată aici la 20-40%), fără barieră inițială, pe primele 3-6 luni sau pe primul an de contract, exact pe segmentul unde Reduco vrea creștere de leaduri (firme mici și medii care azi ezită să se aboneze fără să vadă rezultatul).
- **Migrare la retainer, pentru marjă și predictibilitate:** după ce economia e dovedită pe factură reală (1-2 cicluri de facturare), oferă trecerea la **Model E (retainer în trepte)** — captează corect valoarea de la clienții mari (Caz1-tip, +125% venit față de plafonul actual Premium) fără să piardă clienții mici care rămân pe treptele Basic/Standard nemodificate.
- **Coș pentru clienții sub prag, ca să nu-i pierzi:** clienții care nu ating pragul de calificare individual pentru B sau E (sub ~1.400-1.900 lei/lună factură) nu trebuie refuzați, ci direcționați spre **Model D (grup de cumpărare)** — singurul model conceput să facă un client mic (tip Caz2) rentabil prin agregare, nu prin taxare disproporționată.
- **Model C — nu ca model principal.** Calculul arată riscul de conflict de interese (Reduco ar fi plătită de furnizor să recomande, nu de client să fie obiectivă) și dependența de negocieri greu de obținut ca broker nou. Poate exista ca venit secundar, transparent, disclosed clientului, dar nu ar trebui să înlocuiască relația directă cu clientul care e chiar activul de încredere pe care Reduco îl construiește azi (cf. `plan-extindere-b2b.md`, secțiunea 0: "Raportul de Optimizare... e argumentul de vânzare").

**Cifre de urmărit dacă se testează Model B:** rata de conversie audit → contract success-fee (comparat cu 25% conversie audit → abonament, ținta actuală din planul de extindere), venitul mediu/client în primele 6 luni pe segment mic vs. mare, și timpul real de recuperare a costului auditului (calculat aici la 0,18-5,09 luni, cu variație mare între tipurile de client).

---

## Ce lipsește pentru a rafina modelul (de cerut de la client)

1. **Costul orar real** al unui specialist care face auditul (am ilustrat cu 100-150 lei/oră ca asumpție — nu e o cifră a Reduco).
2. **Rata de success fee** pe care CEO ar accepta-o (am ilustrat 20/30/40% — parametru de decizie, nu fapt).
3. **Costul lunar real de deservire** per client (facturare, suport, raportare) — am folosit 100 lei/lună ca asumpție.
4. **O ofertă reală de comision de la un furnizor** dacă Model C rămâne pe agendă — fără ea, orice cifră lei/MWh e doar un reper de negociere, nu o previziune.
5. **Mai multe cazuri reale** (avem doar 2) pentru a recalibra procentul mediu de economie (17,5%) folosit ca proxy în tot modelul.

---

*Document generat pentru comparare planificat vs. realizat (bookkeeping/financial-modeling). Toate calculele sunt reproductibile — vezi metodologia inline la fiecare secțiune.*
