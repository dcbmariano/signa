import glob
import os

lista = glob.glob("../pdb/*.pdb")

cont = 0
for l in lista:
	cont+=1
	print(cont,'/',len(lista), l)
	os.system("python3 contacts.py "+l+" -csv")
