import glob
import os

lista = glob.glob("../pdb_files/cs1/*.pdb")

cont = 0
for l in lista:
	cont+=1
	print(cont,'/',len(lista), l)
	# os.system("python3 contacts.py "+l+" -csv")
