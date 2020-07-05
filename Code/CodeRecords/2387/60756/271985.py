line1=input().split()
n=int(line1[0])
m=int(line1[1])
arr=list(map(int,input().split()))
for i in range(m):
    s=list(map(int,input().split()))
    arr[s[1]-1:s[2]]=sorted(arr[s[1]-1:s[2]],reverse=(s[0]==1))
print(arr[int(input())-1])