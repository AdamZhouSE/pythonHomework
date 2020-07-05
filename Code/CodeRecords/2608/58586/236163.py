
def dfs(res,input,output,start,end):
    if isList(output) and output not in res:
        res.append(output)
    for i in range(start,end):
        if len(output)==0:
            if not isValid(input[i]):
                continue
        output+=input[i]
        dfs(res,input,output,i+1,end)
        output=output[:-1]
        

def isValid(c):
    list=['a','e','i','o','u']
    return c in list

def isList(str):
    if len(str)==0:
        return False
    last=len(str)-1
    return isValid(str[0]) and not isValid(str[last])

nums=int(input())
for i in range(nums):
    lines=input()
    res=[]
    dfs(res,lines,"",0,len(lines))
    if(len(res)==0):
        print(-1)
    else:
        res.sort()
        for i in range(len(res)):
            print(res[i],end='')
            if not i==len(res)-1:
                print(' ',end='')
        print()
    


