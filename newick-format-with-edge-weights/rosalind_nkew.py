#Newick Format with Edge Weights

"""
Given: A collection of nn weighted trees (n<=40n<=40) in Newick format, with each tree containing at most 200 nodes; 
each tree Tk is followed by a pair of nodes xkxk and ykyk in TkTk.
Return: A collection of nn numbers, for which the kkth number represents the distance between xkxk and yk in Tk.
"""

from StringIO import StringIO
from Bio import Phylo

def print_collection(lst):
    for s, t in lst:
        k, j = t.split()
        tree = Phylo.read(StringIO(s), 'newick')
        print (int(tree.distance(k, j))),
    return

def main():
    foo = open("rosalind_nkew.txt", "r")
    lst=[]
    for k in foo.read().strip().split('\n\n'):
        lst.append(k.split('\n'))
    print_collection(lst)
    
if __name__ == '__main__':
    main()
