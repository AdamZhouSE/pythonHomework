n=int(input())
for i in range(0,n):
    str1=str(input())
    str1=sorted(str1)
    res=0
    j=0
    while(j<=len(str1)-1):
        res+=str1.count(str1[j])-1
        j+=str1.count(str1[j])
    print(res)