import math
import sys
'''
Script: contacts.py
Version: 0.4
Function: Simple script for calculating contacts
Use: python contacts.py [file-name].pdb [optional: -hb -hy -ar -re -at -sb -db -csv]
    -hb hydrogen bonds  -hy hydrophobic  -ar aromatic         -re repulsive 
	-at attractive      -sb salt bridge  -db disulfide bonds  -csv (save as csv) 
Author: @dcbmariano
Date: 2024
'''
# -----------------------------------------------------------------------------
# 0. Definitions
# -----------------------------------------------------------------------------

show_contacts = {

	'ligacao_hidrogenio': True,  # hydrogen bonds  - set True or False
	'hidrofobico': False,        # hydrophobic     - set True or False
	'aromatico': True,           # aromatic        - set True or False
	'repulsivo': True,           # repulsive       - set True or False
	'atrativo': True,            # attractive      - set True or False
	'ponte_salina': True,        # salt bridge     - set True or False
	"ponte_dissulfeto": True     # disulfide bonds - set True or False

}

# OUTPUT: saida = tela (just show it on the screen) | csv (file)
saida = 'tela'  # tela | csv

# INPUT: a PDB file
try:
	entrada = sys.argv[1]

	if len(sys.argv) > 2:
		for i in show_contacts:
			show_contacts[i] = False

		for i in range(len(sys.argv)):
			if sys.argv[i] == "-hb":
				show_contacts["ligacao_hidrogenio"] = True
			if sys.argv[i] == "-hy":
				show_contacts["hidrofobico"] = True
			if sys.argv[i] == "-ar":
				show_contacts["aromatico"] = True
			if sys.argv[i] == "-re":
				show_contacts["repulsivo"] = True
			if sys.argv[i] == "-at":
				show_contacts["atrativo"] = True
			if sys.argv[i] == "-sb":
				show_contacts["ponte_salina"] = True
			if sys.argv[i] == "-db":
				show_contacts["ponte_dissulfeto"] = True
			if sys.argv[i] == "-csv":
				saida = 'csv'
				for i in show_contacts: # csv salva tudo 
					show_contacts[i] = True

except:
	entrada = "../docs/examples/2lzm.pdb"

# -----------------------------------------------------------------------------
# Definições padrão do sistema | System default settings
# -----------------------------------------------------------------------------

if saida == 'csv':
	w = open('contacts.csv','w')
	w.write('CONTACT;RES1:ATOM;RES2:ATOM;DIST\n') # cabeçalho do CSV

# CONTATOS (baseado na definição do nAPOLI) - contacts by nApoli
# tipo = (distancia_minima, distancia_maxima)
aromatic = (2, 4)
hidrogen_bond = (0, 3.9)
hidrophobic = (2, 4.5)
repulsive = (2, 6)
atractive = (2, 6)
salt_bridge = (0, 3.9)
disulfide_bond = (0, 2.8)

three_to_one = { "ALA": "A", "ARG": "R", "ASN": "N", "ASP": "D", "CYS": "C", "GLN": "Q", "GLU": "E", "GLY": "G", "HIS": "H", "ILE": "I", "LEU": "L", "LYS": "K", "MET": "M", "PHE": "F", "PRO": "P", "SER": "S", "THR": "T", "TRP": "W", "TYR": "Y", "VAL": "V" } 

# REGRAS - RULES
# 1 - deve ser feito por átomos de resíduos diferentes (must be made by different residue atoms)
# 2 - aromatic = aromatic + aromatic
# 3 - hb => aceptor + donor
# 4 - hidrophobic: hidrofobic + hidrofobic
# 5 - Repulsive: positive=>positive ou negative=>negative
# 6 - Atractive: positive=>negative ou negative=>positive
# 7 - salt_bridge: positive=>negative ou negative=>positive

# 'RES:ATOM':	[	Hydrophobic,	Aromatic,	Positive,	Negative,	Donor,	Acceptor	]
# 'ALA:CA':		[	0|1,			0|1,		0|1,		0|1,		0|1,	0|1			]
contatos = { 'ALA:N': [0, 0, 0, 0, 1, 0], 'ALA:CA': [0, 0, 0, 0, 0, 0], 'ALA:C': [0, 0, 0, 0, 0, 0], 'ALA:O': [0, 0, 0, 0, 0, 1], 'ALA:CB': [1, 0, 0, 0, 0, 0], 'ARG:N': [0, 0, 0, 0, 1, 0], 'ARG:CA': [0, 0, 0, 0, 0, 0], 'ARG:C': [0, 0, 0, 0, 0, 0], 'ARG:O': [0, 0, 0, 0, 0, 1], 'ARG:CB': [1, 0, 0, 0, 0, 0], 'ARG:CG': [1, 0, 0, 0, 0, 0], 'ARG:CD': [0, 0, 0, 0, 0, 0], 'ARG:NE': [0, 0, 1, 0, 1, 0], 'ARG:CZ': [0, 0, 1, 0, 0, 0], 'ARG:NH1': [0, 0, 1, 0, 1, 0], 'ARG:NH2': [0, 0, 1, 0, 1, 0], 'ASN:N': [0, 0, 0, 0, 1, 0], 'ASN:CA': [0, 0, 0, 0, 0, 0], 'ASN:C': [0, 0, 0, 0, 0, 0], 'ASN:O': [0, 0, 0, 0, 0, 1], 'ASN:CB': [1, 0, 0, 0, 0, 0], 'ASN:CG': [0, 0, 0, 0, 0, 0], 'ASN:OD1': [0, 0, 0, 0, 0, 1], 'ASN:ND2': [0, 0, 0, 0, 1, 0], 'ASP:N': [0, 0, 0, 0, 1, 0], 'ASP:CA': [0, 0, 0, 0, 0, 0], 'ASP:C': [0, 0, 0, 0, 0, 0], 'ASP:O': [0, 0, 0, 0, 0, 1], 'ASP:CB': [1, 0, 0, 0, 0, 0], 'ASP:CG': [0, 0, 0, 0, 0, 0], 'ASP:OD1': [0, 0, 0, 1, 0, 1], 'ASP:OD2': [0, 0, 0, 1, 0, 1], 'CYS:N': [0, 0, 0, 0, 1, 0], 'CYS:CA': [0, 0, 0, 0, 0, 0], 'CYS:C': [0, 0, 0, 0, 0, 0], 'CYS:O': [0, 0, 0, 0, 0, 1], 'CYS:CB': [1, 0, 0, 0, 0, 0], 'CYS:SG': [0, 0, 0, 0, 1, 1], 'GLN:N': [0, 0, 0, 0, 1, 0], 'GLN:CA': [0, 0, 0, 0, 0, 0], 'GLN:C': [0, 0, 0, 0, 0, 0], 'GLN:O': [0, 0, 0, 0, 0, 1], 'GLN:CB': [1, 0, 0, 0, 0, 0], 'GLN:CG': [1, 0, 0, 0, 0, 0], 'GLN:CD': [0, 0, 0, 0, 0, 0], 'GLN:OE1': [0, 0, 0, 0, 0, 1], 'GLN:NE2': [0, 0, 0, 0, 1, 0], 'GLU:N': [0, 0, 0, 0, 1, 0], 'GLU:CA': [0, 0, 0, 0, 0, 0], 'GLU:C': [0, 0, 0, 0, 0, 0], 'GLU:O': [0, 0, 0, 0, 0, 1], 'GLU:CB': [1, 0, 0, 0, 0, 0], 'GLU:CG': [1, 0, 0, 0, 0, 0], 'GLU:CD': [0, 0, 0, 0, 0, 0], 'GLU:OE1': [0, 0, 0, 1, 0, 1], 'GLU:OE2': [0, 0, 0, 1, 0, 1], 'GLY:N': [0, 0, 0, 0, 1, 0], 'GLY:CA': [0, 0, 0, 0, 0, 0], 'GLY:C': [0, 0, 0, 0, 0, 0], 'GLY:O': [0, 0, 0, 0, 0, 1], 'HIS:N': [0, 0, 0, 0, 1, 0], 'HIS:CA': [0, 0, 0, 0, 0, 0], 'HIS:C': [0, 0, 0, 0, 0, 0], 'HIS:O': [0, 0, 0, 0, 0, 1], 'HIS:CB': [1, 0, 0, 0, 0, 0], 'HIS:CG': [0, 1, 0, 0, 0, 0], 'HIS:ND1': [0, 1, 1, 0, 1, 1], 'HIS:CD2': [0, 1, 0, 0, 0, 0], 'HIS:CE1': [0, 1, 0, 0, 0, 0], 'HIS:NE2': [0, 1, 1, 0, 1, 1], 'ILE:N': [0, 0, 0, 0, 1, 0], 'ILE:CA': [0, 0, 0, 0, 0, 0], 'ILE:C': [0, 0, 0, 0, 0, 0], 'ILE:O': [0, 0, 0, 0, 0, 1], 'ILE:CB': [1, 0, 0, 0, 0, 0], 'ILE:CG1': [1, 0, 0, 0, 0, 0], 'ILE:CG2': [1, 0, 0, 0, 0, 0], 'ILE:CD1': [1, 0, 0, 0, 0, 0], 'LEU:N': [0, 0, 0, 0, 1, 0], 'LEU:CA': [0, 0, 0, 0, 0, 0], 'LEU:C': [0, 0, 0, 0, 0, 0], 'LEU:O': [0, 0, 0, 0, 0, 1], 'LEU:CB': [1, 0, 0, 0, 0, 0], 'LEU:CG': [1, 0, 0, 0, 0, 0], 'LEU:CD1': [1, 0, 0, 0, 0, 0], 'LEU:CD2': [1, 0, 0, 0, 0, 0], 'LYS:N': [0, 0, 0, 0, 1, 0], 'LYS:CA': [0, 0, 0, 0, 0, 0], 'LYS:C': [0, 0, 0, 0, 0, 0], 'LYS:O': [0, 0, 0, 0, 0, 1], 'LYS:CB': [1, 0, 0, 0, 0, 0], 'LYS:CG': [1, 0, 0, 0, 0, 0], 'LYS:CD': [1, 0, 0, 0, 0, 0], 'LYS:CE': [0, 0, 0, 0, 0, 0], 'LYS:NZ': [0, 0, 1, 0, 1, 0], 'MET:N': [0, 0, 0, 0, 1, 0], 'MET:CA': [0, 0, 0, 0, 0, 0], 'MET:C': [0, 0, 0, 0, 0, 0], 'MET:O': [0, 0, 0, 0, 0, 1], 'MET:CB': [1, 0, 0, 0, 0, 0], 'MET:CG': [1, 0, 0, 0, 0, 0], 'MET:SD': [0, 0, 0, 0, 0, 1], 'MET:CE': [1, 0, 0, 0, 0, 0], 'PHE:N': [0, 0, 0, 0, 1, 0], 'PHE:CA': [0, 0, 0, 0, 0, 0], 'PHE:C': [0, 0, 0, 0, 0, 0], 'PHE:O': [0, 0, 0, 0, 0, 1], 'PHE:CB': [1, 0, 0, 0, 0, 0], 'PHE:CG': [1, 1, 0, 0, 0, 0], 'PHE:CD1': [1, 1, 0, 0, 0, 0], 'PHE:CD2': [1, 1, 0, 0, 0, 0], 'PHE:CE1': [1, 1, 0, 0, 0, 0], 'PHE:CE2': [1, 1, 0, 0, 0, 0], 'PHE:CZ': [1, 1, 0, 0, 0, 0], 'PRO:N': [0, 0, 0, 0, 0, 0], 'PRO:CA': [0, 0, 0, 0, 0, 0], 'PRO:C': [0, 0, 0, 0, 0, 0], 'PRO:O': [0, 0, 0, 0, 0, 1], 'PRO:CB': [1, 0, 0, 0, 0, 0], 'PRO:CG': [1, 0, 0, 0, 0, 0], 'PRO:CD': [0, 0, 0, 0, 0, 0], 'SER:N': [0, 0, 0, 0, 1, 0], 'SER:CA': [0, 0, 0, 0, 0, 0], 'SER:C': [0, 0, 0, 0, 0, 0], 'SER:O': [0, 0, 0, 0, 0, 1], 'SER:CB': [0, 0, 0, 0, 0, 0], 'SER:OG': [0, 0, 0, 0, 1, 1], 'THR:N': [0, 0, 0, 0, 1, 0], 'THR:CA': [0, 0, 0, 0, 0, 0], 'THR:C': [0, 0, 0, 0, 0, 0], 'THR:O': [0, 0, 0, 0, 0, 1], 'THR:CB': [0, 0, 0, 0, 0, 0], 'THR:OG1': [0, 0, 0, 0, 1, 1], 'THR:CG2': [1, 0, 0, 0, 0, 0], 'TRP:N': [0, 0, 0, 0, 1, 0], 'TRP:CA': [0, 0, 0, 0, 0, 0], 'TRP:C': [0, 0, 0, 0, 0, 0], 'TRP:O': [0, 0, 0, 0, 0, 1], 'TRP:CB': [1, 0, 0, 0, 0, 0], 'TRP:CG': [1, 1, 0, 0, 0, 0], 'TRP:CD1': [0, 1, 0, 0, 0, 0], 'TRP:CD2': [1, 1, 0, 0, 0, 0], 'TRP:NE1': [0, 1, 0, 0, 1, 0], 'TRP:CE2': [0, 1, 0, 0, 0, 0], 'TRP:CE3': [1, 1, 0, 0, 0, 0], 'TRP:CZ2': [1, 1, 0, 0, 0, 0], 'TRP:CZ3': [1, 1, 0, 0, 0, 0], 'TRP:CH2': [1, 1, 0, 0, 0, 0], 'TYR:N': [0, 0, 0, 0, 1, 0], 'TYR:CA': [0, 0, 0, 0, 0, 0], 'TYR:C': [0, 0, 0, 0, 0, 0], 'TYR:O': [0, 0, 0, 0, 0, 1], 'TYR:CB': [1, 0, 0, 0, 0, 0], 'TYR:CG': [1, 1, 0, 0, 0, 0], 'TYR:CD1': [1, 1, 0, 0, 0, 0], 'TYR:CD2': [1, 1, 0, 0, 0, 0], 'TYR:CE1': [1, 1, 0, 0, 0, 0], 'TYR:CE2': [1, 1, 0, 0, 0, 0], 'TYR:CZ': [0, 1, 0, 0, 0, 0], 'TYR:OH': [0, 0, 0, 0, 1, 1], 'VAL:N': [0, 0, 0, 0, 1, 0], 'VAL:CA': [0, 0, 0, 0, 0, 0], 'VAL:C': [0, 0, 0, 0, 0, 0], 'VAL:O': [0, 0, 0, 0, 0, 1], 'VAL:CB': [1, 0, 0, 0, 0, 0], 'VAL:CG1': [1, 0, 0, 0, 0, 0], 'VAL:CG2': [1, 0, 0, 0, 0, 0]}

# -----------------------------------------------------------------------------
# 1. LÊ ARQUIVO PDB E CONVERTE EM DICIONÁRIO - CONVERT PDB FILE TO SAVE DICT
# -----------------------------------------------------------------------------
# lê átomos - read atoms
with open(entrada) as pdb_file:
	linhas = pdb_file.readlines()
	pdb = {}
	for linha in linhas:
		if linha[0:4] == 'ATOM':

			residuo = linha[17:20].strip()
			atomo = linha[13:16].strip()
			res_num = linha[22:26].strip()
			cadeia = linha[21]

			chave = cadeia+':'+res_num+'-'+residuo+':'+atomo

			x = float(linha[30:38].strip())
			y = float(linha[38:46].strip())
			z = float(linha[46:54].strip())

			coord = (x, y, z)

			pdb[chave] = coord

# print(pdb)
# Exemplo de linha
# ATOM      2  CA  MET A   1      36.942 -23.581   8.984  1.00 19.55           C  
#OM      2  CA  MET A   1      36.942 -23.581   8.984  1.00 19.55           C  

# -----------------------------------------------------------------------------
# 2. CALCULA matriz de distância (TODOS contra TODOS) - RETURN distance matrix
# -----------------------------------------------------------------------------

def distancia(x1,y1,z1,x2,y2,z2):
	''' Calculate the Euclidean distance using the equation
		(calcula a distância euclidiana usando a fórmula):
	    	dist² = (x2-x1)² + (y2-y1)² + (z2-z1)²
	'''
	dist = math.sqrt(
		(x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2 
	)

	return round(dist, 1)

matriz_distancia = {}

# contatores numéricos
ni = 0
nj = 0


# preenche linha
for i in pdb:
	
	matriz_distancia[i] = {}

	# preenche coluna
	for j in pdb:

		if ni<nj:  # remove redundância (diagonal inferior)

			matriz_distancia[i][j] = distancia(
				pdb[i][0], pdb[i][1], pdb[i][2],
				pdb[j][0], pdb[j][1], pdb[j][2]
			)

		nj+=1
	ni+=1

# print(matriz_distancia)
# { 
#	'MET:N': {'MET:N': 0.0, 'MET:CA': 1.5, 'MET:C': 2.5, ... },
# 	'MET:CA': { MET:N': 1.5, 'MET:CA': 0.0, 'MET:C': 1.0, ... }, 
#   [...]
# }

# -----------------------------------------------------------------------------
# 3. Calculating contacts
# -----------------------------------------------------------------------------
# contatos = {'RES:ATOM': [Hydrophobic, Aromatic, Positive, Negative, Donor, Acceptor]}

# Analisa matriz de distância
for i in matriz_distancia:

	r1 = i.split('-')
	r1_num = r1[0]
	r1_name = r1[1]

	for j in matriz_distancia[i]:

		r2 = j.split('-')
		r2_num = r2[0]
		r2_name = r2[1]

		# evita comparações com o mesmo resíduo
		if r1_num != r2_num:


			# hidrofobico -----------------------------------------------------
			if show_contacts['hidrofobico']:
				if matriz_distancia[i][j] >= hidrophobic[0] and matriz_distancia[i][j] <= hidrophobic[1]:
					try:
						if contatos[r1_name][0] == 1 and contatos[r2_name][0] == 1:
							if saida == 'tela':
								print('HY', i, j, matriz_distancia[i][j], sep=';')
							else:
								w.write("HY;"+i+";"+j+";"+str(matriz_distancia[i][j])+"\n")
					except:
						warning = 'Ignorando chave inexistente|Ignoring non-existent key: '+i+','+j


			# aromatic --------------------------------------------------------
			if show_contacts['aromatico']:
				if matriz_distancia[i][j] >= aromatic[0] and matriz_distancia[i][j] <= aromatic[1]:
					try:
						if contatos[r1_name][1] == 1 and contatos[r2_name][1] == 1:
							if saida == 'tela':
								print('AR', i, j, matriz_distancia[i][j], sep=';')
							else:
								w.write("AR;"+i+";"+j+";"+str(matriz_distancia[i][j])+"\n")
					except:
						warning = 'Ignorando chave inexistente|Ignoring non-existent key: '+i+','+j


			# repulsive -------------------------------------------------------
			if show_contacts['repulsivo']:
				if matriz_distancia[i][j] >= repulsive[0] and matriz_distancia[i][j] <= repulsive[1]:
					try:
						if ( 
							(contatos[r1_name][2] == 1 and contatos[r2_name][2] == 1) or # positivos vs. positivo
							(contatos[r1_name][3] == 1 and contatos[r2_name][3] == 1)    # negativo vs. negativo
						):
							if saida == 'tela':
								print('RE', i, j, matriz_distancia[i][j], sep=';')
							else:
								w.write("RE;"+i+";"+j+";"+str(matriz_distancia[i][j])+"\n")
					except:
						warning = 'Ignorando chave inexistente|Ignoring non-existent key: '+i+','+j


			# atrativo -------------------------------------------------------
			if show_contacts['atrativo']:
				if matriz_distancia[i][j] >= repulsive[0] and matriz_distancia[i][j] <= repulsive[1]:
					try:
						if ( 
							(contatos[r1_name][2] == 1 and contatos[r2_name][3] == 1) or # positivos vs. negativo
							(contatos[r1_name][3] == 1 and contatos[r2_name][2] == 1)    # negativo vs. positivo
						):
							if saida == 'tela':
								print('AT', i, j, matriz_distancia[i][j], sep=';')
							else:
								w.write("AT;"+i+";"+j+";"+str(matriz_distancia[i][j])+"\n")
					except:
						warning = 'Ignorando chave inexistente|Ignoring non-existent key: '+i+','+j


			# ligação de hidrogênio (hb) ------------------------------------
			if show_contacts['ligacao_hidrogenio']:
				# Reduz falsos positivos em alfa-hélices ---------------------
				# deve ter 3 residuos entre eles no caso das 310-helix ou 4 para alfa-helices 
				no_false_positive = True # estrategia mais simples do que calcular angulos de H
				# if abs(int(r1_num.split(':')[1]) - int(r2_num.split(':')[1])) < 3: 
				# 	atomo_atual = i.split(':')[-1] 
				# 	if atomo_atual == 'N' or atomo_atual == 'O': # verifica se pode fazer HB
				# 		no_false_positive = False  # bloqueia o cálculo de contato
				# / --------------------------------------------------------------------------------	
				if matriz_distancia[i][j] >= hidrogen_bond[0] and matriz_distancia[i][j] <= hidrogen_bond[1] and no_false_positive:
					try:
						if ( 
							(contatos[r1_name][4] == 1 and contatos[r2_name][5] == 1) or # donor vs. aceptor
							(contatos[r1_name][5] == 1 and contatos[r2_name][4] == 1)    # aceptor vs. donor
						):
							if saida == 'tela':
								print('HB', i, j, matriz_distancia[i][j], sep=';')
							else:
								w.write("HB;"+i+";"+j+";"+str(matriz_distancia[i][j])+"\n")
					except:
						warning = 'Ignorando chave inexistente|Ignoring non-existent key: '+i+','+j


			# ponte salina (atrativo + hb) ------------------------------------
			if show_contacts['ponte_salina']:
				if matriz_distancia[i][j] >= salt_bridge[0] and matriz_distancia[i][j] <= salt_bridge[1]:
					try:
						# atrativo
						if ( 
							(contatos[r1_name][2] == 1 and contatos[r2_name][3] == 1) or # positivos vs. negativo
							(contatos[r1_name][3] == 1 and contatos[r2_name][2] == 1)    # negativo vs. positivo
						):
							# ligação de hidrogênio
							if ( 
								(contatos[r1_name][4] == 1 and contatos[r2_name][5] == 1) or # donor vs. aceptor
								(contatos[r1_name][5] == 1 and contatos[r2_name][4] == 1)    # aceptor vs. donor
							):
								if saida == 'tela':
									print('SB', i, j, matriz_distancia[i][j], sep=';')
								else:
									w.write("SB;"+i+";"+j+";"+str(matriz_distancia[i][j])+"\n")
					except:
						warning = 'Ignorando chave inexistente|Ignoring non-existent key: '+i+','+j

			# ponte dissulfeto -----------------------------------------------------
			if show_contacts['ponte_dissulfeto']:
				if r1_name == "CYS" and r2_name == "CYS":
					if matriz_distancia[i][j] >= disulfide_bond[0] and matriz_distancia[i][j] <= disulfide_bond[1]:
						try:
							if saida == 'tela':
								print('DB', i, j, matriz_distancia[i][j], sep=';')
							else:
								w.write("DB;"+i+";"+j+";"+str(matriz_distancia[i][j])+"\n")
						except:
							warning = 'Ignorando chave inexistente|Ignoring non-existent key: '+i+','+j

if(saida == 'csv'):
	print('Contact calculation performed successfully. \nResult saved in: "contact.csv"')
	print('\nCSV specifications:\nContact type; Residue:atom 1; Residue:atom 2; Distance\n')

print('\nContact types:\n\tHB: hydrogen bonds (ligações de hidrogênio)\n\tHY: hydrophobic (hidrofóbico)\n\tAR: aromatic (aromático)\n\tAT: attractive (atrativo)\n\tRE: repulsive (repulsivo)\n\tSB: salt bridge (ponte de salina)\n')