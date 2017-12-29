#Data Formats

"""
Given: A collection of n (n<=10n<=10) GenBank entry IDs.
Return: The shortest of the strings associated with the IDs in FASTA format.
"""

from Bio import Entrez
from Bio import SeqIO

def return_least_index(strs):
    len_lst=[]
    for i in strs:
        len_lst.append(len(i.seq))
    min_len=min(len_lst)
    k=0
    for ele in strs:
        if len(ele)==min_len:
            min_i=k
        k+=1
    return min_i
    
def main():
    foo=open('rosalind_frmt.txt','r')
    lst = foo.read().strip().split()
    Entrez.email = 'sathyasagar.68@gmail.com'
    strs = list(SeqIO.parse(Entrez.efetch(db='nucleotide', id=lst, rettype='fasta'), 'fasta'))
    f_h = Entrez.efetch(db='nucleotide', id=lst, rettype='fasta')
    print f_h.read().strip().split('\n\n')[return_least_index(strs)]
    foo.close()    

if __name__ =='__main__':
    main()