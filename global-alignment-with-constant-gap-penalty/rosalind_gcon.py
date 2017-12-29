#Global Alignment with Constant Gap Penalty

"""
Given: Two protein strings s and t in FASTA format (each of length at most 1000 aa).
Return: The maximum alignment score between s and t. Use:
The BLOSUM62 scoring matrix.
Constant gap penalty equal to 5.
"""

from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SubsMat import MatrixInfo as Metrices

def get_strs_from_input():
    foo = open("rosalind_gcon.txt",'r')                   
    seq = foo.read().split(">")   
    print seq
    strs = []
    for s in seq:
        if(s!=""):
            strings=s.split()
            s_1=strings[0]
            s_2=''.join(strings[1:])
            strs.append(s_2)    
    return strs

def compute_max_alignment_score(s,t,constant_gap_penalty,linear_gap_penalty):
    for x in pairwise2.align.globalds(s, t, Metrices.blosum62, constant_gap_penalty, linear_gap_penalty):
        print(format_alignment(*x))
        return

def main():
    strs=get_strs_from_input()
    print strs
    string1 = strs[0]
    string2 = strs[1]
    linear_gap_penalty=0
    constant_gap_penalty=-5
    compute_max_alignment_score(string1,string2,constant_gap_penalty,linear_gap_penalty)    
        
if __name__ == '__main__':
    main()