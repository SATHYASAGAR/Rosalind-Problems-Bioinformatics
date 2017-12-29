#Constructing a De Bruijn Graph

"""
Given: A collection of up to 1000 DNA strings of equal length (not exceeding 50 bp) corresponding to a set SS of (k+1)(k+1)-mers.
Return: The adjacency list corresponding to the de Bruijn graph corresponding to str Union Src.
"""

from Bio.Seq import Seq

def get_input_from_file(file_name):
    foo = open(file_name,"r")               
    return foo.readlines()    

def det_adj_lst(str,str1):
    for k in range(len(str)):
        p = str[k][:-1]
        q = str[k][1:]
        pq = (p,q)
        str1.append(pq)
    return str1

def det_adj_lst_srv(str,x,str1):
    for k in range(len(str)):                 #Using set to determine adjcency list and to idenotify unique sets.
        r = x[k][:-1]
        str = x[k][1:]
        rs = (r, str)
        str1.append(rs)
    return str1
    
def main():
    input = get_input_from_file("rosalind_dbru.txt")
    str = []
    for k in input:
        str.append(k.strip())
    x = []
    for k in str:                             
        a = Seq(k)
        x.append("%s" %a.reverse_complement())
    a = []
    b = []
    a=det_adj_lst(str,a)
    b=det_adj_lst_srv(str,x,b)
    result = set(a)                 
    result.update(b)
    for (a,b) in sorted(result):            
        print '(%s, %s)' %(a,b)
    
if __name__ == '__main__':
    main()