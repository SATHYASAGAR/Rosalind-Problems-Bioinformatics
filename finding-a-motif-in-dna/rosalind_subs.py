#Finding a Motif in DNA

"""
Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of tt as a substring of s.
"""

#Open the file and read data into two strings
foo=open("rosalind_subs.txt","r")
strt=foo.read().splitlines()
DNA_str1=strt[0]
DNA_str2=strt[1]

pos=[]      #The list 'pos' holds the location of the substr in the main string

DNA_str2_len=len(DNA_str2)

for i in range(len(DNA_str1)-DNA_str2_len+1):
    if DNA_str1[i:i+DNA_str2_len]==DNA_str2:
        pos.append(i+1)

for i in pos:
    print i,
    
foo.close()