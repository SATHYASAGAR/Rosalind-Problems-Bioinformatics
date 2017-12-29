#Counting Point Mutations

"""
Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
"""

def hamming_distance(lst):
    hamming_distance=0
    for i in range(len(lst[1])-1):
        if lst[0][i]<>lst[1][i]:
            hamming_distance+=1
    return hamming_distance

def main():
    foo=open('rosalind_hamm.txt','r')
    lst = foo.read().strip().split()  
    print hamming_distance(lst)
    foo.close()
    
if __name__ =='__main__':
    main()
    


