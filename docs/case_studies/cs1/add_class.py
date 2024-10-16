entrada = "output_signa_not_cumulative_12.csv"
dados = """pdbid,family,superfamily
2ADA,adenosine deaminase,amidohydrolase
1A4M,adenosine deaminase,amidohydrolase
1A4L,adenosine deaminase,amidohydrolase
1ADD,adenosine deaminase,amidohydrolase
1FKW,adenosine deaminase,amidohydrolase
1FKX,adenosine deaminase,amidohydrolase
1UIO,adenosine deaminase,amidohydrolase
1UIP,adenosine deaminase,amidohydrolase
1KRM,adenosine deaminase,amidohydrolase
1NDZ,adenosine deaminase,amidohydrolase
1W1I,adenosine deaminase,amidohydrolase
1NDV,adenosine deaminase,amidohydrolase
1NDW,adenosine deaminase,amidohydrolase
1NDY,adenosine deaminase,amidohydrolase
1O5R,adenosine deaminase,amidohydrolase
1QXL,adenosine deaminase,amidohydrolase
1UML,adenosine deaminase,amidohydrolase
2BGN,adenosine deaminase,amidohydrolase
2E1W,adenosine deaminase,amidohydrolase
1V79,adenosine deaminase,amidohydrolase
1V7A,adenosine deaminase,amidohydrolase
1VFL,adenosine deaminase,amidohydrolase
1WXY,adenosine deaminase,amidohydrolase
1WXZ,adenosine deaminase,amidohydrolase
1K70,cytosine deaminase,amidohydrolase
1K6W,cytosine deaminase,amidohydrolase
1RA0,cytosine deaminase,amidohydrolase
1RA5,cytosine deaminase,amidohydrolase
1RAK,cytosine deaminase,amidohydrolase
1R9X,cytosine deaminase,amidohydrolase
1R9Y,cytosine deaminase,amidohydrolase
1R9Z,cytosine deaminase,amidohydrolase
3G77,cytosine deaminase,amidohydrolase
1NFG,d-hydantoinase,amidohydrolase
1K1D,d-hydantoinase,amidohydrolase
1GKQ,d-hydantoinase,amidohydrolase
1GKP,d-hydantoinase,amidohydrolase
1YNY,d-hydantoinase,amidohydrolase
1J79,dihydroorotase3,amidohydrolase
2E25,dihydroorotase3,amidohydrolase
2Z27,dihydroorotase3,amidohydrolase
2Z24,dihydroorotase3,amidohydrolase
2Z25,dihydroorotase3,amidohydrolase
2Z26,dihydroorotase3,amidohydrolase
2Z28,dihydroorotase3,amidohydrolase
2Z29,dihydroorotase3,amidohydrolase
2Z2A,dihydroorotase3,amidohydrolase
2Z2B,dihydroorotase3,amidohydrolase
1XGE,dihydroorotase3,amidohydrolase
2GOK,imidazolonepropionase,amidohydrolase
2PUZ,imidazolonepropionase,amidohydrolase
2BB0,imidazolonepropionase,amidohydrolase
2G3F,imidazolonepropionase,amidohydrolase
1ONX,isoaspartyl dipeptidase,amidohydrolase
1ONW,isoaspartyl dipeptidase,amidohydrolase
1POK,isoaspartyl dipeptidase,amidohydrolase
1PO9,isoaspartyl dipeptidase,amidohydrolase
1POJ,isoaspartyl dipeptidase,amidohydrolase
1M7J,n-acyl-d-amino-acid deacylase,amidohydrolase
1RK5,n-acyl-d-amino-acid deacylase,amidohydrolase
1V4Y,n-acyl-d-amino-acid deacylase,amidohydrolase
1V51,n-acyl-d-amino-acid deacylase,amidohydrolase
1RJP,n-acyl-d-amino-acid deacylase,amidohydrolase
1RJQ,n-acyl-d-amino-acid deacylase,amidohydrolase
1RJR,n-acyl-d-amino-acid deacylase,amidohydrolase
1RK6,n-acyl-d-amino-acid deacylase,amidohydrolase
2DVT,gamma-resorcylate decarboxylase,amidohydrolase
2DVU,gamma-resorcylate decarboxylase,amidohydrolase
2DVX,gamma-resorcylate decarboxylase,amidohydrolase
1I0D,phosphotriesterase,amidohydrolase
1I0B,phosphotriesterase,amidohydrolase
1HZY,phosphotriesterase,amidohydrolase
1DPM,phosphotriesterase,amidohydrolase
1PTA,phosphotriesterase,amidohydrolase
1JGM,phosphotriesterase,amidohydrolase
1EZ2,phosphotriesterase,amidohydrolase
1EYW,phosphotriesterase,amidohydrolase
2R1K,phosphotriesterase,amidohydrolase
2R1L,phosphotriesterase,amidohydrolase
2R1M,phosphotriesterase,amidohydrolase
2R1N,phosphotriesterase,amidohydrolase
3C86,phosphotriesterase,amidohydrolase
2R1P,phosphotriesterase,amidohydrolase
1PSC,phosphotriesterase,amidohydrolase
2O4M,phosphotriesterase,amidohydrolase
2O4Q,phosphotriesterase,amidohydrolase
2OB3,phosphotriesterase,amidohydrolase
2OQL,phosphotriesterase,amidohydrolase
1P6C,phosphotriesterase,amidohydrolase
1P6B,phosphotriesterase,amidohydrolase
1QW7,phosphotriesterase,amidohydrolase
2D2G,phosphotriesterase,amidohydrolase
2D2H,phosphotriesterase,amidohydrolase
2D2J,phosphotriesterase,amidohydrolase
1E9Z,urease,amidohydrolase
1E9Y,urease,amidohydrolase
2KAU,urease,amidohydrolase
1KRA,urease,amidohydrolase
1A5K,urease,amidohydrolase
1A5L,urease,amidohydrolase
1A5N,urease,amidohydrolase
1A5O,urease,amidohydrolase
1A5M,urease,amidohydrolase
1EJR,urease,amidohydrolase
1EJS,urease,amidohydrolase
1EJT,urease,amidohydrolase
1EJU,urease,amidohydrolase
1EJV,urease,amidohydrolase
1EJW,urease,amidohydrolase
1FWE,urease,amidohydrolase
1FWF,urease,amidohydrolase
1FWG,urease,amidohydrolase
1FWH,urease,amidohydrolase
1FWI,urease,amidohydrolase
1FWA,urease,amidohydrolase
1FWB,urease,amidohydrolase
1FWC,urease,amidohydrolase
1FWD,urease,amidohydrolase
1KRB,urease,amidohydrolase
1KRC,urease,amidohydrolase
1EJX,urease,amidohydrolase
1FWJ,urease,amidohydrolase
1EF2,urease,amidohydrolase
1UBP,urease,amidohydrolase
4UBP,urease,amidohydrolase
3UBP,urease,amidohydrolase
2UBP,urease,amidohydrolase
1S3T,urease,amidohydrolase
1IE7,urease,amidohydrolase
1J5S,uronate isomerase,amidohydrolase
2Q01,uronate isomerase,amidohydrolase
2Q6E,uronate isomerase,amidohydrolase
2Q08,uronate isomerase,amidohydrolase
1WDK,enoyl-CoA hydratase,crotonase
1WDM,enoyl-CoA hydratase,crotonase
1WDL,enoyl-CoA hydratase,crotonase
1EY3,enoyl-CoA hydratase,crotonase
2DUB,enoyl-CoA hydratase,crotonase
1DUB,enoyl-CoA hydratase,crotonase
1MJ3,enoyl-CoA hydratase,crotonase
1HNU,dodecenoyl-CoA delta-isomerase (peroxisomal),crotonase
1HNO,dodecenoyl-CoA delta-isomerase (peroxisomal),crotonase
1K39,dodecenoyl-CoA delta-isomerase (peroxisomal),crotonase
1PJH,dodecenoyl-CoA delta-isomerase (peroxisomal),crotonase
1Q51,1,4-dihydroxy-2-napthoyl-CoA synthase,crotonase
1Q52,1,4-dihydroxy-2-napthoyl-CoA synthase,crotonase
1RJM,1,4-dihydroxy-2-napthoyl-CoA synthase,crotonase
1RJN,1,4-dihydroxy-2-napthoyl-CoA synthase,crotonase
2GTR,histone acetyltransferase,crotonase
2FBM,histone acetyltransferase,crotonase
2FW2,histone acetyltransferase,crotonase
1E9I,enolase,enolase
2ONE,enolase,enolase
1ONE,enolase,enolase
1PDY,enolase,enolase
1PDZ,enolase,enolase
1EBH,enolase,enolase
1EBG,enolase,enolase
1ELS,enolase,enolase
1NEL,enolase,enolase
7ENL,enolase,enolase
6ENL,enolase,enolase
5ENL,enolase,enolase
4ENL,enolase,enolase
3ENL,enolase,enolase
1OEP,enolase,enolase
1IYX,enolase,enolase
1L8P,enolase,enolase
1P43,enolase,enolase
1P48,enolase,enolase
1TE6,enolase,enolase
2AL2,enolase,enolase
2FYM,enolase,enolase
2AKZ,enolase,enolase
2AKM,enolase,enolase
2AL1,enolase,enolase
2OQY,galactarate dehydratase,enolase
3ES7,galactarate dehydratase,enolase
3ES8,galactarate dehydratase,enolase
3FYY,galactarate dehydratase,enolase
3GD6,galactarate dehydratase,enolase
1ECQ,glucarate dehydratase,enolase
1EC9,glucarate dehydratase,enolase
1EC8,glucarate dehydratase,enolase
1EC7,glucarate dehydratase,enolase
1BQG,glucarate dehydratase,enolase
1JCT,glucarate dehydratase,enolase
1JDF,glucarate dehydratase,enolase
1MDR,mandelate racemase,enolase
2MNR,mandelate racemase,enolase
1MNS,mandelate racemase,enolase
1DTN,mandelate racemase,enolase
1MDL,mandelate racemase,enolase
1MRA,mandelate racemase,enolase
1YEY,L-fuconate dehydratase,enolase
1TZZ,D-tartrate dehydratase,enolase
2GSH,rhamnonate dehydratase,enolase
2I5Q,rhamnonate dehydratase,enolase
2HNE,L-fuconate dehydratase,enolase
2HXU,L-fuconate dehydratase,enolase
2DW6,D-tartrate dehydratase,enolase
2DW7,D-tartrate dehydratase,enolase
2HXT,L-fuconate dehydratase,enolase
2P3Z,rhamnonate dehydratase,enolase
2P0I,rhamnonate dehydratase,enolase
2OG9,L-talarate/galactarate dehydratase,enolase
2PP0,L-talarate/galactarate dehydratase,enolase
2PP1,L-talarate/galactarate dehydratase,enolase
2PP3,L-talarate/galactarate dehydratase,enolase
3BOX,rhamnonate dehydratase,enolase
3D46,rhamnonate dehydratase,enolase
3D47,rhamnonate dehydratase,enolase
2OZ3,rhamnonate dehydratase,enolase
2QJJ,mannonate dehydratase,enolase
2QJN,mannonate dehydratase,enolase
2QJM,mannonate dehydratase,enolase
1KKR,methylaspartate ammonia-lyase,enolase
1KKO,methylaspartate ammonia-lyase,enolase
1KD0,methylaspartate ammonia-lyase,enolase
1KCZ,methylaspartate ammonia-lyase,enolase
1FHV,o-succinylbenzoate synthase,enolase
1FHU,o-succinylbenzoate synthase,enolase
1JPM,dipeptide epimerase,enolase
1JPD,dipeptide epimerase,enolase
1TKK,dipeptide epimerase,enolase
1F9C,muconate cycloisomerase (syn),enolase
2MUC,muconate cycloisomerase (syn),enolase
3MUC,muconate cycloisomerase (syn),enolase
1SJA,o-succinylbenzoate synthase,enolase
1SJB,o-succinylbenzoate synthase,enolase
1SJC,o-succinylbenzoate synthase,enolase
1SJD,o-succinylbenzoate synthase,enolase
1R6W,o-succinylbenzoate synthase,enolase
1XS2,N-succinylamino acid racemase,enolase
1XPY,N-succinylamino acid racemase,enolase
1R0M,N-succinylamino acid racemase,enolase
1WUE,o-succinylbenzoate synthase,enolase
1WUF,o-succinylbenzoate synthase,enolase
2OFJ,o-succinylbenzoate synthase,enolase
2FKP,N-succinylamino acid racemase,enolase
2GGG,N-succinylamino acid racemase,enolase
2GGH,N-succinylamino acid racemase,enolase
2GGI,N-succinylamino acid racemase,enolase
2GGJ,N-succinylamino acid racemase,enolase
2OKT,o-succinylbenzoate synthase,enolase
2OLA,o-succinylbenzoate synthase,enolase
2PGE,o-succinylbenzoate synthase,enolase
2OZT,o-succinylbenzoate synthase,enolase
2P88,N-succinylamino acid racemase 2,enolase
2P8B,N-succinylamino acid racemase 2,enolase
2P8C,N-succinylamino acid racemase 2,enolase
2ZC8,N-succinylamino acid racemase,enolase
3CAW,o-succinylbenzoate synthase,enolase
3DG3,muconate cycloisomerase (anti),enolase
3DG6,muconate cycloisomerase (anti),enolase
3DG7,muconate cycloisomerase (anti),enolase
1AQ6,2-haloacid dehalogenase,haloacid dehalogenase
1JUD,2-haloacid dehalogenase,haloacid dehalogenase
1QH9,2-haloacid dehalogenase,haloacid dehalogenase
1QQ5,2-haloacid dehalogenase,haloacid dehalogenase
1QQ6,2-haloacid dehalogenase,haloacid dehalogenase
1QQ7,2-haloacid dehalogenase,haloacid dehalogenase
1ZRM,2-haloacid dehalogenase,haloacid dehalogenase
1ZRN,2-haloacid dehalogenase,haloacid dehalogenase
1MH9,5'-nucleotidase,haloacid dehalogenase
1Q92,5'-nucleotidase,haloacid dehalogenase
1Q91,5'-nucleotidase,haloacid dehalogenase
1CQZ,epoxide hydrolase n-terminal phosphatase,haloacid dehalogenase
1CR6,epoxide hydrolase n-terminal phosphatase,haloacid dehalogenase
1EK1,epoxide hydrolase n-terminal phosphatase,haloacid dehalogenase
1EK2,epoxide hydrolase n-terminal phosphatase,haloacid dehalogenase
1S8O,epoxide hydrolase n-terminal phosphatase,haloacid dehalogenase
1VJ5,epoxide hydrolase n-terminal phosphatase,haloacid dehalogenase
1SU4,p-type atpase,haloacid dehalogenase
1IWO,p-type atpase,haloacid dehalogenase
1KJU,p-type atpase,haloacid dehalogenase
1T5S,p-type atpase,haloacid dehalogenase
1T5T,p-type atpase,haloacid dehalogenase
1VFP,p-type atpase,haloacid dehalogenase
2ZBD,p-type atpase,haloacid dehalogenase
1WPG,p-type atpase,haloacid dehalogenase
1LVH,beta-phosphoglucomutase,haloacid dehalogenase
1O03,beta-phosphoglucomutase,haloacid dehalogenase
1O08,beta-phosphoglucomutase,haloacid dehalogenase
1F5S,phosphoserine phosphatase,haloacid dehalogenase
1J97,phosphoserine phosphatase,haloacid dehalogenase
1L7M,phosphoserine phosphatase,haloacid dehalogenase
1L7N,phosphoserine phosphatase,haloacid dehalogenase
1NNL,phosphoserine phosphatase,haloacid dehalogenase
1L8O,phosphoserine phosphatase,haloacid dehalogenase
1L8L,phosphoserine phosphatase,haloacid dehalogenase
1L7P,phosphoserine phosphatase,haloacid dehalogenase
1L7O,phosphoserine phosphatase,haloacid dehalogenase
1FEZ,phosphonoacetaldehyde hydrolase,haloacid dehalogenase
1SWW,phosphonoacetaldehyde hydrolase,haloacid dehalogenase
1SWV,phosphonoacetaldehyde hydrolase,haloacid dehalogenase
1RDF,phosphonoacetaldehyde hydrolase,haloacid dehalogenase
1RQN,phosphonoacetaldehyde hydrolase,haloacid dehalogenase
1RQL,phosphonoacetaldehyde hydrolase,haloacid dehalogenase
5EAT,5epi-Aristolochene,isoprenoid synthase typeI
1HX9,5epi-Aristolochene,isoprenoid synthase typeI
1HXA,5epi-Aristolochene,isoprenoid synthase typeI
1HXC,5epi-Aristolochene,isoprenoid synthase typeI
1HXG,5epi-Aristolochene,isoprenoid synthase typeI
5EAS,5epi-Aristolochene,isoprenoid synthase typeI
5EAU,5epi-Aristolochene,isoprenoid synthase typeI
1N1B,Bornyl Diphosphate,isoprenoid synthase typeI
1N1Z,Bornyl Diphosphate,isoprenoid synthase typeI
1N20,Bornyl Diphosphate,isoprenoid synthase typeI
1N21,Bornyl Diphosphate,isoprenoid synthase typeI
1N22,Bornyl Diphosphate,isoprenoid synthase typeI
1N23,Bornyl Diphosphate,isoprenoid synthase typeI
1N24,Bornyl Diphosphate,isoprenoid synthase typeI
1PS1,Pentalenene,isoprenoid synthase typeI
1HM4,Pentalenene,isoprenoid synthase typeI
1HM7,Pentalenene,isoprenoid synthase typeI
1JFA,Trichodiene,isoprenoid synthase typeI
1JFG,Trichodiene,isoprenoid synthase typeI
1KIY,Trichodiene,isoprenoid synthase typeI
1KIZ,Trichodiene,isoprenoid synthase typeI
1T47,4-hydroxyphenylpyruvate dioxygenase,vicinal oxygen chelate
1CJX,4-hydroxyphenylpyruvate dioxygenase,vicinal oxygen chelate
1TG5,4-hydroxyphenylpyruvate dioxygenase,vicinal oxygen chelate
1TFZ,4-hydroxyphenylpyruvate dioxygenase,vicinal oxygen chelate
1SQD,4-hydroxyphenylpyruvate dioxygenase,vicinal oxygen chelate
1SP9,4-hydroxyphenylpyruvate dioxygenase,vicinal oxygen chelate
1SQI,4-hydroxyphenylpyruvate dioxygenase,vicinal oxygen chelate
1SP8,4-hydroxyphenylpyruvate dioxygenase,vicinal oxygen chelate
1F1V,3,4-dihydroxyphenylacetate 2,3-dioxygenase,vicinal oxygen chelate
1F1U,3,4-dihydroxyphenylacetate 2,3-dioxygenase,vicinal oxygen chelate
1F1R,3,4-dihydroxyphenylacetate 2,3-dioxygenase,vicinal oxygen chelate
1F1X,3,4-dihydroxyphenylacetate 2,3-dioxygenase,vicinal oxygen chelate
1Q0O,3,4-dihydroxyphenylacetate 2,3-dioxygenase,vicinal oxygen chelate
1Q0C,3,4-dihydroxyphenylacetate 2,3-dioxygenase,vicinal oxygen chelate
1KW9,2,3-dihydroxybiphenyl dioxygenase,vicinal oxygen chelate
1KW8,2,3-dihydroxybiphenyl dioxygenase,vicinal oxygen chelate
1KW6,2,3-dihydroxybiphenyl dioxygenase,vicinal oxygen chelate
1KW3,2,3-dihydroxybiphenyl dioxygenase,vicinal oxygen chelate
1EIL,2,3-dihydroxybiphenyl dioxygenase,vicinal oxygen chelate
1EIR,2,3-dihydroxybiphenyl dioxygenase,vicinal oxygen chelate
1EIQ,2,3-dihydroxybiphenyl dioxygenase,vicinal oxygen chelate
1DHY,2,3-dihydroxybiphenyl dioxygenase,vicinal oxygen chelate
1KWB,2,3-dihydroxybiphenyl dioxygenase,vicinal oxygen chelate
1KWC,2,3-dihydroxybiphenyl dioxygenase,vicinal oxygen chelate
1LKD,2,3-dihydroxybiphenyl dioxygenase,vicinal oxygen chelate
1LGT,2,3-dihydroxybiphenyl dioxygenase,vicinal oxygen chelate
1KNF,2,3-dihydroxybiphenyl dioxygenase,vicinal oxygen chelate
1KND,2,3-dihydroxybiphenyl dioxygenase,vicinal oxygen chelate
1KMY,2,3-dihydroxybiphenyl dioxygenase,vicinal oxygen chelate
1HAN,2,3-dihydroxybiphenyl dioxygenase,vicinal oxygen chelate
1LQP,fosfomycin resistance protein FosA,vicinal oxygen chelate
1LQO,fosfomycin resistance protein FosA,vicinal oxygen chelate
1LQK,fosfomycin resistance protein FosA,vicinal oxygen chelate
1NKI,fosfomycin resistance protein FosA,vicinal oxygen chelate
1NNR,fosfomycin resistance protein FosA,vicinal oxygen chelate
1NPB,fosfomycin resistance protein FosA,vicinal oxygen chelate
1QIP,glyoxalase I,vicinal oxygen chelate
1QIN,glyoxalase I,vicinal oxygen chelate
1FRO,glyoxalase I,vicinal oxygen chelate
1BH5,glyoxalase I,vicinal oxygen chelate
1FA8,glyoxalase I,vicinal oxygen chelate
1FA7,glyoxalase I,vicinal oxygen chelate
1FA6,glyoxalase I,vicinal oxygen chelate
1FA5,glyoxalase I,vicinal oxygen chelate
1F9Z,glyoxalase I,vicinal oxygen chelate""".split("\n")

w = open("output_processado.csv","w")
tmp = ''
for i in range(2,302,2):
	i = round(i/10, 1)
	for j in range(25,225,25):
		j = round(j/100,2)
		tmp += str(i)+'-'+str(j)+','

w.write("arquivo,"+tmp+"pdb,family,superfamily\n")


with open(entrada) as arquivo:
	linhas = arquivo.readlines()

	for linha in linhas:
		celulas = linha.split(',')
		linha_atual = celulas[0]
		nome_pdb = linha_atual[-10:-6].upper()

		for dado in dados:
			dado = dado.replace("2,3-","2_3-").replace("3,4-", "3_4-").replace("1,4-", "1_4-")
			ref = dado.split(',')

			pdb_ref = ref[0]

			if nome_pdb == pdb_ref:
				w.write(linha[:-1]+","+dado+"\n")

