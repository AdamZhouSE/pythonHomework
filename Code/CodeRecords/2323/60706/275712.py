list1=input().split(',')
A=[]
for i in range(len(list1)):
    A.append(int(list1[i]))
K=int(input())
ans=max(max(A) - min(A) - 2*K, 0)
print(ans)