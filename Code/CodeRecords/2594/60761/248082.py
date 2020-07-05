def maxBetweenSame(string):
    letterset=set(string)
    letterlist=list(string)
    n=0
    if(len(letterset)==len(letterlist)):
        return "-1"
    else:
        for i in range(len(string)-1):
            if(string[i+1:].count(string[i])>0):
                j=len(string)-1
                while(string[j]!=string[i]):
                    j-=1
                n=max(n,j-i-1)  
        return n

n=int(input())
for i in range(n):
    string=input()
    print(maxBetweenSame(string.lower()))
