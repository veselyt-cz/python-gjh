# Šifry (Codes)

**Cíl**:
Šifrovat nebo dešifrovat zprávu předem známým klíčem.

1. Uživatel vybere, jestli chce šifrovat nebo dešifrovat.
    - `E` = šifrování (encryption)
    - `D` = dešifrování (decryption)
2. Uživatel zadá klíč. Formát klíče zároveň určí typ šifry.
    - Celé číslo v rozsahu od 1 do 25 je klíčem pro _Caesarovu šifru_.
    - Řetězec s délkou alespoň 5 znaků je klíčem pro _Vigenerovu šifru_.
3. Uživatel zadá zprávu, kterou chce šifrovat nebo dešifrovat.
4. Program vypíše šifrovanou nebo dešifrovanou zprávu.

## Caesarova šifra

Předem si domluvíme __klíč__ – číslo mezi 1 a 25.

Při __šifrování__ posouváme písmena v abecedě o počet písmen daný klíčem. Pokud se v abecedě dostaneme za Z, vrátíme se na začátek abecedy a pokračujeme zase od A.

Při __dešifrování__ posouváme písmena v abecedě o stejný počet písmen v opačném směru.

Více informací najdete na [Wikipedii](https://cs.wikipedia.org/wiki/Caesarova_šifra).

### Příklad

Klíč = `3`

```
SRAZ VE TRI ZA SKOLOU
VUDC YH WUL CD VNRORX
```

## Vigenèrova šifra

Předem si domluvíme __klíč__ – slovo nebo větu. Na jedno písmeno zprávy připadá jedno písmeno klíče. Pokud je klíč kratší než zpráva, kterou chceme poslat, klíč se opakuje několikrát za sebou.

Budeme používat [Vigenèrův čtverec](https://commons.wikimedia.org/wiki/File:Vigenère_square.svg).

Při __šifrování__ si najdeme ten řádek, kde je v prvním sloupci písmeno, které chceme šifrovat, a ten sloupec, kde je v prvním řádku odpovídající písmeno klíče. Z tabulky vybereme písmeno, které je v průsečíku vybraného řádku a sloupce.

Při __dešifrování__ si najdeme ten sloupec, kde je v prvním řádku odpovídající písmeno klíče, a v tomto sloupci hledáme písmeno, které chceme dešifrovat. Z řádku, kde ho najdeme, vezmeme písmeno z prvního sloupce. To je dešifrované písmeno.

Více informací najdete na [Wikipedii](https://cs.wikipedia.org/wiki/Vigenèrova_šifra).

### Příklad

Klíč = `PEJSEK`

```
POKLAD V ZAPADNI VEZI
ESTDEN K DJHENCM EWDS
```