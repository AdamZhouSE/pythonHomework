def judge(lis):
    sum=0
    for i in range(0,len(lis)):
        for j in range(0,len(lis[i])):
            sum=sum+int(lis[i][j])
    if sum%3==0:
        return 1
    else:
        return 0

n=int(input())
ans=[]
for i in range(0,n):
    input()
    s=input().split()
    ans.append(judge(s))

for i in ans:
    print(i)