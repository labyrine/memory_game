import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def saldo_euroina(self):
        return self.saldo / 100

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(2500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 35.0)

    def test_saldo_vahenee_oikein_kun_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 5.0)

    def test_saldo_ei_muutu_kun_ei_ole_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(2500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_palauta_true_rahojen_riittaessa(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 5.0)
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)
    
    def test_palauta_false_kun_rahat_ei_riita(self):
        self.maksukortti.ota_rahaa(2500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
        self.assertEqual(self.maksukortti.ota_rahaa(2500), False)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")