#Consensus and Profile

"""
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
"""

foo = open("rosalind_cons.txt",'r')
strt = foo.read()
seq=strt.strip().split('>')
str = []

for s in seq:       #Concatinate all the multiline strings
    if(s!=""):
        all_str=s.split()
        str1=all_str[0]
        str2=''.join(all_str[1:])
        str.append(str2)

        
str_each_ele_len=len(str[1])
j=0
dna_dict={'A':[0], 'C':[0], 'G':[0], 'T':[0]} 

for i in dna_dict:
        for k in range(str_each_ele_len-1):
            dna_dict[i].append(0)

num_parses=str_each_ele_len
i_parse=0

while i_parse<num_parses:
    for i in str:
        while j<str_each_ele_len:
            dna_dict[i[j]][j]+=1
            break
    j+=1
    i_parse+=1


output_str = ''
i_parse=0
j=0   
max_list = []
while i_parse<num_parses:
    for i in dna_dict:
        if j<str_each_ele_len:
            max_list.append(dna_dict[i][j])
    max_val = max(max_list)
    pos = max_list.index(max_val)
    if pos == 0:
        output_str += 'A'
    elif pos == 1:
        output_str += 'C'
    elif pos == 2:
        output_str += 'T'
    else:
        output_str += 'G'
    max_list = []
    j+=1
    i_parse+=1
        
print output_str

for i in dna_dict:
    print i+":",dna_dict[i]