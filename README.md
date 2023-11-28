# Muistipeli

Sovellus on muistipeli, jota voi pelata yksi tai useampi henkilö.

Tällä hetkellä sovelluksessa toimii korttien kääntäminen näkyviin ja pois näkyvistä.

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/labyrine/memory_game/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/labyrine/memory_game/blob/main/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/labyrine/memory_game/blob/main/dokumentaatio/changelog.md)

## Asentaminen

1. Riippuvuudet asennetaan terminaalissa memory_game kansion sisällä komennolla

```bash
poetry install
```

2. Pelin käynnistäminen tapahtuu komennolla

```bash
poetry run invoke start
```
## Komentorivitoiminnot

### Pelin suorittaminen

```bash
poetry run invoke start
```

### Testaaminen

```bash
poetry run invoke test
```

### Testikattavuus

```bash
poetry run invoke coverage-report
```

Raportti tulee generoitumaan _htmlcov_-hakemistoon.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemien tarkistusten suorittaminen

```bash
poetry run invoke lint
```
