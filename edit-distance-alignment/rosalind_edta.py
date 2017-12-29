#Edit Distance Alignment

"""
Given: Two protein strings s and t in FASTA format (with each string having length at most 1000 a).
Return: The edit distance dE(s,t)dE(s,t) followed by two augmented strings s′ and t′ representing an optimal alignment of s and t.
"""

import sys                                  
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

def get_strs_from_input():
    foo = open("rosalind_edta.txt",'r')                   
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
    algmnts = pairwise2.align.localds(str[0], str[1])            
    print(format_alignment(*algmnts[0]))
    
if __name__ == '__main__':
    main()
