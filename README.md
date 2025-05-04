# Taidesivusto
- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään ja ulos sovelluksesta
- Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan omia julkaisuja, joissa on nimi, kuvaus, kuva sekä tägit
- Käyttäjä näkee sovellukseen lisätyt julkaisut
- Käyttäjä pystyy etsimään julkaisuja julkaisuun liitettyjen tägien perusteella
- Sovelluksessa on käyttäjäsivut, jotka näyttävät käyttäjän nimen, käyttäjän lisäämät julkaisut sekä julkaisujen määrän
- Käyttäjä pystyy valitsemaan julkaisulle yhden tai useamman luokittelun (esim. teema, johon taideteos liittyy ja taideteoksen tyyppi (maalaus, piirrustus...))
- Käyttäjä pystyy jättämään kommentteja muiden tai omaan julkaisuun


## Sovelluksen asennus

Asenna `flask`-kirjasto:

```
$ pip install flask
```

Luo tietokannan taulut:

```
$ sqlite3 database.db < schema.sql
```

Voit käynnistää sovelluksen näin:

```
$ flask run
```
