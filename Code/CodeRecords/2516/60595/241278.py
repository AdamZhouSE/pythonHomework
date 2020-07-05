def Test():
    num=int(input())
    block=[]
    result=[]
    for i in range(0,num):
        block.append(eval("["+input()+"]"))
    for i in range(0,len(block)):
        g=findRight(i,block)
        temp=int(str(g)[1]) if(g!=-1) else -1
        result.append(temp if(temp!=-1) else -1)
    print(result)

def findRight(i,block):
    d={}
    for j in range(0,len(block)):
        if(i!=j):
            if(block[j][0]>=block[i][-1]):
                d[j]=block[j]
    if(not (d)):
        return -1
    else:
        d=sorted(d.items(),key=lambda kv:(kv[1][0]))
        return d[0]

if __name__ == "__main__":
    Test()