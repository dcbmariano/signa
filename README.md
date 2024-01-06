<img src="./docs/img/header.png">

# Quickstart
<code>python quickstart.py</code>

## docs
- <a href="#signa-docs-en">Documentation in English</a>
- <a href="#signa-docs-pt-br">Documentação em Português (PT-BR)</a>

## Signa Docs (EN)

Welcome to Signa library source code.

Signa reimplements a series of methods for building structural signatures based on work carried out by researchers at the Bioinformatics and Systems Laboratory of the Department of Computer Science at the <i>Universidade Federal de Minas Gerais</i>.

Signa was developed using the Python language, which guarantees a simple and friendly syntax, in addition to high performance and a fast running time.

Requirements: 
- Numpy
- Scipy

### What does Signa do?
<img src="./docs/img/about.png">


### Simple use:

Clone the repository using the command-line terminal, GitHub Desktop, or click the <code>Code > Download ZIP</code> button. Next, install the library and then import signa into your Python script (we do not provide support for the installation process).

However, the **fastest way to test Signa** is to copy the <code>signa.py</code> file (it is inside the Signa folder) to the same directory as your PDB files (to test, copy the file <code>2lzm.pdb</code> that is inside <code>docs/examples</code>). Then create a python file in the same directory and add the following command:

~~~
import signa

signature = signa.read('2lzm.pdb', 'signa-charge')
print(signature)
~~~

The signa.read() function accepts the following parameters:

~~~
def read(
     pdbID,             # address and name of the input PDB file
     signa_type='csm',  # signature type, can be: signa-charge, csm, acsm, acsm-all, acsm-hp
     cutoff_limit = 30, # maximum search limit radius
     cutoff_step = 0.2, # value of the search interval
     output_csv = True, # saves the result as a csv file
     chain='ALL',       # filters the chain from the pdb file
     verbose=True,      # displays messages on the screen while the program runs
     cumulative=True,   # cumulative or non-cumulative signatures
     separator=","",    # output file separator
     forcefield='AMBER' # forcefield used in signa-charge
)
~~~

To handle multiple files, add the PDB file names into a CSV file (one per line). Then use the following command:

~~~
import signa

#To process multiple PDB files, use:
signa.read_csv('lista.csv', 'signa-charge')
~~~

### How to calculate contacts?
The contact calculation script is inside the Signa directory. You can run it as follows:

~~~
python contacts.py [file-name].pdb [optional: -hb -hy -ar -re -at -sb -db -csv]
~~~

Optional parameters:

-hb hydrogen bonds  
-hy hydrophobic  
-ar aromatic         
-re repulsive 
-at attractive      
-sb salt bridge 
-db disulfide bonds  
-csv (save as csv) 

If no parameter is entered, SIGNA-contacts will calculate all contacts.

### Signatures and methods available
- SIGNA-CHARGE
- CSM
- aCSM
- aCSM-HP
- aCSM-ALL
- SSV
- Contacts



## Signa Docs (PT-BR)
Bem-vindo(a) ao código-fonte da biblioteca Signa.

Signa reimplementa uma série de métodos para construção de assinaturas estruturais com base em trabalhos realizados por pesquisadores do Laboratório de Bioinformática e Sistemas do Departamento de Ciência da Computação da Universidade Federal de Minas Gerais. 

Signa foi desenvolvido utilizando a linguagem Python, o que garante uma sintaxe simples e amigável, além de alta performance e um rápido tempo de execução.

Requisitos: 
- Numpy
- Scipy

### Para que serve a biblioteca Signa?
<img src="./docs/img/about.png">
Signa converte a estrutura tridimensional de uma macromolécula em um vetor numérico usando diversos tipos de assinaturas estruturais.

### Como usar Signa em seus scripts Python?

Clone o repositório usando o terminal de linhas de comando, GitHub Desktop ou clique no botão <code>Code > Download ZIP</code>. Em seguida, faça a instalação da biblioteca e depois importe signa para seu script Python (não fornecemos suporte para o processo de instalação). 

Entretanto, a maneira **mais rápida de testar Signa** é copiando o arquivo <code>signa.py</code> (ele está dentro da pasta Signa) para o mesmo diretório dos seus arquivos PDB (para testar, copie o arquivo <code>2lzm.pdb</code> que está dentro de <code>docs/examples</code>). Em seguida, crie um arquivo python no mesmo diretório e adicione o comando a seguir:

~~~
import signa

entry = '2lzm.pdb'
signature = signa.read(entry, 'signa-charge')
print(signature)
~~~

A função signa.read() aceita os seguintes parâmetros:

~~~
def read(
    pdbID,                  # endereço e nome do arquivo PDB de entrada
    signa_type='csm',       # tipo de assinatura, pode ser: signa-charge, csm, acsm, acsm-all, acsm-hp
    cutoff_limit = 30,      # raio máximo de limite de busca
    cutoff_step = 0.2,      # valor do intervalo de busca
    output_csv = True,      # salva o resultado como um arquivo csv
    chain='ALL',            # filtra a cadeia do arquivo pdb 
    verbose=True,           # exibe mensagens na tela enquanto o programa roda
    cumulative=True,        # assinaturas cumulativas ou não cumulativas
    separator=",",          # separador do arquivo de saída
    forcefield='AMBER'      # campo de força usado em signa-charge
)
~~~

Para lidar com múltiplos arquivos, adicione os nomes dos arquivos PDB em um arquivo CSV (um por linha). Em seguida, use o seguinte comando:

~~~
import signa

#Para processar múltiplos arquivos PDB, use:
signa.read_csv('lista.csv', 'signa-charge')
~~~

### Como fazer um cálculo de contatos?
O script de cálculo de contatos está dentro do diretório Signa. Você pode executá-lo da seguinte forma:

~~~
python contacts.py [file-name].pdb [optional: -hb -hy -ar -re -at -sb -db -csv]
~~~

Parâmetros opcionais:

-hb hydrogen bonds  
-hy hydrophobic  
-ar aromatic         
-re repulsive 
-at attractive      
-sb salt bridge 
-db disulfide bonds  
-csv (save as csv) 

Se nenhum parâmetro for informado, SIGNA irá calcular todos os contatos.

### Assinaturas e métodos disponíveis

- SIGNA-CHARGE
- CSM
- aCSM
- aCSM-HP
- aCSM-ALL
- SSV
- Contacts

<hr>

## Signa by Laboratório de Bioinformática e Sistemas
Contributions by:
- [Diego Mariano](https://github.com/dcbmariano)
- Eduardo Utsch Madureira Moreira
- [Frederico Chaves Carvalho](https://github.com/fccarvalho2)
- Lucas Moraes
- Raquel Cardoso de Melo Minardi
- and many others.