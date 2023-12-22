# Arkkitehtuuri

## Rakenne

Ohjelman rakenne pyrkii noudattamaan kaksitasoista kerrosarkkitehtuuria. Koodin pakkausrakenne on seuraava:

![1703278837843](https://github.com/labyrine/memory_game/assets/130062658/1cdde779-88dd-47d3-afa2-51fa1bbd0c2b)

Pakkaus ui sisältävät käyttöliitymän koodin, services ja sprites taas sovelluslogiikan koodin. GameLoop luokka huolehtii pelin kulusta sekä käyttäjän syötteiden hakemisesta. Main-funktio käynnistää ohjelman. Pakkaus assets sisältää kuvia muistipelin korttien luontia varten.

## Käyttöliittymä

Käyttöliittymässä on kolme näkymää
- Aloitussivu - Pelaajien määrän valinta
- Pelisivu - Pelin kulku ja pelaajien pisteiden päivittyminen
- Tulossivu - Näyttää lopuksi pelaajien pisteet

Jokaisen näiden piirtämisestä vastaa luokka Render. Näkymät ovat näkyvillä yksi kerrallaan.

## Sovelluslogiikka

Luokka GameLoop huolehtii pelin sovelluslogiikasta enimmäkseen kutsumalla MemoryGameSetUp (services kansio) ja Card (sprites kansio) luokkia. MemoryGameSetUp luo kaikki kortit ja Card luokka sisältää metodit yksittäisten korttien käsittelyyn, kuten kääntämiseen ympäri ja poistamiseen. 

Luokka Card sisältää mm metodit:
- card_chosen()
- flip()
- is_matching()
- delete_found()

Luokka/Pakkauskaavio sovelluslogiikan selventämiseksi

![1703280530534](https://github.com/labyrine/memory_game/assets/130062658/b874bf4f-afc4-45a9-a169-a74a60b3ed3f)

## Päätoiminnot

Päätoiminto olisi korttien valitseminen ja kahden kortin vertailu

## Ohjelman rakenteen heikkoudet
GameLoop luokassa on toisteisuutta sekä jotkin osat sen koodista olisi voinut erottaa toisistaan testaamisen helpottamiseksi. Kuvien lataamisen olisi voinut erottaa muualle, että muu koodi olisi siistimpi.
