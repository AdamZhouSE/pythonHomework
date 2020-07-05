def getkeyvalue(c):
    x=arr.count(c)
    return x
arr=eval(input())
# arr=eval("[1,1,2,2,2]")
arr=sorted(arr,key=getkeyvalue,reverse=True)
ans=[arr[0]]
arr.pop(0)
while len(arr)!=0:
    for i in range(len(arr)):
        if arr[i]!=ans[-1]:
            ans.append(arr[i])
            arr.pop(i)
            break
print(ans)