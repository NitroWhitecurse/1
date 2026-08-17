# Verificarea site-ului reduco.ro — ce s-a putut confirma din exterior

**Metodă.** Domeniul `reduco.ro` (inclusiv `www` și `smart`) este respins de proxy-ul de rețea la
nivel de politică — 403 la CONNECT, confirmat de două ori, la interval de ~40 de minute. Ghidul
de depanare al proxy-ului este explicit: un 403 de politică nu se reîncearcă și nu se ocolește.
Nu am încercat rute alternative.

Am reconstruit în schimb site-ul din **indexul public de căutare**, care este un canal separat și
permis. Ce urmează sunt titluri de pagină și descrieri indexate — adică exact ce vede un prospect
în Google înainte de click.

**Limita metodei:** indexul poate fi vechi de zile sau săptămâni și nu arată codul paginii.
Nu am putut verifica: prezența H1-urilor, contrastul culorilor, comportamentul butoanelor,
structura formularelor, viteza. Toate acestea rămân pe auditurile interne, nereconfirmate.

---

## 1. Ce s-a confirmat din auditul intern

| Afirmație din auditul intern | Stare | Dovada |
| --- | --- | --- |
| Titlul paginii principale nu conține „firmă", „IMM" sau „business" | **Confirmat** | Titlul indexat: „Reduco \| Oferte de energie, gaze \| Reclamatii ANRE\| Racordare" |
| `smart.reduco.ro` se prezintă ca și comparator | **Confirmat** | „Reduco - Analiză Facturi Energie și Comparator Furnizori \| Economisește" |
| `/solutii-imm/` există și e orientată pe firme | **Confirmat** | Pagina „Solutii IMM - REDUCO" este indexată |
| Paginile de comparator sunt indexate ca produs principal | **Confirmat** | „Comparator preturi energie electrica", „Comparator preturi gaze naturale" |

## 2. Ce NU s-a putut confirma

- **`/cine-suntem/` nu a apărut în niciun rezultat de căutare.** Poate fi deja ștearsă,
  dezindexată, sau pur și simplu nesurfațată. De verificat direct.
- **Eroarea „Recudo" din meta pe `/abonamente/`** — pagina `/abonamente/` nu a apărut cu
  descrierea ei în rezultate. Rămâne de verificat.
- **Cele ~14 pagini cu prețuri din 2022** (`/juridic-*`, `/casnic-*`, `/oferta-*`) — niciuna
  nu a apărut în căutări. Posibil deja dezindexate, posibil doar nesurfațate. **De verificat în
  Google Search Console**, care e sursa autoritativă, nu căutarea publică.

## 3. Pagini descoperite care nu apar în niciun document intern

Acestea sunt noi. Niciunul dintre auditurile interne, din brief sau din planurile de conținut nu
le menționează.

| URL | Titlu indexat | Ce este |
| --- | --- | --- |
| `/centrale-termice-rate/` | „Centrale termice în rate - 0% Dobândă - **Compară Tot** - Reduco" | Vânzare de centrale termice cu finanțare |
| `/produse/` | „Produse - REDUCO" | Catalog de produse WooCommerce |
| `/livrare/` | „Livrare - REDUCO" | Termeni de livrare — pagină de comerț electronic |
| `/comparator/` | „Comparator - REDUCO" | Un al treilea comparator, peste cele două cunoscute |

Conform descrierilor indexate, `/centrale-termice-rate/` oferă „centrale termice de înaltă
performanță, cu tehnologie de condensare", plata „în până la 36 de rate egale, direct pe factura
de energie sau gaz", consultanță gratuită la alegere, garanție extinsă și „instalare și livrare
rapidă prin echipe autorizate".

Iar `/eficienta-energetica/` nu doar recomandă, ci **implementează**: iluminat LED industrial,
panouri fotovoltaice, sisteme de monitorizare și control.

---

## 4. Problema pe care o creează — și e serioasă

Toată repoziționarea se sprijină pe o singură afirmație, identificată de cercetare drept
**singurul argument pe care concurența nu îl poate copia fără să-și schimbe modelul de business**:

> „Nu suntem furnizor de energie și nu primim comision de la niciun furnizor.
> Suntem plătiți exclusiv de dumneavoastră."

Dar site-ul vinde centrale termice, panouri fotovoltaice, iluminat LED și sisteme de monitorizare,
cu finanțare și instalare prin echipe partenere.

**Dacă Reduco câștigă marjă sau comision din vânzarea acestor echipamente, afirmația de
independență este compromisă material.** Este exact același conflict de interese ca al unui
comparator plătit de furnizori — mutat din zona furnizării de energie în zona furnizării de
echipamente. Un consultant care îți recomandă o centrală și câștigă din vânzarea ei nu e
independent, indiferent cine îl plătește pentru consultanță.

Nu am date despre modelul de remunerare al acestei linii. Sunt trei posibilități:

1. **Reduco câștigă comision din vânzări.** Atunci afirmația de independență, în forma actuală,
   este falsă și nu poate fi publicată așa. Trebuie reformulată strict: *„nu primim comision de
   la niciun furnizor **de energie**"* — și trebuie declarat separat, vizibil, modelul de venit
   din echipamente.
2. **Reduco nu câștigă nimic** — e doar un serviciu de intermediere fără marjă. Atunci trebuie
   spus explicit, pentru că altfel arată exact ca varianta 1.
3. **Linia de produse e reziduală**, rămasă de la modelul vechi de comparator generalist.
   Atunci decizia corectă e să dispară odată cu repoziționarea.

**Aceasta nu e o observație cosmetică.** Un director financiar sceptic — exact publicul-țintă
definit — găsește `/centrale-termice-rate/` la un click distanță de pagina despre independență.
Un competitor o găsește și mai repede. Argumentul cel mai puternic al repoziționării devine,
în mâinile lui, dovada opusă.

**Decizie necesară de la tine, înainte de a publica orice text despre independență.**

## 5. Brandul vechi e mai prezent decât se credea

Auditul intern spunea că „Comparatot" a rămas doar în textul de pe `/cine-suntem/`.

În realitate, **„Compară Tot" apare în titlul indexat al paginii `/centrale-termice-rate/`** —
adică în ce vede utilizatorul în Google, nu îngropat în corpul unei pagini.

Mai mult: `comparatot.ro` este un comparator **activ**, care compară „energie, gaze, telecom,
fotovoltaice, centrale termice și aer condiționat". Suprapunerea cu linia de produse a Reduco
nu e parțială — e aproape totală. Cercetarea de piață îl tratase ca pe un simplu risc de confuzie
de nume. Este mai mult decât atât: e un concurent direct pe exact aceleași categorii de produse.

**Acțiune:** căutarea după „Comparatot" și „Compară Tot" trebuie făcută pe tot site-ul, inclusiv
în titluri, meta descrieri, alt-texte și fișiere media — nu doar pe `/cine-suntem/`.

## 6. O afirmație de risc pe `/solutii-imm/`

Pagina afirmă, conform descrierii indexate, că **„economiile medii sunt între 10% și 55%,
în funcție de domeniu și de măsurile implementate"**.

Un interval de la 10% la 55% nu este o cifră, este o plajă atât de largă încât nu comunică nimic
verificabil. Iar 55% este o afirmație extraordinară, care atrage întrebarea „la ce client, în ce
condiții, față de ce bază de comparație?"

Contrazice direct principiul de ton stabilit în platforma de brand — *cifre exacte, nu adjective;
fără afirmații neverificabile*. Într-o poziționare construită pe credibilitate în fața unui CFO,
o astfel de afirmație lucrează împotriva ta.

**Recomandare:** se înlocuiește cu economii reale, documentate, pe cazuri concrete — cifrele din
auditurile existente (3.803 lei/lună la un punct de consum pe medie tensiune) sunt mult mai
convingătoare tocmai pentru că sunt specifice.

## 7. Ce se schimbă în plan

| Document | Modificare |
| --- | --- |
| `00-brief-context.md` | Adăugată linia de produse ca serviciu nedocumentat anterior |
| `03-platforma-brand.md` | Afirmația de independență devine condiționată de clarificarea modelului de venit din echipamente |
| `06-copy-pagini.md` | Textele despre independență **nu se publică** până la decizia de la punctul 4 |
| `07-plan-executiv.md` | Adăugat risc critic + decizie necesară |
| Săptămânile 1–2 | Se adaugă: căutare „Comparatot"/„Compară Tot" pe tot site-ul; corectarea afirmației de 10–55% |

## 8. Ce rămâne de verificat direct pe site

Lista de mai jos necesită acces la site sau la Google Search Console. Nu poate fi rezolvată din exterior.

1. Modelul de venit al liniei de produse — **prioritatea 1**.
2. Dacă `/cine-suntem/` mai există.
3. Descrierea meta de pe `/abonamente/` și eroarea „Recudo".
4. Lista reală a paginilor cu prețuri din 2022, din Search Console.
5. Dacă H1-urile lipsesc într-adevăr pe tot site-ul.
6. Câte pagini indexate există în total, și câte sunt orfane.
7. Dacă `/comparator/`, `/produse/` și `/livrare/` sunt active sau reziduale.
8. Toate afirmațiile de contrast, viteză și formulare din auditul intern.
