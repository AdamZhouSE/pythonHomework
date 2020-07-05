m,n= [int(x) for x in input().split()]
li = [int(x) for x in input().split()]
ans = []
for i in range(n):
    start,end=[int(x) for x in input().split()]
    ans.append(str(min(li[start-1:end])))
print(" ".join(ans),end=" ")