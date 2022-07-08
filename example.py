import Signa.signa as signa


#help(signa)  # for obtaining more details use this command

# simple use
signature = signa.read('./example/pdb_files/2lzm.pdb', 'csm')
print(signature)

# Multiple files
signa.read_csv('./example/input.csv', signa_type='csm', output='./example/output.csv')
