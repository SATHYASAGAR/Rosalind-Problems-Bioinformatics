#Longest Increasing Subsequence

"""
Given: A positive integer n<=10000n<=10000 followed by a permutation of length n.
Return: A longest increasing subsequence of pi, followed by a longest decreasing subsequence of pi.
"""

def remove_same_length_ele(l_lst):
    remove_len=len(l_lst[len(l_lst)-1])
    for i in l_lst[:len(l_lst)-1]:
        if len(i) == remove_len:
            l_lst.remove(i)
    #print "l_lst after removing ",l_lst

foo = open("rosalind_lgis.txt","r")
str1=foo.read().splitlines()
N=str1[0]
input_str_positive=str1[1].split()

input_str_negative=[str(-int(x)) for x in input_str_positive]

for input_str in (input_str_positive,input_str_negative):
    smallest_ele = min(int(s) for s in input_str)
    largest_ele = max(int(s) for s in input_str)
    l_lst=[]
    for i in input_str:
        #print i
        if input_str.index(i)==0:
            l_lst.append([i])
            #print l_lst
        
        elif int(i) == smallest_ele:
            l_lst.append([i])
            #print l_lst
            remove_same_length_ele(l_lst)
                        
        elif int(i) == largest_ele:
            #print "before calc longest_list- l_lst= ",l_lst
            longest_list=max(enumerate(l_lst), key = lambda tup: len(tup[1]))[1]
            #print "longest_list= ",longest_list
            lst=[]
            for k in longest_list:
                lst.append(k)
            l_lst.append(lst)
            l_lst[len(l_lst)-1].append(i)
            #print l_lst
            remove_same_length_ele(l_lst)
            
        else:
            second_largest_ele_list=l_lst[0]
            second_largest_ele=int(l_lst[0][len(l_lst[0])-1])
            for j in l_lst:
                if int(j[len(j)-1])>second_largest_ele and int(j[len(j)-1])<int(i):
                    second_largest_ele_list=[k for k in j]
                    second_largest_ele=int(j[len(j)-1])
            if second_largest_ele > int(i):
                l_lst.append([i])
                #print l_lst                            
            else:
                lst=[]
                for k in second_largest_ele_list:
                    lst.append(k)
                l_lst.append(lst)
                l_lst[len(l_lst)-1].append(i)
                #print l_lst
            remove_same_length_ele(l_lst)
            
    longest_list1=max(enumerate(l_lst), key = lambda tup: len(tup[1]))[1]
    for i in longest_list1:
        print abs(int(i)),
    print