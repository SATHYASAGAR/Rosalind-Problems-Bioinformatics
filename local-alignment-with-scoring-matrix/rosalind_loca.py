#Local Alignment with Scoring Matrix

"""
Given: Two protein strings s and t in FASTA format (each having length at most 1000 a).
Return: A maximum alignment score along with substrings rr and uu of s and t, respectively, which produce this maximum alignment score (multiple solutions may exist, in which case you may output any one). 
Use:
The PAM250 scoring matrix.
Linear gap penalty equal to 5.
"""

import sys
from Bio import pairwise2                       
from Bio.pairwise2 import f_almt
from Bio.SubsMat import MatrixInfo as Mat

def get_strs_from_input():
    foo = open("rosalind_loca.txt",'r')                   
    seq = foo.read().split(">")            
    strs = []
    for s in seq:
        if(s!=""):
            strings=s.split()
            s_1=strings[0]
            s_2=''.join(strings[1:])
            strs.append(s_2)    
    return strs

def main():
    str = get_strs_from_input()    
    matscores = Mat.pam250
    for k in pairwise2.align.localds(str[0], str[1], matscores, -5, -5):      
        print (f_almt(*k))
    
if __name__ == '__main__':
    main()