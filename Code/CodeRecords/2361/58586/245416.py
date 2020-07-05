arr=list(map(int,input().split(",")))
temp=[]
res=[0]
used=[]
def is_valid(num1,num2):
    temp=pow(num1+num2,0.5)
    return temp==int(temp)
def dfs(arr,pre,temp,res,used):
    if len(arr)==len(temp):
        res[0]+=1
        return
    for i in range(0,len(arr)):
        if len(temp)>0:
            if not is_valid(pre,arr[i]):
                continue
            if i in used:
                continue
            if i>0 and arr[i]==arr[i-1] and i-1 in used:
                continue
        temp.append(arr[i])
        used.append(i)
        pre=arr[i]
        dfs(arr,pre,temp,res,used)
        temp.pop()
        used.pop()

    return
if len(arr)==1:
    if is_valid(0,arr[0]):
        print(1)
    else:
        print(0)
else:
    dfs(arr, 0, temp, res, used)
    print(res[0])