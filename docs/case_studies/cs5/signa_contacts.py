#import networkx as nx
#from node2vec import Node2Vec
import numpy as np
import glob

three_to_one = { "ALA": "A", "ARG": "R", "ASN": "N", "ASP": "D", "CYS": "C", "GLN": "Q", "GLU": "E", "GLY": "G", "HIS": "H", "ILE": "I", "LEU": "L", "LYS": "K", "MET": "M", "PHE": "F", "PRO": "P", "SER": "S", "THR": "T", "TRP": "W", "TYR": "Y", "VAL": "V" } 


def formata(r):

	aux = r.split(":") # 0 cadeia, 1 num-res, 2 atom
	cadeia = aux[0]
	atom = aux[2]
	num = aux[1].split('-')[0]
	nome = aux[1].split('-')[1]

	return cadeia, atom, num, nome



pasta = glob.glob("output/*csv")
ct = 0
w = open("assinatura.csv","w")

for arquivo_nome in pasta: 
	ct+=1
	print(ct, "/", len(pasta), arquivo_nome)

	dists_hb = []; dists_ar = []; dists_at = []; dists_re = []; 

	cont = 0
	with open(arquivo_nome) as arquivo:

		contatos = arquivo.readlines()

		for contato in contatos:
			if cont == 0:
				cont+=1
				continue
			dist = 0
			tipo, r1, r2, dist = contato.split(";")

			cadeia1, atom1, num1, nome1 = formata(r1)
			cadeia2, atom2, num2, nome2 = formata(r2)

			dist = abs(int(num2) - int(num1))

			if tipo == "HB":
				dists_hb.append(dist)
			if tipo == "AR":
				dists_ar.append(dist)
			if tipo == "AT":
				dists_at.append(dist)
			if tipo == "RE":
				dists_re.append(dist)

			cont+=1

	#print(dists)
	c1, i1 = np.histogram(dists_hb, bins=100)
	c2, i2 = np.histogram(dists_ar, bins=100)
	c3, i3 = np.histogram(dists_at, bins=100)
	c4, i4 = np.histogram(dists_re, bins=100)


	# for i, j in zip(contagens, intervalos):
	# 	print(i, ":", j)
	nome1 = arquivo_nome.split("/")[-1]
	nome = "output_formatado/"+nome1
	assinatura = list(c1) + list(c2) + list(c3) + list(c4)
	assinatura = str(assinatura).replace("[","").replace("]","")
	print(nome1, ",", assinatura, file=w)




