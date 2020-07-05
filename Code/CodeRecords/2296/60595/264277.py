def Test():
    n,root=map(int,input().split())
    eages=[]
    d={}
    for i in range(0, n):
        eages.append(eval("[" + input().strip().replace(" ", ",") + "]"))
    sum=int(input())
    def zuTree(eages, root):
        zu = [0 for _ in range(0, 1000)]
        zu[1] = root
        for x in eages:
            father = x[0]
            leftson = x[1]
            rightson = x[2]
            d[x[0]]=x[3]
            i = zu.index(father)
            left = 2 * i
            right = 2 * i + 1
            zu[left] = leftson
            zu[right] = rightson
        return zu
    zu=zuTree(eages,root)
    def GetRoads(path,i):
        if(zu[i]==0):
            return ""
        left=2*i
        right=2*i+1
        if(zu[left]!=0) and (zu[right]!=0):
            path+=str(zu[i])+"-"
            return GetRoads(path,left)+" "+GetRoads(path,right)
        else:
            return path+str(zu[i])
    answer=GetRoads("",1)
    mades=answer.split()
    roads=[]
    for c in mades:
        temp=eval("["+c.replace("-",",")+"]")
        for i in range(1,len(temp)+1):
            for j in range(0,len(temp)):
                if(j+i<=len(temp) and roads.count(temp[j:j+i])==0):
                    roads.append(temp[j:j+i])
    res=0
    for x in roads:
        do=0
        for m in x:
            do=do+d[m]
        if(do==sum):
            res=max(res,len(x))
    print(res)
if __name__ == "__main__":
    Test()