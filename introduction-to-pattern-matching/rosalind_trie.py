from itertools import count

class T(object):
    def __init__(self):
        self.counter = count(start=1)
        self.start_node = [next(self.counter), {}]

    def insert_new(self, str):
        node = self.start_node
        for i in str:
            if i not in node[1]:
                node[1][i] = [next(self.counter), {}]
            node = node[1][i]

def add_node(strs):
    trie = T()
    for str in strs:
        trie.insert_new(str)
    return trie.start_node


def recursive_print(node):
    for i, node2 in node[1].iteritems():
        print node[0], node2[0], i
        recursive_print(node2)

foo = open("rosalind_trie.txt").readlines()
    
str = [k.strip() for k in foo if k.strip()]
    
recursive_print(add_node(str))




    

    
