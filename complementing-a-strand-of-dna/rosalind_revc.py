#Complementing a Strand of DNA

"""
Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement s.
"""

foo=open("rosalind_revc.txt","r")
s=foo.read()
rev_complement=''

for i in s:
	if i=='A':
		rev_complement+='T'
		
	elif i=='T':
		rev_complement+='A'
		
	elif i=='C':
		rev_complement+='G'
		
	elif i=='G':
		rev_complement+='C'
			
	else:
		rev_complement+=i

rev_complement=rev_complement[::-1]
print rev_complement
foo.close()
		