#Locating Restriction Sites

"""
Given: A DNA string of length at most 1 kbp in FASTA format.
Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.
"""

from Bio.Seq import Seq                         
from Bio.Alphabet import generic_dna as g_dna

def get_strs_from_input():
    foo = open("rosalind_revp.txt",'r')                   
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
    str = get_strs_from_input()[0]
    output = [];pos_1 = [];pos_2 = []
    r1=4; r2=13
    for i in range(r1, r2):                      
        for k in range(0, len(str)-i+1):
            s = str[k:k + i]
            x = Seq(s,g_dna)
            if x == x.reverse_complement():
                pos_1.append(k+1); pos_2.append(i); output.append(x)
    for k in range(len(pos_1)):             
        print pos_1[k],pos_2[k]
    
if __name__ == '__main__':
    main()