import Signa.signa as signa

#help(signa)  # for obtaining more details use this command
# print(signa.version)  # returns signa version

# Simple use
signature = signa.read('./docs/examples/pdb_files/2lzm.pdb', 'csm')
print(signature)

# signature = signa.read('./docs/examples/pdb_files/2lzm.pdb', 'acsm')
# print(signature)

# signature = signa.read('./docs/examples/pdb_files/2lzm.pdb', 'acsm_hp')
# print(signature)

# signature = signa.read('./docs/examples/pdb_files/2lzm.pdb', 'acsm_all')
# print(signature)

# Select a specific chain
# signature = signa.read('./docs/examples/pdb_files/2lzm.pdb', 'csm', chain='A')
# print(signature)

# Multiple files
# signa.read_csv(
# 	csv_file='./docs/examples/input.csv', 
# 	signa_type='csm', 
# 	output='./docs/examples/output.csv'
# )

# SSV - Comparisons between signatures
#ssv = signa.ssv('./docs/examples/pdb_files/2lzm.pdb', './docs/examples/pdb_files/2lzm.pdb')
#print(ssv)