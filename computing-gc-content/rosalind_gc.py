#Computing GC Content

"""
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. 
"""

foo = open('rosalind_gc.txt', 'r')		#Taking input from the file
lines = foo.read()
mystr = lines.splitlines()			
d={}									#Dictionary to store ID and the string

#Store ID as Key and String as Value
for i in mystr:
	if '>' in i:
		j=i.replace('>','')
		d[j]=d.get(i,'')
	else:
		d[j]+=i

#Assume the first element to have highest GC-content
greatest_id=d.keys()[0]
CG_count=d.values()[0].count('C')+d.values()[0].count('G')
greatest_count=float(CG_count)/len(d.values()[0])*100

#Find the ID with highest GC-content
for i in range(len(d)):
	CG_count_i=d.values()[i].count('C')+d.values()[i].count('G')
	tmp_count = float(CG_count_i)/len(d.values()[i])*100
	if tmp_count > greatest_count:
		greatest_id = d.keys()[i]
		greatest_count = tmp_count
		
print greatest_id
print round(greatest_count,6)
foo.close()