import Signa.signa as signa
# from signa import signa  #instalação local do signa v0.2 => /opt/homebrew/lib/python3.9/site-packages/signa

# help(signa)  # for obtaining more details use this command
# print(signa.version)  # returns signa version

# Simple use
#signature = signa.read('./docs/examples/pdb_files/2lzm.pdb', 'acsm-all', cutoff_limit=20, cutoff_step=2, separator=",", cumulative=True)
#print(signature)

# SIGNA-CHARGE
# signature = signa.read('./docs/examples/pdb_files/2lzm.pdb', signa_type='SIGNA-CHARGE')
# print(signature)

# signature = signa.read('./docs/examples/pdb_files/2lzm.pdb', 'csm', cutoff_limit=30, cutoff_step=0.2, separator=",", cumulative=True)
# print(signature)

# Obtaining the labels
#labels_example = signa.labels(signa_type='csm', cutoff_step=2, cutoff_limit=20, separator=",", cumulative=True)
#print(labels_example)

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
#  	csv_file='./docs/examples/input_cs1.csv', 
#  	signa_type='csm', 
#  	output='./docs/examples/output_cs1.csv',
#     cutoff_limit=30
# )

# SSV - Comparisons between signatures
#ssv = signa.ssv('./docs/examples/pdb_files/2lzm.pdb', './docs/examples/pdb_files/2lzm.pdb')
#print(ssv)

# Multiple files
signa.read_csv(
 	csv_file='./docs/examples/input_cs1.csv', 
 	signa_type='signa-charge', 
 	output='./docs/examples/output_signa.csv',
    cutoff_limit=30
)