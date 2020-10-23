ffrom Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os

# Cambiar la dirección del archivo .gbk que desee leer
filename =  "/mnt/c/Users/MUDTL/Docuemnts/git/Ejercicio-biopython/ls_orchid.gbk"

def summarize_contents(filename):
	ListaR = []
	ListaR = os.path.split(filename)
	Cadena = " "
	Cadena = ("file: "+ ListaR[1] + "\npath: " + ListaR[0])
	# Número de registros
	all_records=[]
	records = list(SeqIO.parse(filename, "genbank"))
	Cadena += ("\nnum_records: " + str(len(records)))
	Cadena += ("\nrecords:")
	# Registros
	for seq_record in SeqIO.parse(filename, "genbank"):
		all_records.append(seq_record.name)
		Cadena += ("\n- id:" + str(seq_record.id))
		Cadena += ("\nname: " + seq_record.name)
		Cadena += ("\ndescription: " + str(seq_record.description))
		Cadena += ("\n")
	return Cadena
R = summarize_contents(filename)
print(R)
