import unittest
import script

class prueba(unittest.TestCase):
  def test_summarize_contents(self):
    
      s = summarize_contents("data/AF323668.gbk")
      self.assertEqual("file: AF323668.gbk\npath: C:\Users\MUDTL\Documents\GitHub\Ejercicio-biopython\data\AF323668.gbk")

      s = summarize_contents("data/ls_orchid.fasta")
      self.assertEqual("file: ls_orchid.fasta\npath: C:\Users\MUDTL\Documents\GitHub\Ejercicio-biopython\data\ls_orchid.fasta" )
      
      s = summarize_contents("data/ls_orchid.gbk")
      self.assertEqual("file: ls_orchid.gbk\npath: C:\Users\MUDTL\Documents\GitHub\Ejercicio-biopython\data\ls_orchid.gbk")
      
      s = summarize_contents("data/m_cold.fasta")
      self.assertEqual("file: m_cold.fasta\npath: C:\Users\MUDTL\Documents\GitHub\Ejercicio-biopython\data\m_cold.fasta ")
      
      s = summarize_contents("data/NC_002703.gbk")
      self.assertEqual("file: NC_002703.gbk\npath: C:\Users\MUDTL\Documents\GitHub\Ejercicio-biopython\data\NC_002703.gbk")
      
      s = summarize_contents("data/opuntia.fasta")
      self.assertEqual("file: opuntia.fasta\npath: C:\Users\MUDTL\Documents\GitHub\Ejercicio-biopython\data\opuntia.fasta" )

 #prueba de concatenación y complemento //////////////////////////////////////////////////////////////////////////////////////////////     
      
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


      
      
#prueba de extract.sequences///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class preubaext_sec(unittest.TestCase):
  def test_extract_sequences(self):
    archivo = "C:\Users\MUDTL\Downloads\sequences.fasta"
    c = Scrpt.extract_sequences(archivo)
    self.assertEqual(c)
    
if__name__ == "__main__":
  unittest.main()
