# Známky (Grades)

**Cíl**:
Určit vážený průměr známek z jednoho předmětu.

1. Uživatel zadá počet známek, které dosud obdržel ve vybraném předmětu (_Kolik máš známek?_).
    - Program zkontroluje, že uživatel zadal kladné celé číslo. V opačném případě se zeptá znovu.
2. Uživatel zadá hodnotu první známky z vybraného předmětu (_Zadej 1. známku:_).
    - Program zkontroluje, že uživatel zadal celé číslo v rozsahu 1-5. V opačném případě se zeptá znovu.
3. Uživatel zadá váhu první známky z vybraného předmětu (_Zadej váhu 1. známky:_).
    - Program zkontroluje, že uživatel zadal celé číslo v rozsahu 1-3. V opačném případě se zeptá znovu.
4. Program pokračuje znovu od bodu 2, dokud uživatel nezadá všechny známky podle bodu 1.
5. Program vypočte vážený průměr zadaných známek a vypíše ho do konzole s přesností na dvě desetinná místa.
6. Program určí známku na vysvědčení zaokrouhlením váženého průměru a vypíše ji do konzole.

*Bonus*:

1. Uživatel zadá váhu příští známky z vybraného předmětu (_Zadej váhu příští známky:_).
2. Program vypočte vážený průměr pro všechny možné získané známky a vypíše ho do konzole s přesností na dvě desetinná místa.

## Příklad

```
Kolik máš známek? 3

Zadej 1. známku: 2
Zadej váhu 1. známky: 2

Zadej 2. známku: 0
To není platná známka!
Zadej 2. známku: 1
Zadej váhu 2. známky: 3

Zadej 3. známku: 3
Zadej váhu 3. známky: +
To není platná váha!
Zadej váhu 3. známky: 1

Vážený průměr: 1.67
Známka na vysvědčení: 2
```