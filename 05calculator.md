# Kalkulačka (Calculator)

**Cíl**:
Vypočítat příklad složený z několika matematických operací.

1. Uživatel zadá první celé číslo (_Zadej číslo_).
2. Uživatel vybere jednu matematickou operaci zadáním příslušného symbolu (_Vyber operaci_):
    - `+` (sčítání)
    - `-` (odčítání)
    - `*` (násobení)
    - `/` (dělení)
3. Uživatel zadá druhé celé číslo (_Zadej číslo_).
4. Program provede vybranou matematickou operaci a vypíše do konzole celý příklad včetně výsledku:
    - `1 + 2 = 3`
    - `3 - 2 = 1`
5. Program pokračuje znovu od bodu 2. Výsledek předchozí matematické operace se stane prvním číslem následující matematické operace.

- Pokud uživatel místo operace zadá symbol `=`, program se ukončí.
- Pokud uživatel zadá neplatnou operaci, program vypíše chybu a ukončí se.

## Příklad

```
Zadej číslo: 12
Vyber operaci: +
Zadej číslo: 34

12 + 34 = 46

Vyber operaci: -
Zadej číslo: 5

46 - 5 = 39

Vyber operaci: *
Zadej číslo: 6

39 * 6 = 234

Vyber oparaci: = 
```