import glob

pastas = glob.glob("./pdb/*")
w = open("input_cs3.csv","w")

for pasta in pastas:

	pdbs = glob.glob(pasta+"/*.pdb")

	for pdb in pdbs:
		nome = pdb.replace("./", "./docs/case_studies/cs3/")
		w.write(nome + "\n")
