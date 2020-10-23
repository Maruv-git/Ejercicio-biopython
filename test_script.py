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
