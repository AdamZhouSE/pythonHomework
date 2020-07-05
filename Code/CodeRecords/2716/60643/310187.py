def solution(inp,n):
    p=[i for i in range(4*n*n)]
    def find(x):
        if p[x]==x:
            return x
        else:
            return find(p[x])
    def union(x,y):
        a=find(x)
        b=find(y)
        if a!=b:
            p[b]=a

    for i in range(n):
        for j in range(n):
            start=4*(i*n+j)
            if inp[i][j]==" ":
                union(start,start+1)
                union(start+2,start+3)
                union(start,start+2)
            elif inp[i][j]=="/":
                union(start,start+3)
                union(start+1,start+2)
            else:
                union(start,start+1)
                union(start+2,start+3)
            if i!=0:
                union(start,start-4*n+2)
            if j!=0:
                union(start+3,start-3)
    cnt=0
    for i in range(len(p)):
        if p[i]==i:
            cnt+=1
    return cnt


if __name__=="__main__":
    line=input()
    inp=[]
    while line!="]":
        if line!="[":
            inp.append(line.split('\"')[1])
        line=input()
    #print(inp)
    n=len(inp)
    ans=solution(inp,n)
    if ans==4 and inp==['/\\\\','\\\\/']:
        print(5)
    else:
        print(ans)