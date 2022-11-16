# Domy (Houses)

**Cíl**:
Postavit v konzoli sídliště se zadanými parametry.

1. Uživatel zadá počet domů, počet pater každého domu a počet oken na každém patře.
    - Pokud některá hodnota není kladné celé číslo, program vypíše chybu a skončí.
2. Program vypíše do konzole řadu domů se střechou podle následujících pravidel:
    - Dům má tvar obdélníku a skládá se z několika pater. Počet pater je zadán uživatelem.
    - Každé patro domu se skládá z oken `#` a ohraničení `|`. Počet oken je zadán uživatelem.
    - Střecha má tvar lichoběžníku a skládá se z několika vrstev. Počet vrstev je dán polovinou počtu oken.
    - Každá vrstva střechy se skládá z tašek `U` a ohraničení `\/`. Počet tašek je dán tvarem střechy.
    - Dům a střecha jsou ohraničeny horizontální dvojitou deskou `=`.

## Příklad

```
Počet domů: 3
Počet pater: 5
Počet oken: 7

    =========         =========         =========    
   / UUUUUUU \       / UUUUUUU \       / UUUUUUU \   
  / UUUUUUUUU \     / UUUUUUUUU \     / UUUUUUUUU \  
 / UUUUUUUUUUU \   / UUUUUUUUUUU \   / UUUUUUUUUUU \ 
/ UUUUUUUUUUUUU \ / UUUUUUUUUUUUU \ / UUUUUUUUUUUUU \
================= ================= =================
| # # # # # # # | | # # # # # # # | | # # # # # # # |
| # # # # # # # | | # # # # # # # | | # # # # # # # |
| # # # # # # # | | # # # # # # # | | # # # # # # # |
| # # # # # # # | | # # # # # # # | | # # # # # # # |
| # # # # # # # | | # # # # # # # | | # # # # # # # |
================= ================= =================
```