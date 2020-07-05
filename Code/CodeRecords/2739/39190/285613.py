def cal1(target,k,index,path,res):
    if target==0 and len(path)==k:
        res.append(path)
        return
    if path and target <path[-1]:
        return
    for i in range(index,10):
        cal1(target-i,k,i+1,path+[i],res)

def func(k,n):
    result=list()
    cal1(n,k,1,list(),result)
    print(result)

ip=input("")
func(int(ip[0]),int(ip[-1]))