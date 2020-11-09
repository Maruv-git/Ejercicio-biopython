import Bio
from Bio import SeqIO
from bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import os


filename =  os.path.abspath("data/ls_orchid.gbk")

def summarize_contents(filename):
	lta = []
	lta = os.path.split(filename)
	cadena = " "
	cadena = ("\nfile: "+ lta[1] + "\npath: " + lta[0])
	File_Extension = []
	File_Extension = os.path.splitext(filename)
	if(File_Extension[1]==".gbk"):
		type_file="GenBank"
	else:
		type_file="Fasta"
		pass
	rgstro = list(SeqIO.parse(filename, type_file))
	cadena += ("\nnum_rgstro: " + str(len(rgstro)))
	cadena += ("\nrecord(s): ")
	for seq_record in SeqIO.parse(filename, type_file):
		cadena += ("\n-ID: " + str(seq_record.id))
		cadena += ("\nName: " + seq_record.name)
		cadena += ("\nDescription: " + str(seq_record.description))
		return cadena
		if __name__ == "__main__":
			R = summarize_contents(filename)
			print(R)
#SEGUNDO EJERCICIO////////////////////////////////////////////////////////////

def concatenate_get_reverse_of_complement(s1,s2):
		scon = Seq(s1 + s2)
		return scon.reverse_complement()
		creversa = concatenaate_and_get_reverse_of_complement(sec1, sec2)
		if __name__ == "__main__":
			print (creversa)


