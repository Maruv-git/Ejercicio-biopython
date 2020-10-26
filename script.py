ffrom Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os

# Cambiar la dirección del archivo .gbk que desee leer
filename =  "/mnt/c/Users/MUDTL/Docuemnts/GitHub/Ejercicio-biopython/ls_orchid.gbk"

def summarize_contents(filename):
	lta = []
	lta = os.path.split(filename)
	cadena = " "
	cadena = ("\nfile: "+ lta[1] + "\npath: " + lta[0])
	File_Extension = []
	File_Extension = os.path.splitext(filename)
//////////////////////////////////////////////////////////////////////////////////	
	if(File_Extension[1]==".gbk"):
		type_file="GenBank"
	else:
		type_file="Fasta"
		pass
	rgstro = list(SeqIO.parse(filename, type_file))
	cadena += ("\nnum_rgstro: " + str(len(rgstro)))
	cadena += ("\nrecord(s): ")
///////////////////////////////////////////////////////////////////////////////////	
	for seq_record in SeqIO.parse(filename, type_file):
		cadena += ("\n-ID: " + str(seq_record.id))
		cadena += ("\nName: " + seq_record.name)
		cadena += ("\nDescription: " + str(seq_record.description))
	return cadena
///////////////////////////////////////////////////////////////////////////////////
if __name__=="__main__":
	R = summarize_contents(filename)
	print(R)
