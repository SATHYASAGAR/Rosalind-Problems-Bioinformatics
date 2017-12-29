#Finding a Protein Motif

"""
Given: At most 15 UniProt Protein Database access IDs.
Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations 
in the protein string where the motif can be found.
"""

import urllib
import re

def list_motif_loc(id,str1,regexp):
    lst=[] 
    for i in range(len(str1)-4):
        m = re.search(regexp,str1[i:i+4])
        if m is not None:
            lst.append(m.group(0))
    if len(lst)>0:
        print id
        for i in lst:
            print str1.find(i)+1,
        print 

if __name__ =='__main__':
    regexp='N[^P][ST][^P]'
    foo=open("rosalind_mprt.txt","r")
    input=foo.read().splitlines()
    for id in input:
        url="http://www.uniprot.org/uniprot/"+id+".fasta"
        filehandle = urllib.urlopen(url)
        str=filehandle.read().splitlines()
        str1=''
        for i in str[1:]:
            str1+=i

        list_motif_loc(id,str1,regexp)
        
    foo.close()