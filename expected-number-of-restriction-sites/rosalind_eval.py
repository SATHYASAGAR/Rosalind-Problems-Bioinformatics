#Expected Number of Restriction Sites

"""
Given: A positive integer nn (n<=1,000,000<=1,000,000), a DNA string s of even length at most 10, and an array A of length at most 20, containing numbers between 0 and 1.
Return: An array B having the same length as AA in which B[i]B[i] represents the expected number of times that s will appear as a substring of a random DNA string t of length n, where t is formed with GC-content A[i].
"""

from numpy import log, exp

def main():
    foo = open("rosalind_eval.txt","r")
    input = foo.read().strip().split('\n')
    n = int(input[0]);string = input[1];k = input[2]
    gc_inp = k.split(" ")
    for i in gc_inp:
        gc_count = float(i)
        g_count = string.count("G")
        a_count = string.count("A")
        c_count = string.count("C")
        t_count = string.count("T")
        print round(exp(log(gc_count/2)*(g_count+c_count) + log((1-gc_count)/2)*(a_count+t_count))*(n-1),3),

if __name__ == '__main__':
    main()
    
#refrence : Peer discussion