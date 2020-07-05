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
for i in range(n):
    if arr[i][i]!=sign:
        isX=False
        break
for i in range(n):
    if arr[i][n-i-1]!=sign:
        isX=False
        break
isTwo=True
if len(set_)>2:
    isTwo=False
if isTwo and isX:
    list_ans.append("YES")
else:
    list_ans.append("NO")
print("\n".join(str(i) for i in list_ans))