#Distances in Trees

import sys
import re

def print_collection(p):
    for q, r in p:                                                    
        r = r.split()
        smbls = iter(re.split('([(),])', q))                                 
        while next(smbls) not in r:
            pass
        count_1 = 0; count_2 = 0                                                                  
        for y in smbls:                                                       
            if y in r:
                break
            if y in ',)':
                if count_2 > 0:
                    count_2 -= 1
                else:
                    count_1 += 1
            if y in ',(':
                count_2 += 1
        cnt_sum=count_1+count_2
        print cnt_sum       

def main():
    foo = open('rosalind_nwck.txt', 'r')                                                  
    p = [z.split('\n') for z in foo.read().strip().split('\n\n')]           
    print_collection(p)        
        
if __name__ == '__main__':
    main()    
    
    
#Reference - Discussed with peers in class