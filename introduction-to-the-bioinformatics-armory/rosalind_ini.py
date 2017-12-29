#Introduction to the Bioinformatics Armory

"""
Given: A DNA string s of length at most 1000 bp.
Return: Four integers (separated by spaces) representing the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s. 
Note: You must provide your answer in the format shown in the sample output below.
"""

foo=open("rosalind_ini.txt","r")
s=foo.read()
n={}		#Dictionary to store the count of the symbols in s

for i in s:
	n[i]=s.count(i)		#Store the symbols as Key and Count as value

for key in sorted({'A','C','G','T'}):
	print n[key],

foo.close()