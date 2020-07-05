n=int(input())
lis=list(map(int,input().split(" ")))
s=list(map(int,input().split(" ")))
for i in range(0,len(s)):
    re=[]
    lis[s[i]-1]=-1
    sum=0
    for j in range(0,len(lis)):
        if(lis[j]!=-1):
            sum+=lis[j]
        else:
            re.append(sum)
            sum=0
        if(j==len(lis)-1):
            re.append(sum)
    print(max(re))