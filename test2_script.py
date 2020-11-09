import unittest
import script
import os

class prueban2(unittest.TestCase):
    def test_concatenate_get_reverse_of_complement(self):


        Ej1 = Sec("ATAGACATAGAAATAGATACATAGAT")
        Cadrev = concatenate_and_get_reverse_of_complement("ATCGATAGCTAGATCGATATAG", "TCAGATAGCGGGTACAGTGTGTT")
        self.assertEqual(Ej1,Cadrev)

        Ej2 = Sec("ATACTAGATAGATGGGGATCACTGAC")
        Cadrev = concatenate_and_get_reverse_of_complement("atgacagatagacacaggctcgatgatcggtgatc", "ggtagacagatttgatcggta")
        self. assertEqual(Ej2,Cadrev)

        Ej3 = Sec("ATCGCTAGTagatcTgTAGAtGtG")
        Cadrev = concatenate_and_get_reverse_of_complement("ATGCGATgTCgGtaATg", "AAATgCcGATAGtGcGtG")
        self.assertEqual(Ej3,Cadrev)

        Ej4 = Sec("AGGCTCGTGATAgTgTgTgAAcGT")
        Cadrev = concatenate_and_get_reverse_of_complement("cagatagacgtcgctcgctgggaagtcgt", "gatagatacacagatagaagata")
        self.assertEqual(Ej4,Cadrev)

        Ej5 = Sec("agatcagatctgcgctgagagcccacagagagtatttttt")
        Cadrev = concatenate_and_get_reverse_of_complement("CGATAGCTGTAGCGTAGCGTA", "gtcgtgtcgctagcgatcgataaa")
        self.assertEqual(Ej5,Cadrev)
