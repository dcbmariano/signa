# ----------------------------------------------------------------------------
# Signa v0.1                                                          | alpha
# ----------------------------------------------------------------------------
# Copyright 2022 by Laboratory of Bioinformatics and Systems (UFMG, Brazil).
# Department of Computer Science - Universidade Federal de Minas Gerais.
# License MIT - https://opensource.org/licenses/MIT
# ----------------------------------------------------------------------------

"""
# ----------------------------------------------------------------------------
  Signa library tool
# ----------------------------------------------------------------------------

Script: signa.py
Contains: functions to deal with strutural signatures of molecules.
Requirements: numpy / scipy

# Simple use:

import signa

signature = open('2lzm.pdb', 'csm')
print(signature)

# Dealing with several PDB files
signa.read_csv('lista.csv', 'csm-hp')


# Biopython context:
from Bio.Signa import signa

# ----------------------------------------------------------------------------
"""

# requirements
import numpy as np
from scipy.spatial import distance


def readFile(filename):
    for line in open(filename):
        yield line

def read_pdb(pdbID):
    """ Read a PDB file """

    residues = []
    atom_name = []
    coords = []

    for line in readFile(pdbID):
        if line[0:4] == 'ATOM':
           coords.append([float(line[31:38]),float(line[39:46]),float(line[47:54])])
           residues.append(line[17:20].strip())
           atom_name.append(line[13:16].strip())

    return atom_name, coords, residues

def read_mmcif():
    pass


def read_csv(csv_file, signa_type = 'csm', output="output.csv", 
    cutoff_limit=10, cutoff_step=0.1, output_csv=True):
    """Read several PDB files
        This function receives a list of PDB files and ]
            returns a CSV with signatures
        Please, include one file per line. 
        For example: "input.csv"
            2lzm.pdb
            1bga.pdb
    """

    print("Running Signa Multi-file")
    print("Signature type: "+signa_type)

    print('...')

    w = open(output, "w")
    i = 'pdb_tmp'

    with open(csv_file) as arquivo:
        linhas = arquivo.readlines()

        for linha in linhas:

            if i != 'pdb_tmp':
                w.write("\n")

            i = linha.strip()

            signature = read(i, signa_type, cutoff_limit, 
                cutoff_step, output_csv)

            w.write(i+",")
            w.write(signature)

    w.close()

    print('Success! Results saved in the file: '+output)


def csm(pdbID, signa_type = 'csm', cutoff_limit=10, 
    cutoff_step=0.1, output_csv=True):

    """ CSM Algorithm
    This function implements the CSM algorithm. 

    Please cite:
        Pires, Douglas EV; de Melo-Minardi, Raquel C; dos Santos, Marcos A;
        da Silveira, Carlos H; Santoro, Marcelo M; Meira, Wagner. 
        Cutoff Scanning Matrix (CSM): structural classification and function 
        prediction by protein inter-residue distance patterns. BMC GENOMICS, 
        v. 12, p. S12, 2011.
    """

    pdbID = pdbID.rstrip()

    k = 0
    sign = ''

    # ------------------------------------------------------------------------
    # Get atoms coords
    # ------------------------------------------------------------------------
    atom_name, coords, residues = read_pdb(pdbID)

    k = len(coords)
    resatom = np.array([residues[x]+atom_name[x] for x in range(k)])
    coords = np.array(coords)
    dist = distance.pdist(coords,metric='euclidean')
    dist = distance.squareform(dist)
    
    # ------------------------------------------------------------------------
    # distance distribution
    # ------------------------------------------------------------------------
   
    for i in np.round(np.arange(cutoff_limit, -cutoff_step, -cutoff_step), 5):

        cutoff_start = 0
        cutoff_end = i

        if cutoff_end < 0:
            break

        # 0: CSM
        if signa_type == 0 or signa_type.lower() == 'CSM'.lower():
            edge_count = int(((dist > cutoff_start) & (dist <= cutoff_end)).sum()/2)
            sign += str(edge_count)+','

                        
    if sign[-1]==',':
        sign = sign[:-1]

    result = [int(s) for s in sign.split(',')]

    if output_csv:
        return sign
    else:
        return np.array(result)


def csm_hp(pdbID, signa_type = 'csm', cutoff_limit=10, cutoff_step=0.1, output_csv=True):
    """ CSM-HP Algorithm
    This function implements the CSM-HP algorithm. 

    Please cite:
        PIRES, D. E. V. ; DE MELO-MINARDI, R. C. ; da Silveira, C. H. ; 
        CAMPOS, F. F. ; Meira, W. . aCSM: noise-free graph-based signatures 
        to large-scale receptor-based ligand prediction. Bioinformatics 
        (Oxford. Print), v. 29, p. 855-861, 2013.
    """

    atoms_hydrophobic = [
        'ALACB', 'ARGCB', 'ARGCG', 'ARGCD', 'ASNCB', 'ASPCB', 
        'CYSCB', 'GLNCB', 'GLNCG', 'GLUCB', 'GLUCG', 'HISCB', 'HISCG',
        'HISCD2', 'HISCE1', 'ILECB', 'ILECG1', 'ILECG2', 'ILECD1', 
        'LEUCB', 'LEUCG', 'LEUCD1', 'LEUCD2', 'LYSCB', 'LYSCG', 'LYSCD', 
        'METCB', 'METCG', 'METCE', 'PHECB', 'PHECG', 'PHECD1', 'PHECD2', 
        'PHECE1', 'PHECE2', 'PHECZ', 'PROCB', 'PROCG', 'PROCD', 'THRCG2', 
        'TRPCB', 'TRPCG', 'TRPCD1', 'TRPCD2', 'TRPCE2', 'TRPCE3', 'TRPCH2', 
        'TRPCZ', 'TRPCZ2', 'TRPCZ3', 'TYRCB', 'TYRCG', 'TYRCD1', 'TYRCD2', 
        'TYRCE1', 'TYRCE2', 'TYRCZ', 'VALCB', 'VALCG1', 'VALCG2'
    ]
    
    atoms_positive = ['ARGNH1', 'ARGNH2', 'HISND1', 'HISNE2', 'LYSNZ']
    
    atoms_negative = ['ASPOD1', 'ASPOD2', 'GLUOE1', 'GLUOE2']
    
    atoms_acceptor = [
        'ALAO', 'ARGO', 'ASNO', 'ASNOD1', 'ASPO', 'ASPOD1', 'ASPOD2', 'CYSO', 
        'GLNO', 'GLNOE1', 'GLUO', 'GLUOE1', 'GLUOE2', 'GLYO', 'HISO', 'ILEO',   
        'LEUO', 'LYSO', 'METO', 'PHEO', 'PROO', 'SERO', 'THRO', 'TRPO', 
        'TYRO', 'VALO'
    ]
    
    atoms_donor = [
        'ALAN', 'ARGN', 'ARGNE', 'ARGNH1', 'ARGNH2', 'ASNN', 'ASNND2', 
        'ASNOD1', 'ASPN', 'CYSN', 'GLNN', 'GLNNE2', 'GLUN', 'GLYN', 'HISN', 
        'HISND1', 'HISNE2', 'ILEN', 'LEUN', 'LYSN', 'LYSNZ', 'METN', 'PHEN', 
        'PRON', 'SERN', 'SEROG', 'THRN', 'THROG1', 'TRPN', 'TRPNE1', 'TYRN', 
        'TYROH', 'VALN'
    ]
    
    atoms_aromatic = [
        'HISCG', 'HISND1', 'HISCD2', 'HISCE1', 'HISNE2', 'PHECG', 'PHECD1', 
        'PHECD2', 'PHECE1', 'PHECE2', 'PHECZ', 'TRPCG', 'TRPCD1', 'TRPCD2', 
        'TRPNE1', 'TRPCE2', 'TRPCE3', 'TRPCZ2', 'TRPCZ3', 'TRPCH2', 'TYRCD1', 
        'TYRCD2', 'TYRCE1', 'TYRCE2', 'TYRCG', 'TYRCZ'
    ]
    
    atoms_sulfur = ['CYSS', 'METSD']

    # ------------------------------------------------------------------------

    atoms_class = {}
    
    for i in atoms_hydrophobic:
        atoms_class[i] = 'Hydro'
    
    for i in atoms_positive:
        atoms_class[i] = 'Pos'
    
    for i in atoms_negative:
        atoms_class[i] = 'Neg'
    
    for i in atoms_acceptor:
        atoms_class[i] = 'Acc'
    
    for i in atoms_donor:
        atoms_class[i] = 'Don'
    
    for i in atoms_aromatic:
        atoms_class[i] = 'Aro'
    
    for i in atoms_sulfur:
        atoms_class[i] = 'Sul'
    

    acsm_all = {
        'Acc': 0,
        'Aro': 1,
        'Don': 2,
        'Hydro': 3, 
        'Neg': 4, 
        'Neutral': 5, 
        'Pos': 6,
        'Sul': 7, 
    }

    pdbID = pdbID.rstrip()

    k = 0
    sign = ''

    # ------------------------------------------------------------------------
    # Get atoms coords
    # ------------------------------------------------------------------------
    atom_name, coords, residues = read_pdb(pdbID)

    k = len(coords)
    resatom = np.array([residues[x]+atom_name[x] for x in range(k)])
    resh = [x in atoms_hydrophobic for x in resatom]
    res_type = np.array([atoms_class.get(x, 'Neutral') for x in resatom])
    coords = np.array(coords)
    dist = distance.pdist(coords,metric='euclidean')
    dist = distance.squareform(dist)
    signa_keys = list(acsm_all.keys())
    
    # ------------------------------------------------------------------------
    # 2 - distance distribution
    # ------------------------------------------------------------------------
   
    for cutoff_temp in np.round(np.arange(cutoff_limit, -cutoff_step, -cutoff_step), 5):

        cutoff_start = 0
        cutoff_end = cutoff_temp

        if cutoff_end < 0:
            break

        # 1: CSM-HP
        elif signa_type == 1 or signa_type.lower() == 'CSM-HP'.lower():

            dist_hh = dist[resh].T[resh]
            edge_count_hh = int(((dist_hh<=cutoff_end)&(dist_hh>cutoff_start)).sum()/2)
            dist_pp = dist[np.invert(resh)].T[np.invert(resh)]
            edge_count_pp = int(((dist_pp<=cutoff_end)&(dist_pp>cutoff_start)).sum()/2)
            dist_hp = dist[resh].T[np.invert(resh)]
            edge_count_hp = ((dist_hp<=cutoff_end)&(dist_hp>=cutoff_start)).sum()
            sign += str(edge_count_hh)+','
            sign += str(edge_count_pp)+','
            sign += str(edge_count_hp)+','

    if sign[-1]==',':
        sign = sign[:-1]

    result = [int(s) for s in sign.split(',')]

    if output_csv:
        return sign
    else:
        return np.array(result)


def acsm(pdbID, signa_type = 'acsm', cutoff_limit=10, cutoff_step=0.1, output_csv=True):
    """ aCSM Algorithm
    This function implements the aCSM algorithm. 

    Please cite:
        PIRES, D. E. V. ; DE MELO-MINARDI, R. C. ; da Silveira, C. H. ; 
        CAMPOS, F. F. ; Meira, W. . aCSM: noise-free graph-based signatures 
        to large-scale receptor-based ligand prediction. Bioinformatics 
        (Oxford. Print), v. 29, p. 855-861, 2013.
    """

    # ------------------------------------------------------------------------
    # Definitions of Atom Types
    # ------------------------------------------------------------------------

    atoms_hydrophobic = [
        'ALACB', 'ARGCB', 'ARGCG', 'ARGCD', 'ASNCB', 'ASPCB', 
        'CYSCB', 'GLNCB', 'GLNCG', 'GLUCB', 'GLUCG', 'HISCB', 'HISCG',
        'HISCD2', 'HISCE1', 'ILECB', 'ILECG1', 'ILECG2', 'ILECD1', 
        'LEUCB', 'LEUCG', 'LEUCD1', 'LEUCD2', 'LYSCB', 'LYSCG', 'LYSCD', 
        'METCB', 'METCG', 'METCE', 'PHECB', 'PHECG', 'PHECD1', 'PHECD2', 
        'PHECE1', 'PHECE2', 'PHECZ', 'PROCB', 'PROCG', 'PROCD', 'THRCG2', 
        'TRPCB', 'TRPCG', 'TRPCD1', 'TRPCD2', 'TRPCE2', 'TRPCE3', 'TRPCH2', 
        'TRPCZ', 'TRPCZ2', 'TRPCZ3', 'TYRCB', 'TYRCG', 'TYRCD1', 'TYRCD2', 
        'TYRCE1', 'TYRCE2', 'TYRCZ', 'VALCB', 'VALCG1', 'VALCG2'
    ]
    
    atoms_positive = ['ARGNH1', 'ARGNH2', 'HISND1', 'HISNE2', 'LYSNZ']
    
    atoms_negative = ['ASPOD1', 'ASPOD2', 'GLUOE1', 'GLUOE2']
    
    atoms_acceptor = [
        'ALAO', 'ARGO', 'ASNO', 'ASNOD1', 'ASPO', 'ASPOD1', 'ASPOD2', 'CYSO', 
        'GLNO', 'GLNOE1', 'GLUO', 'GLUOE1', 'GLUOE2', 'GLYO', 'HISO', 'ILEO',   
        'LEUO', 'LYSO', 'METO', 'PHEO', 'PROO', 'SERO', 'THRO', 'TRPO', 
        'TYRO', 'VALO'
    ]
    
    atoms_donor = [
        'ALAN', 'ARGN', 'ARGNE', 'ARGNH1', 'ARGNH2', 'ASNN', 'ASNND2', 
        'ASNOD1', 'ASPN', 'CYSN', 'GLNN', 'GLNNE2', 'GLUN', 'GLYN', 'HISN', 
        'HISND1', 'HISNE2', 'ILEN', 'LEUN', 'LYSN', 'LYSNZ', 'METN', 'PHEN', 
        'PRON', 'SERN', 'SEROG', 'THRN', 'THROG1', 'TRPN', 'TRPNE1', 'TYRN', 
        'TYROH', 'VALN'
    ]
    
    atoms_aromatic = [
        'HISCG', 'HISND1', 'HISCD2', 'HISCE1', 'HISNE2', 'PHECG', 'PHECD1', 
        'PHECD2', 'PHECE1', 'PHECE2', 'PHECZ', 'TRPCG', 'TRPCD1', 'TRPCD2', 
        'TRPNE1', 'TRPCE2', 'TRPCE3', 'TRPCZ2', 'TRPCZ3', 'TRPCH2', 'TYRCD1', 
        'TYRCD2', 'TYRCE1', 'TYRCE2', 'TYRCG', 'TYRCZ'
    ]
    
    atoms_sulfur = ['CYSS', 'METSD']

    # ------------------------------------------------------------------------

    atoms_class = {}
    
    for i in atoms_hydrophobic:
        atoms_class[i] = 'Hydro'
    
    for i in atoms_positive:
        atoms_class[i] = 'Pos'
    
    for i in atoms_negative:
        atoms_class[i] = 'Neg'
    
    for i in atoms_acceptor:
        atoms_class[i] = 'Acc'
    
    for i in atoms_donor:
        atoms_class[i] = 'Don'
    
    for i in atoms_aromatic:
        atoms_class[i] = 'Aro'
    
    for i in atoms_sulfur:
        atoms_class[i] = 'Sul'
    

    acsm_all = {
        'Acc': 0,
        'Aro': 1,
        'Don': 2,
        'Hydro': 3, 
        'Neg': 4, 
        'Neutral': 5, 
        'Pos': 6,
        'Sul': 7, 
    }

    pdbID = pdbID.rstrip()

    k = 0
    sign = ''

    # ------------------------------------------------------------------------
    # Get atoms coords
    # ------------------------------------------------------------------------
    atom_name, coords, residues = read_pdb(pdbID)

    k = len(coords)
    resatom = np.array([residues[x]+atom_name[x] for x in range(k)])
    resh = [x in atoms_hydrophobic for x in resatom]
    res_type = np.array([atoms_class.get(x, 'Neutral') for x in resatom])
    coords = np.array(coords)
    dist = distance.pdist(coords,metric='euclidean')
    dist = distance.squareform(dist)
    signa_keys = list(acsm_all.keys())
    
    # ------------------------------------------------------------------------
    # 2 - distance distribution
    # ------------------------------------------------------------------------
   
    for cutoff_temp in np.round(np.arange(cutoff_limit, -cutoff_step, -cutoff_step), 5):

        cutoff_start = 0
        cutoff_end = cutoff_temp

        if cutoff_end < 0:
            break

        # 2: aCSM
        elif signa_type == 2 or signa_type.lower() == 'aCSM'.lower():
            for x in range(len(signa_keys)):
                for y in range(x,len(signa_keys)):
                    dist_2 = dist[res_type==signa_keys[x]].T[res_type==signa_keys[y]]
                    if x == y:
                        sign += str(int(((dist_2<=cutoff_end)&(dist_2>cutoff_start)).sum()/2))+','
                    else:
                        sign += str(((dist_2<=cutoff_end)&(dist_2>=cutoff_start)).sum())+','
                        
    if sign[-1]==',':
        sign = sign[:-1]

    result = [int(s) for s in sign.split(',')]

    if output_csv:
        return sign
    else:
        return np.array(result)

def capri():
    """Implements Capri algorithm"""
    pass


def vtr():
    """Implements VTR algorithm"""
    pass


def proteus():
    """Implements Proteus algorithm"""
    pass


def pse():
    """Implements Proteus Search Engine algorithm"""
    pass


def asmc():
    """Implements ASMC algorithm

    Please, cite:
        de Melo-Minardi RC, Bastard K, Artiguenave F. Identification of 
        subfamily-specific sites based on active sites modeling and 
        clustering. Bioinformatics. 2010 Dec 15;26(24):3075-82. 
        doi: 10.1093/bioinformatics/btq595.
    """
    pass


def contacts():
    """Implements contacts calculus"""
    pass


def ssv(pdb1, pdb2, signa_type='acsm', cutoff_limit=10, 
    cutoff_step=0.1, output_csv=False):
    """
        Implements SSV algorithm
        Input: two PDB files
        Output: a float number
        SSV returns the difference between the macromolecules' signatures

        Please, cite: 
            MARIANO, Diego et al. A computational method to propose mutations 
            in enzymes based on structural signature variation (SSV). 
            International journal of molecular sciences, 
            v. 20, n. 2, p. 333, 2019.
    """
    signa_pdb1 = acsm(pdb1, signa_type, cutoff_limit, cutoff_step, output_csv)
    signa_pdb2 = acsm(pdb1, signa_type, cutoff_limit, cutoff_step, output_csv)

    ssv = distance.pdist([signa_pdb1, signa_pdb2], metric='euclidean')

    return ssv[0]


def read(pdbID, signa_type, cutoff_limit = 10, cutoff_step = 0.1, output_csv = True):
    """Function read_pdb()
    This function aims to read ".pdb" files

    PT-BR: Adicionar opção de retornar mapas de distância, 
        mapas de átomos hidrofóbicos, mapas de átomos por tipo
    """

    if signa_type == 'csm' or signa_type == 0:
        return csm(pdbID, signa_type, cutoff_limit, cutoff_step, output_csv)
    
    elif signa_type == 'csm-hp' or signa_type == 1:
        return csm_hp(pdbID, signa_type, cutoff_limit, cutoff_step, output_csv)
    
    elif signa_type == 'acsm' or signa_type == 2:
        return acsm(pdbID, signa_type, cutoff_limit, cutoff_step, output_csv)
    
