def A(ls):
    s=[0,0,0]
    min=10000
    for i in range(len(ls)-1):
        j=i+1
        while j<len(ls):
            if j!=i:
                if abs(ls[i]-ls[j])<min:
                    min=abs(ls[i]-ls[j])
                    s[0]=i
                    s[1]=j
                    s[2]=min
            j=j+1
    return s

N=int(input())
ls=input().split(" ")
ls=[int(x) for x in ls]
result=0
while len(ls)>0:
    s=A(ls)
    result=result+s[2]
    del ls[s[0]]
    del ls[s[1]-1]
print(result)


