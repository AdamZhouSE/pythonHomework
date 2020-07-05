def subUnion(res,str,start,end,i,b):
    if i==str.__len__():
        b=start+b+end
        res.append(b)
        return
    subUnion(res,str,start,end,i+1,b)
    b=b+str[i]
    subUnion(res,str,start,end,i+1,b)

n=int(input())
i=0
res=list()
while i<n:
    resPart = list()
    str=input()
    length=str.__len__()
    j=0
    while j<length:
        if str[j]=='a' or str[j]=='e' or str[j]=='i' or str[j]=='o' or str[i]=='u':
            k=j+1
            while k<length:
                if str[k]=='a' or str[k]=='e' or str[k]=='i' or str[k]=='o' or str[k]=='u':
                    k=k+1
                    continue
                else:
                    subUnion(resPart,str[j+1:k],str[j],str[k],0,"")
                    k=k+1
        j=j+1
    i=i+1
    resPart.sort()
    res.append(resPart)
i=0

while i<n:
    if res[i].__len__()==0:
        print(-1)
    else:
        j=0
        while j<res[i].__len__():
            if j!=0:
                if res[i][j]!=res[i][j-1]:
                    print(" ",end="")
                else:
                    j=j+1
                    continue
            print(res[i][j],end="")
            j=j+1
        print()
    i=i+1