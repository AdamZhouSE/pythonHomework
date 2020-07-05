m,n=map(int,input().split())
A=list(input())
B=list(input())
if m>n:
    print(0)
else:
    k=0
    ans=[]
    for i in range(n-m+1):
        flag=True
        for j in range(i,i+m):
            if A[j-i]=='*' or B[j]=='*':
                continue
            elif A[j-i]!=B[j]:
                flag=False
                break
        if flag:
            ans.append(i)
            k+=1
    print(k)
    for i in ans:
        print(i+1,end=' ')
    print()