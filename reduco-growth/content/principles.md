# Sistem de generare conținut — psihologie + metoda Hormozi

Nu înlocuiește skill-ul `reduco-linkedin` (acela dă regulile de scriere: hook, ton, CTA, lungime).
Acest fișier dă **structura de gândire din spatele fiecărei postări** — ce declanșator psihologic și ce
pilon Hormozi alegi înainte să scrii, ca generarea să fie sistematică, nu inspirație aleatorie.

## Structura Hormozi: Hook — Retain — Reward

Din *$100M Leads*. Fiecare postare trece prin toate trei, în ordine:

1. **Hook** — oprește scroll-ul. Regulile din `reduco-linkedin` (simptom recunoscut, sub 14 cuvinte,
   fără meta-comunicare) sunt implementarea Hook-ului.
2. **Retain** — ține cititorul până la capăt. Se face prin curiozitate deschisă devreme și închisă
   târziu ("două rânduri de pe factură — care sunt, spun mai jos"), poveste cu tensiune (o problemă
   reală, nu rezolvată din prima linie), sau structură numerotată care promite un final.
3. **Reward** — livrează valoarea promisă în Hook, apoi cere ceva mic (CTA-ul din `reduco-linkedin`).
   Recompensa vine înaintea cererii, niciodată invers — asta e regula "Give, Give, Give, Ask" a lui
   Hormozi: postarea trebuie să merite citită chiar dacă cititorul nu dă niciodată click.

## Declanșatori psihologici — alege UNUL dominant per postare

Nu combina mai mult de unul-două, altfel postarea devine confuză. Fiecare are un tipar corespunzător
deja definit în `reduco-linkedin`:

| Declanșator | Ce face | Tipar `reduco-linkedin` |
|---|---|---|
| **Curiozitate (information gap)** | Deschide un gol pe care creierul vrea să-l închidă | Detaliul ignorat |
| **Dovadă socială** | "Alții ca tine au avut aceeași problemă" | Cazul concret (anonimizat) |
| **Pattern interrupt** | Contrazice o presupunere comună, forțează atenție | Contra-intuitivul |
| **Aversiune la pierdere** | Frica de a pierde bani/timp cântărește mai mult decât câștigul | Greșeala comună / cost ascuns |
| **Autoritate** | Explici mecanismul tehnic corect, câștigi încredere | Termen tehnic explicat din mers |
| **Reciprocitate** | Dai ceva util gratuit (checklist, explicație) înainte de a cere ceva | Magnetul de lead (`lead-magnet.md`) |

## Pilonii de conținut (rotație pe cele 5 linii de business Reduco)

Rotești subiectul, nu doar declanșatorul, ca să nu suni ca un singur mesaj repetat:

1. Audit factură + schimbare furnizor
2. Racordare și avize ATR
3. Litigii și reclamații ANRE
4. Prosumatori și fonduri nerambursabile
5. Abonament persoane juridice (produsul recurent)

## Cum se combină (rotația din `topics.csv`)

Fiecare rând din `topics.csv` e o combinație fixă: `pilon_serviciu × declanșator_psihologic`. Rutina de
generare ia rândul următor nefolosit, nu alege liber — asta garantează varietate reală în loc de
repetarea aceluiași unghi ("cazul concret") de fiecare dată pentru că e cel mai ușor de scris.

## Ce NU se automatizează

- Postarea efectivă pe LinkedIn — nu există conector de postare; draftul se salvează în
  `content/drafts/` și tu copiezi manual, după ce citești și aprobi.
- Cifrele concrete — dacă subiectul cere o cifră reală (client anonimizat, sumă recuperată), rămâne
  placeholder `[X]` până o completezi, exact cum cere `reduco-linkedin`.
