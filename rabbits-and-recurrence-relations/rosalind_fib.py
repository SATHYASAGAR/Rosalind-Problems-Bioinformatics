#Rabbits and Recurrence Relations

"""
Given: Positive integers n<=40n<=40 and k<=5k<=5.
Return: The total number of rabbit pairs that will be present after nn months if we begin with 1 pair and in each generation, 
every pair of reproduction-age rabbits produces a litter of kk rabbit pairs (instead of only 1 pair).
"""

def fibo(n,k):
    return 1 if n==1 or n==2 else fibo(n-1,k)+k*fibo(n-2,k)

foo=open("rosalind_fib.txt","r")        #Take input from a file
str=foo.read().split()

n=int(str[0]); k=int(str[1])
print fibo(n,k)

foo.close()