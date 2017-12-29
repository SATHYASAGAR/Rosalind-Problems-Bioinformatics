#Construct the Burrows-Wheeler Transform of a String

"""
Given: A string Text.
Return: BWT(Text).
"""

from collections import deque  

def rotate_seq(seq):                          
    d = deque(seq)
    rlist = []
    for k in range(0,len(d)):
        rlist.append(''.join(map(d.rotate(-1),d)))
    return (rlist)

def main():             
    foo = open("rosalind_ba9i.txt","r")                   
    input = foo.read().strip()
    lst = []
    lst.append(input)
    rotated_seq = rotate_seq(input)
    for k in range(0,len(rotated_seq)-1):
        lst.append(rotated_seq[k])
    lst.sort()                       
    bwt = ""
    for k in range(0,len(lst)):        
        bwt = bwt + lst[k][-1:]
    print bwt
    
if __name__ == '__main__':
    main()