#Enumerating k-mers Lexicographically

"""
Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n<=10)
Return: All strings of length n that can be formed from the alphabet, ordered lexicographically.
"""

from itertools import product       #To find the cartesian product of the symbols

input ="T A G C\n4"                #Input for testing
#input=open("rosalind_lexf.txt","r").read()   #Input from a file
input=input.splitlines()

result= list(product(input[0].split(' '),repeat = int(input[1])))   #Find the cartesian product and store the result in a list

result= map(''.join,result)
result.sort()

for ele in result:
    print ele