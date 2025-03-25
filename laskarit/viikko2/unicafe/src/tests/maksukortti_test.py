import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_str_function(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    #def test_konstruktori_ei_aseta_saldoa_negatiiviseksi(self):
    #    maksukortti = Maksukortti(-1000)

    #    self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 0.00 euroa")

    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(2500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 35.0)

    #def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
    #    self.maksukortti.lataa_rahaa(-100)

    #    self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_kortilta_voi_ottaa_rahaa(self):
        self.maksukortti.ota_rahaa(1000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 0.0)

    def test_kortilta_ei_voi_ottaa_rahaa_saldoa_enempaa(self):
        self.maksukortti.ota_rahaa(2000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_kortilta_rahaa_ottaessa_funktio_palauttaa_True(self):
        palaute = self.maksukortti.ota_rahaa(100)
        self.assertEqual(palaute, True)

    def test_kortilta_rahan_otton_hyljettya_funktio_palauttaa_False(self):
        palaute = self.maksukortti.ota_rahaa(2000)
        self.assertEqual(palaute, False)