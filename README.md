# Taidesivusto
IDEA:
- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen
- Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan omia taideteoksia sisältäviä julkaisuja
- Käyttäjä näkee sovellukseen lisätyt julkaisut
- Käyttäjä pystyy etsimään julkaisuja hakusanalla julkaisun teeman perusteella
- Sovelluksessa on käyttäjäsivut, jotka näyttävät tilastoja ja käyttäjän lisäämät julkaisut
- Käyttäjä pystyy valitsemaan julkaisulle yhden tai useamman luokittelun (esim. teema, johon taideteos liittyy ja taideteoksen tyyppi (maalaus, piirrustus...))
- Käyttäjä pystyy jättämään kommentteja muiden julkaisuihin

TEHTY:
- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen
- Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan omia julkaisuja (ei vielä kuvanlisäys-ominaisuutta)
- Käyttäjä näkee sovellukseen lisätyt julkaisut
- Käyttäjä pystyy etsimään julkaisuja hakusanalla julkaisun kuvauksen ja nimen perusteella
- Sovelluksessa on käyttäjäsivut, jotka näyttävät käyttäjän lisäämät julkaisut
- Käyttäjä pystyy valitsemaan julkaisulle yhden tai useamman luokittelun (esim. teema, johon taideteos liittyy ja taideteoksen tyyppi (maalaus, piirrustus...))
- Käyttäjä pystyy jättämään kommentteja muiden julkaisuihin


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
