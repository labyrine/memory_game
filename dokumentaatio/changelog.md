# Changelog

# Viikko 4
- Käyttäjä näkee 40 muistipelin korttia ensin kuvapuoli alaspäin
- Käyttäjä voi kääntää kortteja näkyviin ja pois näkyvistä
- Lisätty Card-luokka korttien luomista varten
- Testaaminen aloitettu Card-luokalle

# Viikko 5
- Yksi pelaaja voi nostaa kaksi korttia kerrallaan näkyviin
- Jos kortit ovat samat, ne poistuvat pelistä. Jos ne ovat eri, ne kääntyvät takaisin ympäri
- Peli päättyy, kun kaikki kortit on löydetty sulkemalla sovelluksen
- Card-luokan testit korjattu luokkaan tehtyjen muutosten mukaisiksi

# Viikko 6
- Pelaajat voivat valita yhden, kahden tai kolmen pelaajan pelin (Aloitusruutu)
- Pelaajien vuorot vaihtuvat peliruudulla vaihtamalla väriä
- Jokaisella pelaajalla on päivittyvät pisteet peliruudulla
- Rakenteen korjausta: Luokka MemoryGameSetUp huolehtii mm. Card olioiden luomisesta ja GameLoop taas pelin aikaisesta käyttäjän toiminnasta

# Viikko 7
- Rakenteen korjausta: Nyt aloitus ja tulos-sivuja kutsutaan samassa funktiossa kuin pelin silmukkaa, eikä suoraan main-funktiossa
- Kun kaikki parit on löydetty, ruudulle ilmestyy pelin tulokset
