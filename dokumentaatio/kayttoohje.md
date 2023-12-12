# Käyttöohje

Lataa projektin viimeisin release valitsemalla Assets-kohdan alta Source_code.

## Ohjelman käynnistäminen

Riippuvuudet asennetaan terminaalissa memory_game kansion sisällä komennolla

```bash
poetry install
```

Pelin käynnistäminen tapahtuu komennolla

```bash
poetry run invoke start
```

## Pelin aloittaminen

- Peli aloitetaan valitsemalla pelaajamäärä väliltä 1-3. Tämä tehdään valitsemalla näppäin 1, 2 tai 3.

## Pelin kulku

- Kukin pelaaja pystyy nostamaan vuorollaan 2 korttia kerrallaan näkyviin. Pisteitä saa löydetyistä pareista.

## Pelin päättyminen

- Peli päättyy, kun kaikki parit on löydetty

## Ohjelman päättäminen

- Pelin ohjelman voi päättää milloin tahansa yläkulman rastista
