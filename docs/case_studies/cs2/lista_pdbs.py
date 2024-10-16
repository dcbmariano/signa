import glob

pastas = glob.glob("./pdb/*")
w = open("input_cs2.csv","w")

for pasta in pastas:

	pdbs = glob.glob(pasta+"/*.pdb")

	for pdb in pdbs:
		nome = pdb.replace("./", "./docs/case_studies/cs2/")
		w.write(nome + "\n")
