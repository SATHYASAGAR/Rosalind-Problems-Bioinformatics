#k-Mer Composition

"""
Given: A DNA string ss in FASTA format (having length at most 100 kbp).
Return: The 4-mer composition of s.
"""

from Bio.Seq import Seq
from itertools import product       #To find the cartesian product of the symbols

foo=open("rosalind_kmer.txt","r")   #Take input from a file
input = foo.read().splitlines()
input = ''.join(input[1:])          #Fetch the dna string

str=''
for i in range(len(input)-3):
    str+= input[i:i+4]+' '          
print str    
dna ="A C G T\n4"                
dna=dna.splitlines()
result= list(product(dna[0].split(' '),repeat = int(dna[1])))   #Find the cartesian product and store the result in a list
result= map(''.join,result)
result.sort()

for i in result:
    print str.count(i),