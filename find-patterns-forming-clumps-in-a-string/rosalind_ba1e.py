#Find Patterns Forming Clumps in a String

"""
Given: A string Genome, and integers k, L, and t.
Return: All distinct k-mers forming (L, t)-clumps in Genome.
"""

foo=open("rosalind_ba1e.txt","r")		#Read input from a file
str=foo.read().splitlines()			
str[1]=str[1].split(' ')				#Create a sub list for k,L and t

#Assign appropriate values from the list to the variables
s=str[0]
k=int(str[1][0])
l=int(str[1][1])
t=int(str[1][2])

l_ind=0				#This variable keeps track of L characters 
chk_str_f_ind=0		#First pointer to the start of k length string
chk_str_s_ind=0		#Second pointer to the end of k length string
count=0
full_str_length=len(s)

D={}		#Dictionary to store the k-mers 

while(l_ind<=full_str_length and chk_str_s_ind<= full_str_length-k):		#First while loop to loop over L characters
	while(chk_str_s_ind<l_ind+l and chk_str_s_ind<= full_str_length-k):		#Second while loop to check for k-mers
		chk_str = s[chk_str_s_ind:chk_str_s_ind+k]
		count = s[l_ind:l_ind+l].count(chk_str)
		if count >= t:
			D[chk_str]=count
		count = 0
		chk_str_s_ind+=1
	chk_str_s_ind=chk_str_f_ind+1
	chk_str_f_ind+=1
	l_ind+=1

for key in D.keys():
	print key,

foo.close()