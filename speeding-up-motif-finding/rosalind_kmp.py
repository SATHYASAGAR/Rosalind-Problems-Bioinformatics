#Speeding Up Motif Finding

"""
Given: A DNA string s (of length at most 100 kbp) in FASTA format.
Return: The failure array of s.
"""

foo = open("rosalind_kmp.txt",'r')
strt = foo.read()
seq=strt.strip().split('>')
str = []

        
for s in seq:       #Concatinate all the multiline strings
    if(s!=""):
        all_str=s.split()
        str1=all_str[0]
        str2=''.join(all_str[1:])
        str.append(str2)
str= str[0]

failure_array=[]
for i in range(len(str)):
    failure_array.append(0)
s_pos = 1; substr_pos = 0 
while s_pos < len(str):
    if str[s_pos] == str[substr_pos]:
        substr_pos += 1
        failure_array[s_pos] = substr_pos
        s_pos = s_pos + 1
    elif substr_pos<>0:
        substr_pos = failure_array[substr_pos-1]
    else:
        failure_array[s_pos] = 0
        s_pos = s_pos + 1

for i in failure_array:
    print i,

