# Reduco — 100M Leads: sistem de execuție

Automatizarea planului "Reduco — 100M Leads" din discuția inițială. Nu conține agenți noi — folosește
agenții deja existenți în `.claude/agents/` (în special `content-marketing`, `social-media-manager`,
`sales-outreach`, `growth-analytics`) plus skill-ul `reduco-linkedin`, orchestrați în jurul fișierelor
din acest folder.

## Ce automatizează

1. **`plan-status.md`** — starea curentă a planului: ce fază ești, decizia din Faza 0, log-ul deciziilor
   de la fiecare revizuire de 30 de zile. Sursa unică de adevăr — actualizează-l, nu re-scrie planul.
2. **`tracking.csv`** — tabelul săptămânal cerut în Faza 0 (leaduri conținut, leaduri warm outreach,
   conversații reale, clienți, timp investit). Deschide-l în Sheets/Excel dacă preferi vizual, dar
   originalul rămâne aici ca să poată fi citit și actualizat programatic.
3. **`ltgp-cac.md`** — calculatorul LTGP:CAC de bază din Faza 0, cu formula și un mic script bash
   (`ltgp-cac.sh`) ca să nu recalculezi manual de fiecare dată.
4. **`lead-magnet.md`** — checklist-ul de verificare a facturii, tratat ca magnet de sine stătător
   (Faza 1), cu variantele de titlu testate și rezultatele lor.
5. Rutine programate (vezi mai jos) care te împing să completezi `tracking.csv` săptămânal și să faci
   revizuirea de fază la zilele 30/60/90, în loc să depindă de memorie.

## Rutine active

| Rutină | Cadență | Ce face |
|---|---|---|
| Revizuire săptămânală | luni, 07:00 UTC | Trimite un mesaj în această sesiune cerând completarea `tracking.csv` pentru săptămâna încheiată și un semnal rapid (verde/galben/roșu) pe rata de răspuns |
| Revizuire Faza 1→2 | ziua 30 (2026-09-25) | Cere citirea `tracking.csv`, verificarea semnalelor de alarmă din cadru, actualizarea `plan-status.md` cu decizia explicită |
| Revizuire Faza 2→3 | ziua 60 (2026-10-25) | Idem, plus verificarea rezultatului cererilor de recomandare din portofoliul existent |
| Revizuire Faza 3→4 | ziua 90 (2026-11-24) | Decizia More Better New vs. canal nou, plus pregătirea Faza 4 (Lead Getters, parteneriate) |

Rutinele sunt gestionate prin `create_trigger`/`update_trigger`/`delete_trigger` (server-side, nu depind
de acest container). Le poți lista oricând cu `list_triggers`.

## Fluxul practic

- **Zilnic**: cei 100 de minute de conținut se fac cu skill-ul `reduco-linkedin` (postare, comentarii,
  DM-uri). Nu e automatizat de o rutină separată — e disciplină de execuție, nu ceva ce se poate delega.
- **Săptămânal**: rutina de luni te întreabă direct — completezi rândul din `tracking.csv`.
- **La fiecare 30 de zile**: rutina de fază citește `tracking.csv`, aplică testele din cadru (rata de
  răspuns, "o lună fără lead", engagement fără conversații) și scrie decizia în `plan-status.md`.
- **Agenți de invocat pe fază**:
  - Faza 1: `content-marketing` / `social-media-manager` pentru variantele de titlu ale magnetului.
  - Faza 2: `growth-analytics` pentru citirea datelor din `tracking.csv`.
  - Faza 4: `sales-outreach` pentru structurarea parteneriatelor cu contabili/consultanți.
