#Finding a Shared Motif

"""
Given: A collection of k (k<=100k<=100) DNA strings of str_len at most 1 kbp each in FASTA format.
Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
"""

import operator

def get_all_substr(str):
    str_len = len(str)
    return [str[i:j+1] for i in range(str_len) for j in range(i,str_len)]

def get_longest_substr(str):
    lst=[]      #Holds all the substrings of first DNA string
    lst=get_all_substr(str[0])
    no_common_lst=[]        #Holds all the substrings of first DNA string which is not present in other DNA strings
    
    #logic to populate no_common_lst[]
    for i in lst:
        for j in str[1:]:
            if i not in j:
                no_common_lst.append(i)
                break
    
    common_lst=list(set(lst)-set(no_common_lst))        #Holds the common substrings in all the DNA strings
    
    #logic to find the substring with max length
    d={}
    for i in common_lst:
        d[i]=len(i)
    return max(d.iteritems(), key=operator.itemgetter(1))[0]
    
    
if __name__ =='__main__':
    foo = open("rosalind_lcsm.txt",'r')
    strt = foo.read()
    seq=strt.strip().split('>')
    str = []        #Holds all the DNA strings
    
    #logic to populate str[]
    for s in seq:
        if(s!=""):
            all_str=s.split()
            str1=all_str[0]
            str2=''.join(all_str[1:])
            str.append(str2)
    
    print get_longest_substr(str)  
    foo.close()
    

