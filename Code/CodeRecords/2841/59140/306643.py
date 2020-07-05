def Xenia(flag, res):
    if len(res)==1:
        return res[0]
    else:
        if flag:
            t=[]
            for i in range(0,len(res),2):
                t.append(res[i]|res[i+1])
            res=t.copy()
            return Xenia(False,res)
        else:
            t = []
            for i in range(0, len(res), 2):
                t.append(res[i] ^ res[i + 1])
            res = t.copy()
            return Xenia(True,res)

temp=[int(x) for x in input().split(" ")]
n,m=temp[0],temp[1]
arr=[int(x) for x in input().split(" ")]

for _ in range(m):
    temp = [int(x) for x in input().split(" ")]
    arr[temp[0]-1]=temp[1]
    res=arr.copy()
    print(Xenia(True,res))