t=int(input())
for ex in range(0,t):
    a,b=map(str,input().split(" "))
    i=0
    j=0
    re=0
    while i<len(a) and j<len(b)-1:
        for k in range(j+1,len(b)):
            if a[i]==b[k]:
                j=k
                re+=1
                break
        i+=1
    print(len(a)+len(b)-re)