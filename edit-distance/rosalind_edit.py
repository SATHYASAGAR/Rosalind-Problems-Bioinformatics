from numpy import zeros

def find_edit_distance(string1,string2):
    M=zeros((len(string1)+1,len(string2)+1), dtype=int)
    for i in xrange(1,len(string1)+1):
        M[i][0]=i
    for j in xrange(1,len(string2)+1):
        M[0][j]=j
    for i in xrange(1,len(string1)+1):
        for j in xrange(1,len(string2)+1):
            if(string1[i-1]!=string2[j-1]):
                M[i][j] = min(M[i - 1][j] + 1, M[i][j - 1] + 1, M[i - 1][j - 1] + 1)
            else:
                M[i][j] = M[i - 1][j - 1]
    return M[len(string1)][len(string2)]

def get_strs_from_input():
    foo = open("rosalind_edit.txt",'r')                   
    seq = foo.read().split(">")            
    strs = []
    for s in seq:
        if(s!=""):
            strings=s.split()
            s_1=strings[0]
            s_2=''.join(strings[1:])
            strs.append(s_2)    
    return strs
    
def main():
    strs=get_strs_from_input()
    string1 = strs[0]
    string2 = strs[1]
    print find_edit_distance(string1,string2)
        
if __name__ =='__main__':
    main()