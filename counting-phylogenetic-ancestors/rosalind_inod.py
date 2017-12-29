#Counting Phylogenetic Ancestors

"""
Given: A positive integer n (3<=n<=10000).
Return: The number of internal nodes of any unrooted binary tree having n leaves."
"""

def main():
    foo = open("rosalind_inod.txt","r")
    input=foo.read()
    print int(input) - 2

if __name__ == '__main__':
    main()                        

