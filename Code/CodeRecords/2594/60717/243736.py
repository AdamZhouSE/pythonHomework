n=int(input())

for i in range(0,n):
    strr=input()
    maxx=-1
    for j in range(0,len(strr)):
        for k in range(j,len(strr)):
            if strr[j]==strr[k]:
                maxx=max(k-j-1,maxx)
    print(maxx)
        