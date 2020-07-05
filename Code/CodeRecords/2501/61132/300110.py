t = int(input())
l1=input().split()
l2=input().split()
ans=[[1 for j in range(i+1,len(l1)) if l1.index(l2[j])<l1.index(l2[i])] for i in range(len(l1))]
print(map(sum,map(sum,ans)))