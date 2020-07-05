def test(a,b):
    for i in range(len(a)):
        if a[i]=="*" or b[i]=="*":
            continue
        elif a[i]!=b[i]:
            return False
    return True
m,n = [int(x) for x in input().split()]
if n<m:
    print(0)
    exit()
arr1 = input()
arr2 = input()
cnt=0
ans=[]
for i in range(n-m+1):
    if test(arr1,arr2[i:i+m]):
        ans.append(i+1)
        cnt+=1
print(cnt)
print(*ans,end=" \n")