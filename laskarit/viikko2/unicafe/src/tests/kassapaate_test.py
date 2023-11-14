import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_kassapaate_aloitus_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_maksu_riittaa_kassa_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(260)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(260), 20)

    def test_maukas_maksu_riittaa_kassa_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(450)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(450), 50)

    def test_edullinen_rahaa_liian_vahan_kassa(self):
        self.kassapaate.syo_edullisesti_kateisella(220)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(220), 220)

    def test_maukas_rahaa_liian_vahan_kassa(self):
        self.kassapaate.syo_maukkaasti_kateisella(380)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(380), 380)

    def test_edullinen_rahaa_tarpeeksi_kortti(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.maksukortti.saldo_euroina(), 7.6)

    def test_maukas_rahaa_tarpeeksi_kortti(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.maksukortti.saldo_euroina(), 6)

    def test_edullinen_rahaa_ei_tarpeeksi_kortti(self):
        self.maksukortti = Maksukortti(220)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.maksukortti.saldo_euroina(), 2.2)

    def test_maukas_rahaa_ei_tarpeeksi_kortti(self):
        self.maksukortti = Maksukortti(380)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.maksukortti.saldo_euroina(), 3.8)

    def test_rahan_lataus_kortille_povitiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 700)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1007)
        self.assertEqual(self.maksukortti.saldo_euroina(), 17)

    def test_rahan_lataus_kortille_negatiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -700)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

