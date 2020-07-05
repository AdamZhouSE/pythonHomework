num=int(input())
arr=[]
set_=set()
list_ans=[]
for i in range(num):
    l=list(input())
    s=set(l)
    for element in s:
        set_.add(element)
    arr.append(l)
n=len(arr)
isX=True
sign=arr[0][0]
flag=arr[0][1]
isTwo=True
if flag==sign:
    isTwo=False
for i in range(n):
    if arr[i][n - i - 1] != sign:
        isX = False
    if arr[i][i] != sign:
        isX = False
    for j in range(n):
        if i!=j and i+j!=n-1 and arr[i][j]!=flag:
            isTwo=False

if isTwo and isX:
    list_ans.append("YES")
else:
    list_ans.append("NO")
print("\n".join(str(i) for i in list_ans))