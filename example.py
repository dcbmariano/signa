import Signa.signa as signa


#help(signa)  # for obtaining more details use this command

# simple use
signature = signa.read('./Signa/example/pdb_files/2lzm.pdb', 'csm')
print(signature)

# Multiple files
signa.read_csv('./Signa/example/input.csv', signa_type='csm', output='./Signa/example/output.csv')
