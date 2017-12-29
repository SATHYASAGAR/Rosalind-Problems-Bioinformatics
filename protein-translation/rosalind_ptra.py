#Protein Translation

"""
Given: A DNA string s of length at most 10 kbp, and a protein string translated by s.
Return: The index of the genetic code variant that was used for translation. (If multiple solutions exist, you may return any one.)
"""

import sys
from Bio.Seq import translate

foo=open("rosalind_ptra.txt","r")
str=foo.read().splitlines()
s=str[0]
protein_str=str[1]

for i in [1,2,3,4,5,6,9,10,11,12,13,14,15]:		#loop through the list of table numbers
	if translate(s, table=i, to_stop=True) == protein_str:
		index=i
		print index
		sys.exit()
		
print "Table not found"		#If in case no solution is found
foo.close()