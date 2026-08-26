# LTGP:CAC de bază — Reduco

Reper aproximativ, nu contabilitate exactă. Scop: să existe un număr de care să te lovești când te
întrebi dacă merită testate reclame plătite (Faza 4).

## Formula

```
Valoare anuală client   = abonament anual mediu + comisioane switch estimate/an
Durata medie relație    = ani estimați cât rămâne un client (churn invers)
LTV brut                = Valoare anuală client × Durata medie relație
Cost livrare serviciu   = cost anual estimat de livrare per client (timp + unelte + eventuali colaboratori)
LTGP (Lifetime Gross Profit) = LTV brut − (Cost livrare serviciu × Durata medie relație)

CAC = cost total canal (timp valorizat + bani) ÷ clienți noi obținuți prin canal, într-o perioadă

Raport țintă (cadru): LTGP:CAC ≥ 3:1
```

## Calculator rapid

Rulează `ltgp-cac.sh` cu valorile tale (Lei):

```bash
./ltgp-cac.sh <abonament_anual> <comisioane_switch_an> <ani_durata_relatie> <cost_livrare_an> <cac>
```

Exemplu (valori ilustrative, înlocuiește cu ale tale):

```bash
./ltgp-cac.sh 3600 500 3 800 900
```

## Rezultat curent

- Data calculului: [—]
- Input-uri folosite: [—]
- LTGP: [—]
- CAC: [—]
- Raport LTGP:CAC: [—]
