# Reduco — status plan 100M Leads

Actualizează acest fișier la fiecare revizuire (săptămânală rapid, de fază complet). Nu șterge log-ul —
adaugă la el, ca să existe istoric de decizii.

## Faza curentă

- **Fază**: 0 — Decizie și linie de bază (blocată — vezi log-ul de decizii, revizuirea din 2026-09-25)
- **Zi de plan**: 30 (ziua 1 = data de start declarată mai jos)
- **Data de start (ziua 1)**: 2026-08-27

## Faza 0 — Decizii de scris (o singură dată)

- **Canal prioritar (90 de zile)**: [conținut LinkedIn / warm outreach] — recomandarea din plan: **conținut**
- **Canal secundar (nivel minim, fără resurse suplimentare)**: [celălalt canal]
- **LTGP:CAC de bază calculat**: vezi `ltgp-cac.md` — rezultat: [—]
- **Tabel de măsurare pornit**: `tracking.csv` — [da/nu]

## Log decizii de fază

Format: dată — fază — decizie (continui / ajustez / trec la faza următoare) — motiv pe scurt.

- **2026-09-25 — Revizuire ziua 30 (Faza 1→2) — nu se poate trage o concluzie de fază, rămân în Faza 0.**
  Motiv: nicio decizie din Faza 0 nu a fost scrisă (canal prioritar/secundar nedeclarat, LTGP:CAC
  necalculat), `tracking.csv` e complet gol (0 rânduri completate în 4 revizuiri săptămânale
  consecutive), și niciuna dintre cele 14 postări generate automat (`content/content-log.csv`) nu are
  `status_aprobare` = `postat` sau `data_postare` completată. Nu pot spune dacă s-a postat efectiv ceva
  pe LinkedIn în aceste 30 de zile — ceea ce e mai grav decât "am postat și n-am avut leaduri" (semnalul
  de alarmă explicit din cadru). Rutina de generare a produs conținut constant (14 draft-uri, 3x/săptămână,
  toate cele 5 pilonuri de business acoperite de 2-3 ori), deci partea automatizabilă a funcționat; partea
  care depinde de Marian (decizia de canal, postarea efectivă, completarea tracking-ului) nu a avansat.
  Decizie: rămân în Faza 0 până la răspuns. Nu trec artificial la Faza 2 fără date reale de citit.

  **Am nevoie de răspuns direct la:**
  1. S-a postat vreunul din cele 14 draft-uri pe LinkedIn? Dacă da, care și când?
  2. Confirmi canalul prioritar (conținut LinkedIn, cum recomandă planul) și cel secundar?
  3. Vrei să reduc ritmul rutinei de generare (3x/săptămână) până se recuperează din backlog, sau să
     continue neschimbată?
  4. LTGP:CAC — ai cifrele reale (abonament anual, comisioane switch, durata relației, cost livrare) ca
     să rulez `ltgp-cac.sh`?

## Semnale de alarmă de verificat la fiecare revizuire

- [ ] Rată de răspuns sub pragul normal pentru canal
- [ ] O lună întreagă postat, zero leaduri
- [ ] Engagement prezent, zero conversații private
- [ ] Magnetul de lead (checklist factură) generează cereri constante?
- [ ] Cererile de recomandare din portofoliul existent: câte făcute / câte au dus la conversație reală?
