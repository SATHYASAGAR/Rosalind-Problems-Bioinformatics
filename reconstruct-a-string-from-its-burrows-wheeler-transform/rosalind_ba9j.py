#Reconstruct a String from its burrows-Wheeler Transform

"""
Given: A string Transform (with a single "$" sign).
Return: The string Text such that BWT(Text) = Transform.
"""

def main():
    foo = open("rosalind_ba9j.txt","r")               
    input = foo.read().strip()
    b = [i for i in input]
    sb = sorted(b)
    sb = prepsort(b, sb)            
    for k in range (0,len(b)-2):
        sb = prepsort(b, sb)
    for k in range(0,len(sb)):
        if sb[k][-1] == '$':
            output = sb[k]
    print output

def prepsort(b,sb):                      
    str3 = [b[k] + sb[k] for k in range(0,len(b))]
    str3.sort()
    return str3

if __name__ == '__main__':
    main()