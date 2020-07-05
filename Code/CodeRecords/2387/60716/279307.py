def operation_A(temp:list):
    l,r = temp[1],temp[2]
    lis = [lists[ele] for ele in range(l,r+1)]
    lis.sort()
    if temp[0]==1:
        lis.reverse()
    keys = [lists[t] if t<l or t>r else lis[t-l] for t in range(n)]
    lists = keys

n,m = map(int,input().split())
str1 = input().split()
lists = [int(i) for i in str1]
for i in range(m):
    strtemp = input().split()
    operalist = [int(j) for j in strtemp]
    operation_A(operalist)
q = int(input())
print(lists[q-1])