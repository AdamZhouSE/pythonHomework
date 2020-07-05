line=input()
arr=[int(i) for i in line]
def isValid(temp):
    sum=0
    for i in range(len(temp)):
        sum=sum*10+temp[i]
    while sum>1:
        if sum%2!=0:
            break
        sum=sum//2
    return sum==1

def dfs(arr,temp,used):
    if len(temp)==len(arr) and isValid(temp):
        return True
    else:
        for i in range(0,len(arr)):
            if len(temp)==0 and arr[i]==0:
                continue
            if i in used:
                continue
            else:
                temp.append(arr[i])
                used.append(i)
                if dfs(arr,temp,used):
                    return True
                temp.pop()
                used.pop()
        return False
if dfs(arr,[],[]):
    print("true")
else:
    print("false")


