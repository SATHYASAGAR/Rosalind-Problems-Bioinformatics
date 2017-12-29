#Counting Unrooted Binary Trees

"""
Given: A positive integer nn (n<=1000n<=1000).
Return: The value of b(n) modulo 1,000,000.
"""

def double_fact(n):
    if n==1:
        return 1
    if n<=0:
        return 1
    return n*double_fact(n-2)

def main():
    n=942
    result=double_fact(2*n-5)
    print (result)%1000000
    
if __name__ =='__main__':
    main()