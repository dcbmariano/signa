import math
'''
Script: contatos.py
Versão: 0.1
Função: Script simples para cálculos de contatos
Autor: @dcbmariano
Data: 2022
'''
# -----------------------------------------------------------------------------
# 0. DEFINIÇÕES
# -----------------------------------------------------------------------------

# INPUT: arquivo PDB de entrada
entrada = "2lzm.pdb"

mostrar_contato = {

	'ligacao_hidrogenio': True,
	'hidrofobico': True,
	'aromatico': True,
	'repulsivo': True,
	'atrativo': True,
	'ponte_salina': True

}

# OUTPUT: saida = tela | csv
saida = 'tela'

# -----------------------------------------------------------------------------
# Definições padrão do sistema
# -----------------------------------------------------------------------------

if saida == 'csv':
	w = open('contatos.csv','w')
	w.write('CONTACT;RES1:ATOM;RES2:ATOM;DIST\n') # cabeçalho do CSV

# CONTATOS (baseado na definição do nAPOLI) 
# tipo = (distancia_minima, distancia_maxima)
aromatic = (2, 4)
hidrogen_bond = (0, 3.9)
hidrophobic = (2, 4.5)
repulsive = (2, 6)
atractive = (2, 6)
salt_bridge = (0, 3.9)


# REGRAS
# 1 - deve ser feito por átomos de resíduos diferentes
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
# 1. LÊ ARQUIVO PDB E CONVERTE EM DICIONÁRIO
# -----------------------------------------------------------------------------
# lê átomos
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
# 2. CALCULA matriz de distância => TODOS contra TODOS
# -----------------------------------------------------------------------------

def distancia(x1,y1,z1,x2,y2,z2):
	''' Calcula a distância euclidiana usando a fórmula:
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

#print(matriz_distancia)
# { 
#	'MET:N': {'MET:N': 0.0, 'MET:CA': 1.5, 'MET:C': 2.5, ... },
# 	'MET:CA': { MET:N': 1.5, 'MET:CA': 0.0, 'MET:C': 1.0, ... }, 
#   [...]
# }

# -----------------------------------------------------------------------------
# 3. CÁLCULO DE CONTATOS 
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
			if mostrar_contato['hidrofobico']:
				if matriz_distancia[i][j] >= hidrophobic[0] and matriz_distancia[i][j] <= hidrophobic[1]:
					try:
						if contatos[r1_name][0] == 1 and contatos[r2_name][0] == 1:
							if saida == 'tela':
								print('HIDROFÓBICO', i, j, matriz_distancia[i][j], sep=';')
							else:
								w.write("HY;"+i+";"+j+";"+str(matriz_distancia[i][j])+"\n")
					except:
						warning = 'Ignorando chave inexistente: '+i+','+j


			# aromatic --------------------------------------------------------
			if mostrar_contato['aromatico']:
				if matriz_distancia[i][j] >= aromatic[0] and matriz_distancia[i][j] <= aromatic[1]:
					try:
						if contatos[r1_name][1] == 1 and contatos[r2_name][1] == 1:
							if saida == 'tela':
								print('AROMÁTICO', i, j, matriz_distancia[i][j], sep=';')
							else:
								w.write("AR;"+i+";"+j+";"+str(matriz_distancia[i][j])+"\n")
					except:
						warning = 'Ignorando chave inexistente: '+i+','+j


			# repulsive -------------------------------------------------------
			if mostrar_contato['repulsivo']:
				if matriz_distancia[i][j] >= repulsive[0] and matriz_distancia[i][j] <= repulsive[1]:
					try:
						if ( 
							(contatos[r1_name][2] == 1 and contatos[r2_name][2] == 1) or # positivos vs. positivo
							(contatos[r1_name][3] == 1 and contatos[r2_name][3] == 1)    # negativo vs. negativo
						):
							if saida == 'tela':
								print('REPULSIVO', i, j, matriz_distancia[i][j], sep=';')
							else:
								w.write("RE;"+i+";"+j+";"+str(matriz_distancia[i][j])+"\n")
					except:
						warning = 'Ignorando chave inexistente: '+i+','+j


			# atrativo -------------------------------------------------------
			if mostrar_contato['atrativo']:
				if matriz_distancia[i][j] >= repulsive[0] and matriz_distancia[i][j] <= repulsive[1]:
					try:
						if ( 
							(contatos[r1_name][2] == 1 and contatos[r2_name][3] == 1) or # positivos vs. negativo
							(contatos[r1_name][3] == 1 and contatos[r2_name][2] == 1)    # negativo vs. positivo
						):
							if saida == 'tela':
								print('ATRATIVO', i, j, matriz_distancia[i][j], sep=';')
							else:
								w.write("AT;"+i+";"+j+";"+str(matriz_distancia[i][j])+"\n")
					except:
						warning = 'Ignorando chave inexistente: '+i+','+j


			# ligação de hidrogênio (hb) ------------------------------------
			if mostrar_contato['ligacao_hidrogenio']:
				if matriz_distancia[i][j] >= hidrogen_bond[0] and matriz_distancia[i][j] <= hidrogen_bond[1]:
					try:
						if ( 
							(contatos[r1_name][4] == 1 and contatos[r2_name][5] == 1) or # donor vs. aceptor
							(contatos[r1_name][5] == 1 and contatos[r2_name][4] == 1)    # aceptor vs. donor
						):
							if saida == 'tela':
								print('LIGAÇÃO_DE_HIDROGÊNIO', i, j, matriz_distancia[i][j], sep=';')
							else:
								w.write("HB;"+i+";"+j+";"+str(matriz_distancia[i][j])+"\n")
					except:
						warning = 'Ignorando chave inexistente: '+i+','+j


			# ponte salina (atrativo + hb) ------------------------------------
			if mostrar_contato['ponte_salina']:
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
									print('PONTE_SALINA', i, j, matriz_distancia[i][j], sep=';')
								else:
									w.write("SB;"+i+";"+j+";"+str(matriz_distancia[i][j])+"\n")
					except:
						warning = 'Ignorando chave inexistente: '+i+','+j


if(saida == 'csv'):
	print('Cálculo de contatos realizado com sucesso. \nResultado gravado em: "contato.csv"')
	print('\nEspecificações do CSV:\nTipo de contato; Resíduo:átomo 1; Resíduo:átomo 2; Distância\n')
	print('Tipos de contatos:\n\tHB: ligação de hidrogênio\n\tHY: hidrofóbio\n\tAR: aromático\n\tAT: atrativo\n\tRE: repulsivo\n\tSB: ponte salida\n')