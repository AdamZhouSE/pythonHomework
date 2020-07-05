def subsum(result,start,end):
    if start==end:
        if result!="" and sum([int(x) for x in result.split(" ")[:-1]])==0:
            res.append(True)
        else:res.append(False)
    else:
        subsum(result+str(temp[start])+' ',start+1,end)
        subsum(result, start + 1, end)

t=int(input())

for _ in range(t):
    n=int(input())
    temp=[int(x) for x in input().split(" ")]
    res=[]
    subsum("",0,len(temp))
    if res.count(True)>0:print("Yes")
    else:print("No")