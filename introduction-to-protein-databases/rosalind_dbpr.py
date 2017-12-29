#Introduction to Protein Databases

"""
Given: The UniProt ID of a protein.
Return: A list of biological processes in which the protein is involved (biological processes are found in a subsection of the protein's "Gene Ontology" (GO) section).
"""

import urllib

def list_biological_processes(str):
    for ele in str:
        if " P:" in ele:
            print ele.split(';')[2][3:]

def main():   
    foo=open("rosalind_dbpr.txt","r")
    input = foo.readline()
    url='http://www.uniprot.org/uniprot/'+input.rstrip()+'.txt'
    filehandle = urllib.urlopen(url)
    str = filehandle.read().rstrip().splitlines()
    list_biological_processes(str)
    foo.close()
        
if __name__ =='__main__':
    main()