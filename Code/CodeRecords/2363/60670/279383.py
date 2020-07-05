def bin2int(x):
    n=0
    for c in x:
        n=n*2
        if c=='1':
            n+=1
    return n

def int2bin(x):
    s=''
    while x>0:
        if x%2==0:
            s='0'+s
        else:
            s='1'+s
        x=x//2
    return s

def reverse(x):
    s=''
    for c in x:
        if c=='1':
            s+='0'
        else:
            s+='1'
    return s

n=int(input())
print(bin2int(reverse(int2bin(n))))