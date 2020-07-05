import collections
def one(instr,s):
    n=instr.split(" ")
    return (s+n[1])

def two(instr,s):
    n = instr.split(" ")
    temp=""
    for i in range(len(n[1])):
        temp+=n[1][len(n[1])-1-i]
    return(temp+s)

def palin(s,long):
    res=0
    for i in range(len(s)-long+1):
        de=collections.deque(s[i:i+long])
        de2=collections.deque(s[i:i+long])
        de2.reverse()
        if(de==de2):
            res+=1
    return res

def three(s):
    res=0
    res+=len(s)
    for i in range(2,len(s)):
        res+=palin(s,i)
    if(len(s)!=1):
        de=collections.deque(s)
        de2=collections.deque(s)
        de2.reverse()
        if(de==de2):
            res+=1
    return res

str1=input()
t=int(input())
for i in range(t):
    instr=input()
    if(instr[0]=='1'):
        str1=one(instr,str1)
    elif(instr[0]=='2'):
        str1=two(instr,str1)
    else:
        print(three(str1))
