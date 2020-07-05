def find(arr:list,target:int,temp:list,ans:list)->list:
    for num in arr:
        if target==0:
            ans.append(temp.copy())
            return ans
        else:
            temp.append(num)
            if target>num:
                ans=find(arr[arr.index(num)+1:],target-num,temp,ans)
            elif target==num:
                ans=find(arr,0,temp,ans)
            temp.remove(num)
    return ans


T=int(input())
for t in range(T):
    n=int(input())
    arr=list(map(int,input().split()))
    s=int(input())
    ans=find(arr,s,[],[])
    print(len(ans))