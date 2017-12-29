#Local Alignment with Affine Gap Penalty

"""
Given: Two protein strings ss and tt in FASTA format (each having length at most 10,000 a).
Return: The maximum local alignment score of s and t, followed by substrings r and u of s and t, respectively, that correspond to the optimal local alignment of ss and tt. 
Use:
The BLOSUM62 scoring matrix.
Gap opening penalty equal to 11.
Gap extension penalty equal to 1.
"""

import sys
from Bio import pairwise2
from Bio import SeqIO
from Bio.pairwise2 import format_alignment
from Bio.SubsMat import MatrixInfo as Mat

bs_mat = Mat.blosum62
s1 = input("Enter sequence 1")
s2 = input("Enter sequence 2")
for k in pairwise2.align.localds(s1, s2, bs_mat, -11, -1):
    print(format_alignment(*k))
