import collections
s=input()
maxLetters=eval(input())
minSize=eval(input())
maxSize=eval(input())
n=len(s)
subS=collections.defaultdict(int)
if minSize>maxSize:
    print(0)
else:
    res=0
    for i in range(n-minSize+1):
        temp=s[i:i+minSize]
        letters=set(temp)
        if len(letters)<=maxLetters:
            subS[temp]+=1
            res=max(res,subS[temp])
    print(res)