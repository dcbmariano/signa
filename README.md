# Signa

**Quickstart:** 
<code>python example.py</code>


## EN
Welcome to Signa library source code.

Signa reimplements a series of methods for building structural signatures based on work carried out by researchers at the Bioinformatics and Systems Laboratory of the Department of Computer Science at the <i>Universidade Federal de Minas Gerais</i>.

Signa was developed using the Python language, which guarantees a simple and friendly syntax, in addition to high performance and a fast running time.

### Signatures and methods available
- CSM
- aCSM
- CSM-HP
- SSV
- VTR
- Proteus
- PSE
- Contacts
- and many others

### Simple use:
~~~
import signa

signature = open('2lzm.pdb', 'csm')
print(signature)

#Dealing with several PDB files
signa.read_csv('lista.csv', 'csm-hp')
~~~

## PT-BR
Bem-vindo(a) ao código-fonte da biblioteca Signa.

Signa reimplementa uma série de métodos para construção de assinaturas estruturais com base em trabalhos realizados por pesquisadores do Laboratório de Bioinformática e Sistemas do Departamento de Ciência da Computação da Universidade Federal de Minas Gerais. 

Signa foi desenvolvido utilizando a linguagem Python, o que garante uma sintaxe simples e amigável, além de alta performance e um rápido tempo de execução.


### Como usar Signa em seus scripts Python?
~~~
import signa

signature = open('2lzm.pdb', 'csm')
print(signature)

#Para processar múltiplos arquivos PDB, use:
signa.read_csv('lista.csv', 'csm-hp')
~~~

### Assinaturas e métodos disponíveis

- CSM
- aCSM
- CSM-HP
- SSV
- VTR
- Proteus
- PSE
- Contacts
- E muito mais