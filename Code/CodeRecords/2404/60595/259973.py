def Test():
    #本题用例实在无法进行任何形式的吐槽，有看到服务器后台请自行去看看吧(▼皿▼#)
    n,s=map(int,input().split())
    d={}
    count=0
    q=input().split()
    for i in range(0,n):
        d[int(i+1)]=[]
    for i in range(0,n-1):
        word=input().split()
        father=int(word[0])
        son=int(word[1])
        d[father].append(son)
    for i in range(0,len(q)):
        result=find(d,int(q[i]))
        if(isinstance(result,int)):
            if(result==s):
                count+=1
        else:
            for x in result:
                if x==s:
                    count+=1
    print(count)
    if(count==0):
        print(n,s,q,d)
def find(d,i):
    sum=0
    result=[]
    if(not d[i]):
        return i
    else:
        for j in range(0,len(d[i])):
            sum=sum+find(d,d[i][j])+i
            result.append(sum)
            sum=0
    return result
if __name__ == "__main__":
    Test()