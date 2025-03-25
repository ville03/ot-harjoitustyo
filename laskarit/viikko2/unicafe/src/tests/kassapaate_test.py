import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_konstruktori_asettaa_syotyjen_maaran_oikein_edullisesti(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_konstruktori_asettaa_syotyjen_maaran_oikein_maukkaasti(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kateisella_toimii_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)
    
    def test_syo_edullisesti_kateisella_kasvattaa_syotyjen_edullisten_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kateisella_ei_toimi_vajaalla_saldolla(self):
        self.kassapaate.syo_edullisesti_kateisella(239)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_syo_edullisesti_kateisella_ei_kasvata_syotyjen_edullisten_maaraa_vajaalla_saldolla(self):
        self.kassapaate.syo_edullisesti_kateisella(239)
        
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kateisella_toimii_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)

    def test_syo_maukkaasti_kateisella_kasvattaa_syotyjen_maukkaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kateisella_ei_toimi_vajaalla_saldolla(self):
        self.kassapaate.syo_maukkaasti_kateisella(239)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_syo_maukkaasti_kateisella_ei_kasvata_syotyjen_maukkaiden_maaraa_vajaalla_saldolla(self):
        self.kassapaate.syo_maukkaasti_kateisella(239)
        
        self.assertEqual(self.kassapaate.edulliset, 0)
    #
    def test_syo_edullisesti_kortilla_toimii_oikein(self):
        kortti = Maksukortti(240)
        palaute = self.kassapaate.syo_edullisesti_kortilla(kortti)
        
        self.assertEqual(palaute, True)
    
    def test_syo_edullisesti_kortilla_vahentaa_kortin_saldoa(self):
        kortti = Maksukortti(240)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        
        self.assertEqual(kortti.saldo_euroina(), 0.0)
    
    def test_syo_edullisesti_kortilla_kasvattaa_syotyjen_edullisten_maaraa(self):
        kortti = Maksukortti(240)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kortilla_ei_toimi_vajaalla_saldolla(self):
        kortti = Maksukortti(239)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_syo_edullisesti_kortilla_ei_kasvata_syotyjen_edullisten_maaraa_vajaalla_saldolla(self):
        kortti = Maksukortti(239)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kortilla_toimii_oikein(self):
        kortti = Maksukortti(400)
        palaute = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        
        self.assertEqual(palaute, True)
    
    def test_syo_maukkaasti_kortilla_vahentaa_kortin_saldoa(self):
        kortti = Maksukortti(400)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        
        self.assertEqual(kortti.saldo_euroina(), 0.0)

    def test_syo_maukkaasti_kortilla_kasvattaa_syotyjen_maukkaiden_maaraa(self):
        kortti = Maksukortti(400)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kortilla_ei_toimi_vajaalla_saldolla(self):
        kortti = Maksukortti(399)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_syo_maukkaasti_kortilla_ei_kasvata_syotyjen_maukkaiden_maaraa_vajaalla_saldolla(self):
        kortti = Maksukortti(399)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_lataa_rahaa_kortille_toimii_oikein(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, 100)
        self.assertEqual(kortti.saldo_euroina(), 11.0)

    def test_lataa_rahaa_kortille_kassan_saldo_kasvaa(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1001.0)

    def test_lataa_rahaa_kortille_ei_toimi_negatiivisella_summalla(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, -100)
        self.assertEqual(kortti.saldo_euroina(), 10.0)