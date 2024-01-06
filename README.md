<img src="./docs/img/header.png">

# Quickstart
<code>python quickstart.py</code>

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
~~~
import signa

signature = signa.read('2lzm.pdb', 'csm')
print(signature)

#Dealing with several PDB files
signa.read_csv('lista.csv', 'csm-hp')
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
~~~
import signa

signature = signa.read('2lzm.pdb', 'signa-charge')
print(signature)

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