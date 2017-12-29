#FASTQ format introduction

"""
Given: FASTQ file
Return: Corresponding FASTA records
"""

from Bio import SeqIO

foo=open("rosalind_tfsq.txt", "r")
SeqIO.convert(foo,'fastq','FASTArecords.txt','fasta')
foo.close()