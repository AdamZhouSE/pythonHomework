def dfs(expre,tar,tmp,curres,preres,res:list):
    if tar==curres and len(expre)==0:
        res.append(tmp)
        return

    for i in range(1,len(expre)+1):
        cur=expre[0:i]
        if(len(cur)>1 and cur[0]=='0'):
            return
        curnum=int(cur)
        next=expre[i:]
        if not len(tmp):
            # it's first num
            dfs(next,tar,cur,curnum,curnum,res)
        else:
            dfs(next,tar,tmp+"+"+cur,curres+curnum,curnum,res)
            dfs(next,tar,tmp+"-"+cur,curres-curnum,-curnum,res)
            dfs(next,tar,tmp+"*"+cur,(curres-preres)+preres*curnum,preres*curnum,res)

def addOperator(expre,tar):
    res=[]
    dfs(expre,tar,"",0,0,res)
    return res

expre=input()
tar=int(input())
print(addOperator(expre,tar))