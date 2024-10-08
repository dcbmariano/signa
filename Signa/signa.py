# -----------------------------------------------------------------------------
# SIGNA | stable
# -----------------------------------------------------------------------------
# Copyright 2024 by Laboratory of Bioinformatics and Systems | Diego Mariano
# Department of Computer Science: Universidade Federal de Minas Gerais, Brazil
# License MIT - https://opensource.org/licenses/MIT
# -----------------------------------------------------------------------------
version = 'Signa v1.3'
"""
# ----------------------------------------------------------------------------
  Signa library 
# ----------------------------------------------------------------------------

Script: signa.py
Contains: functions to deal with strutural signatures of molecules.
Requirements: numpy / scipy

# Simple use:

import Signa.signa as signa

signature = signa.read('2lzm.pdb', 'SIGNA-CHARGE')
print(signature)

# Dealing with multiple PDB files
signa.read_csv('lista.csv', 'acsm_hp')

# signa_type supported: signa_charge, csm, acsm, csm_hp, csm_all
# cumulative: True or False

# ----------------------------------------------------------------------------
"""

# requirements
import numpy as np
from scipy.spatial import distance


def readFile(filename):
    for line in open(filename):
        yield line

def read_pdb(pdbID, atom='ALL', chain='ALL'):
    """ Read a PDB file """

    residues = []
    atom_name = []
    coords = []

    for line in readFile(pdbID):
        if line[0:4] == 'ATOM':
            if atom=='CA':  # only alpha carbon
                atom_tmp = line[13:16].strip()
                if atom_tmp != 'CA':
                    continue
            if chain != 'ALL': # only one chain allowed
                chain_tmp = line[21]
                if chain_tmp.upper() != chain.upper():
                    continue
            coords.append([float(line[31:38]),float(line[39:46]),float(line[47:54])])
            residues.append(line[17:20].strip())
            atom_name.append(line[13:16].strip())

    return atom_name, coords, residues

def read_mmcif(pdbID, atom='ALL', chain='ALL'):
    """ Read a MMCIF file """
    residues = []
    atom_name = []
    coords = []

    for line in readFile(pdbID):
        if line[0:4] == 'ATOM':
            line = line.split() # basic support to mmcif; works in most cases
            atom_id = int(line[1])
            atom_name_current = line[3] # atom name for the current atom
            res_name = line[5] # 3 letter code
            chain_name = line[6] # atom chain
            res_id = int(line[8]) # amino acid residue id
            x = float(line[10]) # coord x
            y = float(line[11]) # coord y
            z = float(line[12]) # coord z

            if atom=='CA':  # only alpha carbon
                if atom_name_current != 'CA':
                    continue
            if chain != 'ALL': # only one chain allowed
                if chain_name.upper() != chain.upper():
                    continue
            coords.append([x, y, z])
            residues.append(res_name)
            atom_name.append(atom_name_current)

    return atom_name, coords, residues

def read_folder(folder, signa_type = 'csm', output="output.csv", 
    cutoff_limit=20, cutoff_step=0.2, output_csv=True, verbose=True, chain='ALL', forcefield='AMBER', separator=',', cumulative=True, format='pdb'):
    """Read several PDB files in a folder"""
    if verbose:
        print("Running Signa Multi-file | folder")
        print("Signature type: "+signa_type)
        print('...')

    w = open(output, "w")
    i = 'pdb_tmp'

    import glob

    directory = glob.glob(folder+"/*."+format)
    
    cont = 0
    for pdb_file in directory:

        signature = read(pdb_file, signa_type, cutoff_limit, cutoff_step, output_csv, chain, verbose, cumulative, separator, forcefield)

        w.write(pdb_file+separator)
        w.write(signature+"\n")

        cont+=1
        if verbose:
            print(cont,'/',len(directory),'-',i)

    w.close()

    print('Success! Results saved in the file: '+output)

def read_csv(csv_file, signa_type = 'csm', output="output.csv", 
    cutoff_limit=20, cutoff_step=0.2, output_csv=True, verbose=True, chain='ALL', forcefield='AMBER', separator=',', cumulative=True):
    """Read several PDB files
        This function receives a list of PDB files and ]
            returns a CSV with signatures
        Please, include one file per line. 
        For example: "input.csv"
            2lzm.pdb
            1bga.pdb
    """
    if verbose:
        print("Running Signa Multi-file")
        print("Signature type: "+signa_type)
        print('...')

    w = open(output, "w")
    i = 'pdb_tmp'

    with open(csv_file) as arquivo:
        
        linhas = arquivo.readlines()
        cont = 0
        for linha in linhas:

            if i != 'pdb_tmp':
                w.write("\n")

            i = linha.strip()

            signature = read(i, signa_type, cutoff_limit, cutoff_step, output_csv, chain, verbose, cumulative, separator, forcefield)

            w.write(i+separator)
            w.write(signature)
            cont+=1
            if verbose:
                print(cont,'/',len(linhas),'-',i)

    w.close()

    print('Success! Results saved in the file: '+output)


def csm(pdbID, signa_type = 'csm', cutoff_limit=20, cutoff_step=0.2, output_csv=True, chain='ALL', verbose=True, cumulative=True, separator=',', format='PDB'):
    """ aCSM Algorithm
    This function implements the aCSM algorithm. 

    signa_type => 
      - csm
      - acsm
      - acsm_hp
      - acsm_all

    Please cite:
        PIRES, D. E. V. ; DE MELO-MINARDI, R. C. ; da Silveira, C. H. ; 
        CAMPOS, F. F. ; Meira, W. . aCSM: noise-free graph-based signatures 
        to large-scale receptor-based ligand prediction. Bioinformatics 
        (Oxford. Print), v. 29, p. 855-861, 2013.

        Pires, Douglas EV; de Melo-Minardi, Raquel C; dos Santos, Marcos A;
        da Silveira, Carlos H; Santoro, Marcelo M; Meira, Wagner. 
        Cutoff Scanning Matrix (CSM): structural classification and function 
        prediction by protein inter-residue distance patterns. BMC GENOMICS, 
        v. 12, p. S12, 2011.
    """
    if verbose:
        print('---------------------------------')
        print('Signature algorithm:',signa_type)
        print('CUTOFF:',cutoff_limit)
        print('STEP:', cutoff_step)
        print('PDB:', pdbID)
        print('---------------------------------')
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

    for atoms, class_name in [  # create an acronymous
        (atoms_hydrophobic, 'Hydro'),
        (atoms_positive, 'Pos'),
        (atoms_negative, 'Neg'),
        (atoms_acceptor, 'Acc'),
        (atoms_donor, 'Don'),
        (atoms_aromatic, 'Aro'),
        (atoms_sulfur, 'Sul')
    ]:
        atoms_class.update({atom: class_name for atom in atoms})
    
    acsm_all = {
        'Acc': 0, 'Aro': 1, 'Don': 2, 'Hydro': 3, 'Neg': 4, 'Neutral': 5, 'Pos': 6, 'Sul': 7, 
    }

    pdbID = pdbID.rstrip()

    k = 0
    sign = ''

    # ------------------------------------------------------------------------
    # Get atoms coords
    # ------------------------------------------------------------------------
    if signa_type == 'csm':
        if format.upper() == 'PDB':
            atom_name, coords, residues = read_pdb(pdbID, atom='CA', chain=chain)
        elif format.upper() == 'MMCIF' or format.upper() == 'CIF' or format.upper() == 'PDBX':
            atom_name, coords, residues = read_mmcif(pdbID, atom='CA', chain=chain)
    else:
        if format.upper() == 'PDB':
            atom_name, coords, residues = read_pdb(pdbID, chain=chain)
        elif format.upper() == 'MMCIF' or format.upper() == 'CIF' or format.upper() == 'PDBX':
            atom_name, coords, residues = read_mmcif(pdbID, chain=chain)

    if len(atom_name) == 0:
        print('No match found.')
        exit()
    #
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

        if cumulative:
            cutoff_start = 0
        else:
            cutoff_start = cutoff_temp - cutoff_step
        
        cutoff_end = cutoff_temp

        if cutoff_end <= 0: # if cutoff_end < 0:  # correct bug include +1 column
            break

        # 0: CSM
        if signa_type == 0 or signa_type.lower() == 'acsm' or signa_type.lower() == 'csm':
            edge_count = int(((dist > cutoff_start) & (dist <= cutoff_end)).sum()/2)
            sign += str(edge_count)+separator
        
        # 1: CSM-HP
        elif signa_type == 1 or signa_type.lower() == 'acsm_hp' or signa_type.lower() == 'acsm-hp':

            dist_hh = dist[resh].T[resh]
            edge_count_hh = int(((dist_hh<=cutoff_end)&(dist_hh>cutoff_start)).sum()/2)
            dist_pp = dist[np.invert(resh)].T[np.invert(resh)]
            edge_count_pp = int(((dist_pp<=cutoff_end)&(dist_pp>cutoff_start)).sum()/2)
            dist_hp = dist[resh].T[np.invert(resh)]
            edge_count_hp = ((dist_hp<=cutoff_end)&(dist_hp>=cutoff_start)).sum()
            sign += str(edge_count_hh)+separator
            sign += str(edge_count_pp)+separator
            sign += str(edge_count_hp)+separator

        # 2: aCSM
        elif signa_type == 2 or signa_type.lower() == 'acsm_all' or signa_type.lower() == 'acsm-all':
            for x in range(len(signa_keys)):
                for y in range(x,len(signa_keys)):
                    dist_2 = dist[res_type==signa_keys[x]].T[res_type==signa_keys[y]]
                    if x == y:
                        sign += str(int(((dist_2<=cutoff_end)&(dist_2>cutoff_start)).sum()/2))+separator
                    else:
                        sign += str(((dist_2<=cutoff_end)&(dist_2>=cutoff_start)).sum())+separator
                        
    if sign[-1] == separator:
        sign = sign[:-1]

    result = [int(s) for s in sign.split(separator)]

    if output_csv:
        return sign
    else:
        return np.array(result)

def contacts():
    """Implements contacts calculation
        Use: python Signa/plugins/contacts.py
    """
    print("Please, use: 'from Signa import contacts'")
    pass


def ssv(pdb1, pdb2, signa_type='acsm_all', cutoff_limit=10, 
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
    signa_pdb1 = csm(pdb1, signa_type, cutoff_limit, cutoff_step, output_csv)
    signa_pdb2 = csm(pdb1, signa_type, cutoff_limit, cutoff_step, output_csv)

    ssv = distance.pdist([signa_pdb1, signa_pdb2], metric='euclidean')

    return ssv[0]


def read(pdbID, signa_type='csm', cutoff_limit = 20, cutoff_step = 0.2, output_csv = True, chain='ALL', verbose=True, cumulative=True, separator=",", forcefield='AMBER', format='PDB', show_labels=False):
    """Function read_pdb()
    This function aims to read ".pdb" files

    PT-BR: Adicionar opção de retornar mapas de distância, 
        mapas de átomos hidrofóbicos, mapas de átomos por tipo
    """
    if signa_type.lower() == 'signa_charge' or signa_type.lower() == 'signa-charge':
        return signa_charge(pdbID, forcefield, chain, separator, verbose, cutoff_limit, cutoff_step, cumulative, format)
    elif signa_type.lower() == 'signa-elemental' or signa_type.lower() == 'signa_elemental':
        return signa_elemental(pdbID, chain, separator, verbose, cutoff_limit, cutoff_step, cumulative, format, show_labels)
    else:
        return csm(pdbID, signa_type, cutoff_limit, cutoff_step, output_csv, chain, verbose, cumulative, separator, format)
    

def labels(signa_type='acsm', cutoff_limit = 20, cutoff_step = 0.2, separator = ',', cumulative=True):
    ''' 
    *   Return labels for acsm, acsm-hp, and acsm-all 
    *   
    *   acsm: if cumulative, returns 10.0-0, 9.8-0, ..., 0.2-0.0
    *         else: returns 10.0-9.8, 9.8-9.6, ..., 0.2-0  
    *
    *   acsm-hp: 'hydrophobic x hydrophobic', 'polar x polar', 'hydrophobic x polar'
    *
    *   acsm-all: [
    *               'acceptor', 'donor', 'aromatic', 'hydrophobic', 
    *               'negative', 'neutral', 'positive', 'sulfide'
    *             ] 
    *             # (all-versus-all: acc x don, acc x aro, ..., sul x sul)
    * 
    *   Example: signa.labels('acsm_all', 10, 0.2)
    *   Returns: acceptor x acceptor (10.0-9.8),acceptor x donor (10.0-9.8) ...
    *            positive x sulfide (0.2-0.0),sulfide x sulfide (0.2-0.0)
    '''

    header = ''
    acsm_hp_classes = ['hydrophobic x hydrophobic', 'polar x polar', 'hydrophobic x polar']
    acsm_all_classes = ['acceptor', 'aromatic', 'donor', 'hydrophobic', 'negative', 'neutral', 'positive', 'sulfide']
    # 'Acc': 0, 'Aro': 1, 'Don': 2, 'Hydro': 3, 'Neg': 4, 'Neutral': 5, 'Pos': 6, 'Sul': 7, 

    for i in range(cutoff_limit*100, 0, -1*int(cutoff_step*100)):

        i = i/100 # min cutoff value = 0.01

        if cumulative:
            end=0
        else:
            end = round(i-cutoff_step,1)
        if signa_type == 'csm':
            header += str(i)+'-'+str(end) + separator
        if signa_type == 'acsm':
            header += str(i)+'-'+str(end)+separator
        elif signa_type == 'acsm_hp' or signa_type == 'acsm-hp':
            for x in acsm_hp_classes:
                header += str(x)+' ('+str(i)+'-'+str(end)+')'+separator
        elif signa_type == 'acsm_all' or signa_type == 'acsm-all': 
            for x in range(len(acsm_all_classes)):
                for y in range(x,len(acsm_all_classes)):
                    header += acsm_all_classes[x]+' x '+acsm_all_classes[y]+' ('+str(i)+'-'+str(end)+')'+separator
    if signa_type.upper() == 'SIGNA-CHARGE':
        for i in range(int(cutoff_step*100), (cutoff_limit*100)+int(cutoff_step*100), int(cutoff_step*100)):
            i = i/100
            for j in range(25,201,25):
                j = j/100
                header += str(round(i,2))+"_"+str(round(j,2))+separator

    header = header[:-1] # remove the last separator ','

    return header


def signa_charge(pdbID, forcefield="AMBER", chain="ALL", separator=',', verbose=True, cutoff_limit=30, cutoff_step=0.2, cumulative=True, format='PDB'):
    """ Calculates de structural signature: SIGNA-CHARGE """

    # forcefield values [0]=>AMBER [1] CHARMM | data obtained from nApoli
    ff_values = {
        "ALA:N": [-0.4157, -0.47], "ALA:CA": [0.0337, 0.07], "ALA:C": [0.5973, 0.51], "ALA:O": [-0.5679, -0.51], "ALA:CB": [-0.1825, -0.27], "ARG:N": [-0.3479, -0.47], "ARG:CA": [-0.2637, 0.07], "ARG:C": [0.7341, 0.51], "ARG:O": [-0.5894, -0.51], "ARG:CB": [-0.0007, -0.18], "ARG:CG": [0.039, -0.18], "ARG:CD": [0.0486, 0.2], "ARG:NE": [-0.5295, -0.7], "ARG:CZ": [0.8076, 0.64], "ARG:NH1": [-0.8627, -0.8], "ARG:NH2": [-0.8627, -0.8], "ASN:N": [-0.4157, -0.47], "ASN:CA": [0.0143, 0.07], "ASN:C": [0.5973, 0.51], "ASN:O": [-0.5679, -0.51], "ASN:CB": [-0.2041, -0.18], "ASN:CG": [0.713, 0.55], "ASN:OD1": [-0.5931, -0.55], "ASN:ND2": [-0.9191, -0.62], "ASP:N": [-0.5163, -0.47], "ASP:CA": [0.0381, 0.07], "ASP:C": [0.5366, 0.51], "ASP:O": [-0.5819, -0.51], "ASP:CB": [-0.0303, -0.28], "ASP:CG": [0.7994, 0.62], "ASP:OD1": [-0.8014, -0.76], "ASP:OD2": [-0.8014, -0.76], "CYS:N": [-0.4157, -0.47], "CYS:CA": [0.0213, 0.07], "CYS:C": [0.5973, 0.51], "CYS:O": [-0.5679, -0.51], "CYS:CB": [-0.1231, -0.11], "CYS:SG": [-0.3119, -0.23], "GLN:N": [-0.4157, -0.47], "GLN:CA": [-0.0031, 0.07], "GLN:C": [0.5973, 0.51], "GLN:O": [-0.5679, -0.51], "GLN:CB": [-0.0036, -0.18], "GLN:CG": [-0.0645, -0.18], "GLN:CD": [0.6951, 0.55], "GLN:OE1": [-0.6086, -0.55], "GLN:NE2": [-0.9407, -0.62], "GLU:N": [-0.5163, -0.47], "GLU:CA": [0.0397, 0.07], "GLU:C": [0.5366, 0.51], "GLU:O": [-0.5819, -0.51], "GLU:CB": [0.056, -0.18], "GLU:CG": [0.0136, -0.28], "GLU:CD": [0.8054, 0.62], "GLU:OE1": [-0.8188, -0.76], "GLU:OE2": [-0.8188, -0.76], "GLY:N": [-0.4157, -0.47], "GLY:CA": [-0.0252, -0.02], "GLY:C": [0.5973, 0.51], "GLY:O": [-0.5679, -0.51], "HIS:N": [-0.4157, -0.47], "HIS:CA": [0.0188, 0.07], "HIS:C": [0.5973, 0.51], "HIS:O": [-0.5679, -0.51], "HIS:CB": [-0.0462, -0.09], "HIS:CG": [-0.0266, -0.36], "HIS:ND1": [-0.3811, 0.32], "HIS:CD2": [0.1292, 0.22], "HIS:CE1": [0.2057, 0.25], "HIS:NE2": [-0.5727, -0.7], "ILE:N": [-0.4157, -0.47], "ILE:CA": [-0.0597, 0.07], "ILE:C": [0.5973, 0.51], "ILE:O": [-0.5679, -0.51], "ILE:CB": [0.1303, -0.09], "ILE:CG1": [-0.043, -0.18], "ILE:CG2": [-0.3204, -0.27], "ILE:CD1": [-0.066, -0.27], "LEU:N": [-0.4157, -0.47], "LEU:CA": [-0.0518, 0.07], "LEU:C": [0.5973, 0.51], "LEU:O": [-0.5679, -0.51], "LEU:CB": [-0.1102, -0.18], "LEU:CG": [0.3531, -0.09], "LEU:CD1": [-0.4121, -0.27], "LEU:CD2": [-0.4121, -0.27], "LYS:N": [-0.3479, -0.47], "LYS:CA": [-0.24, 0.07], "LYS:C": [0.7341, 0.51], "LYS:O": [-0.5894, -0.51], "LYS:CB": [-0.0094, -0.18], "LYS:CG": [0.0187, -0.18], "LYS:CD": [-0.0479, -0.18], "LYS:CE": [-0.0143, 0.21], "LYS:NZ": [-0.3854, -0.3], "MET:N": [-0.4157, -0.47], "MET:CA": [-0.0237, 0.07], "MET:C": [0.5973, 0.51], "MET:O": [-0.5679, -0.51], "MET:CB": [0.0342, -0.18], "MET:CG": [0.0018, -0.14], "MET:SD": [-0.2737, -0.09], "MET:CE": [-0.0536, -0.22], "PHE:N": [-0.4157, -0.47], "PHE:CA": [-0.0024, 0.07], "PHE:C": [0.5973, 0.51], "PHE:O": [-0.5679, -0.51], "PHE:CB": [-0.0343, -0.18], "PHE:CG": [0.0118, 0], "PHE:CD1": [-0.1256, -0.115], "PHE:CD2": [-0.1256, -0.115], "PHE:CE1": [-0.1704, -0.115], "PHE:CE2": [-0.1704, -0.115], "PHE:CZ": [-0.1072, -0.115], "PRO:N": [-0.2548, -0.29], "PRO:CA": [-0.0266, 0.09], "PRO:C": [0.5896, 0.51], "PRO:O": [-0.5748, -0.51], "PRO:CB": [-0.007, 0.09], "PRO:CG": [0.0189, 0.02], "PRO:CD": [0.0192, 0], "SER:N": [-0.4157, -0.47], "SER:CA": [-0.0249, 0.07], "SER:C": [0.5973, 0.51], "SER:O": [-0.5679, -0.51], "SER:CB": [0.2117, 0.05], "SER:OG": [-0.6546, -0.66], "THR:N": [-0.4157, -0.47], "THR:CA": [-0.0389, 0.07], "THR:C": [0.5973, 0.51], "THR:O": [-0.5679, -0.51], "THR:CB": [0.3654, 0.14], "THR:OG1": [-0.6761, 0.09], "THR:CG2": [-0.2438, -0.66], "TRP:N": [-0.4157, -0.47], "TRP:CA": [-0.0275, 0.07], "TRP:C": [0.5973, 0.51], "TRP:O": [-0.5679, -0.51], "TRP:CB": [-0.005, -0.18], "TRP:CG": [-0.1415, -0.03], "TRP:CD1": [-0.1638, -0.15], "TRP:CD2": [0.1243, 0.14], "TRP:NE1": [-0.3418, -0.51], "TRP:CE2": [0.138, 0.24], "TRP:CE3": [-0.2387, 0.16], "TRP:CZ2": [-0.1134, 0.17], "TRP:CZ3": [-0.1972, 0.14], "TRP:CH2": [-0.1134, 0.17], "TYR:N": [-0.4157, -0.47], "TYR:CA": [-0.0014, 0.07], "TYR:C": [0.5973, 0.51], "TYR:O": [-0.5679, -0.51], "TYR:CB": [-0.0152, -0.18], "TYR:CG": [-0.0011, 0], "TYR:CD1": [-0.1906, -0.115], "TYR:CD2": [-0.1906, -0.115], "TYR:CE1": [-0.2341, -0.115], "TYR:CE2": [-0.2341, -0.115], "TYR:CZ": [0.3226, 0.11], "TYR:OH": [-0.5579, -0.54], "VAL:N": [-0.4157, -0.47], "VAL:CA": [-0.0875, 0.07], "VAL:C": [0.5973, 0.51], "VAL:O": [-0.5679, -0.51], "VAL:CB": [0.2985, -0.09], "VAL:CG1": [-0.3192, -0.27], "VAL:CG2": [-0.3192, -0.27]
    }

    if forcefield.upper() == "AMBER":
        ff_value = { i:j[0] for i,j in ff_values.items() }
    elif forcefield.upper() == "CHARMM":
        ff_value = { i:j[1] for i,j in ff_values.items() }

    # Step 1 - dist | distance matrix -----------------------------------------
    if format.upper() == 'PDB':
        atom_name, coords, residues = read_pdb(pdbID, chain=chain)
    elif format.upper() == 'MMCIF' or format.upper() == 'CIF' or format.upper() == 'PDBX':
        atom_name, coords, residues = read_mmcif(pdbID, chain=chain)

    if len(atom_name) == 0:
        print('No match found.')
        exit()
        
    k = len(coords)
    resatom = np.array([residues[x]+":"+atom_name[x] for x in range(k)])
    coords = np.array(coords)
    dist = distance.pdist(coords,metric='euclidean')
    dist = distance.squareform(dist)  # distance matrix

    # Step 2 - cdm | charge difference matrix ---------------------------------
    cdm = []

    ci = 0 # aux counters
    for i in resatom:
        cdm.append([]) # append an empty array
        cj = 0 # aux counters
        for j in resatom:
            cdm[ci].append(-1)  # initial value
            try: # returns the module of the difference => dc = |c2 - c1|
                cdm[ci][cj] = abs(round(ff_value[j] - ff_value[i],2))
            except:
                cdm[ci][cj] = 0  # if the atom charge wasn't found, difference = 0
            cj+=1
        ci+=1

    cdm = np.array(cdm)
    #np.set_printoptions(threshold=np.inf) # limit print np array

    # Step 3 - charge difference distribution based on atoms distances --------
    dmax = cutoff_limit; dmin = 0; dstp = cutoff_step  # distance cutoff
    cmax = 2; cmin = 0; cstp = 0.25  # charge cutoff: 8 groups

    cont = []  # counting the number of atom pairs

    #dist => distance matrix / cdm => charge difference matrix
    for d in np.arange(dmin + dstp, dmax + dstp, dstp):
        for e in np.arange(cmin + cstp, cmax + cstp, cstp):
            if cumulative:
                c = (dist <= d) & (cdm < e) & (cdm >= e-cstp)
            else:
                c = (dist <= d) & (dist > d-dstp) & (cdm < e) & (cdm >= e-cstp)

            cont.append(int(c.sum()/2)) # este código não remove o átomo-referência da contagem

    sign = ''
    for c in cont:
        sign+=str(c)+separator

    sign = sign[:-1] # structural signature

    return sign

def dist(x1,y1,z1,x2,y2,z2):
    """ Returns the Euclidian distance; input (6 numeric values): x1,y1,z1,x2,y2,z2 """
    return ((x1 - x2)**2 + (y1-y2)**2 + (z1-z2)**2)**(1/2)

def signa_elemental(pdbID, chain="ALL", separator=',', verbose=True, cutoff_limit=6, cutoff_step=0.2, cumulative=True, format='PDB', show_labels=False):
    """ Calculates de structural signature: SIGNA-ELEMENTAL 
        SigEl uses the following atoms as default: CNOS + X (any other atom)
    """

    # Step 1 - dist | distance matrix -----------------------------------------
    if format.upper() == 'PDB':
        atom_name, coords, residues = read_pdb(pdbID, chain=chain)
    elif format.upper() == 'MMCIF' or format.upper() == 'CIF' or format.upper() == 'PDBX':
        atom_name, coords, residues = read_mmcif(pdbID, chain=chain)

    signature = {}
    #elements = ["C", "N", "P", "O", "S", "F", "Cl", "Br", "I", "B"]
    elements = ["C", "N", "O", "S", "X"]

    #converter angstroms para nanometros
    cmax = int(cutoff_limit * 10)
    cstep = int(cutoff_step * 10)

    # create signature matrix empty
    for d in range(cstep, cmax, cstep):
        signature[d] = {}
        for i2 in range(len(elements)):
            for j2 in range(len(elements)):
                i = elements[i2]
                j = elements[j2]
                if j2 < i2:
                    continue # remove diagonal
                signature[d][i+j] = 0

    # read pdb/pdbx file
    if format.upper() == 'PDB':
        atom_name, coords, residues = read_pdb(pdbID, chain=chain)
    elif format.upper() == 'MMCIF' or format.upper() == 'CIF' or format.upper() == 'PDBX':
        atom_name, coords, residues = read_mmcif(pdbID, chain=chain)

    # calculates the distances
    for i2 in range(len(coords)):
        for j2 in range(len(coords)):
            i = coords[i2]
            j = coords[j2]

            if j2 < i2:
                continue # remove diagonal

            d = dist(i[0], i[1], i[2], j[0], j[1], j[2])
            atom1 = atom_name[i2]
            atom2 = atom_name[j2]

            if atom1 not in elements:
                atom1 = "X"
            if atom2 not in elements:
                atom2 = "X"

            for intervalo in range(cstep, cmax, cstep):
                dtmp = d*10 # angstroms => nanometros

                if dtmp > intervalo-cstep and dtmp <= intervalo:
                    try:
                        signature[intervalo][atom1 + atom2] += 1
                    except:
                        signature[intervalo][atom2 + atom1] += 1

    sig = ""

    for a in signature:
        labels = signature[a].keys()
        for i in signature[a]:
            sig += str(signature[a][i])+","

    sig = sig[:-1]

    # print labels
    if show_labels:
        header = ""
        for i in range(cstep, cmax, cstep):
            for j in labels:
                header += j+":"+str((i-cstep)/10)+"-"+str(i/10)+","
        header = header[:-1]
        print(header)

    return sig