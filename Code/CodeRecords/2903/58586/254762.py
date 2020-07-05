arr=eval(input())
def isValid(string):
    temp=[]
    flag=True
    for s in string:
        if s not in temp:
            temp.append(s)
        else:
            flag=False
            break
    return flag
ans=[0]
def getLen(arr):
    length=0
    for s in arr:
        length+=len(s)
    return length
length=getLen(arr)
def dfs(arr,string,start,ans,length):
    if not isValid(string):
        return
    ans[0]=max(ans[0],len(string))
    if len(string)==length:
        return
    for i in range(len(arr)):
        dfs(arr,string+arr[i],i+1,ans,length)
dfs(arr,"",0,ans,length)
print(ans[0])