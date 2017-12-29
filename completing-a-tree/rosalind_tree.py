#Completing a Tree

"""
Given: A positive integer n (n<=1000n<=1000) and an adjacency list corresponding to a graph on n nodes that contains no cycles.
Return: The minimum number of edges that can be added to the graph to produce a tree.
"""

foo = open("rosalind_tree.txt")
input=foo.readlines()
print(int(input[0])-len(input))
foo.close()