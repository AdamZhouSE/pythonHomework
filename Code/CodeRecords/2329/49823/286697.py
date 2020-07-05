def bh(A):
    def gcd(a, b):
        if b==0:
            return a
        else:
            return gcd(b,a%b)
    def isConnected(a,b):
        return gcd(a,b)>1
    def explore(k,nodes,closed):
        cnt=0
        for i in range(len(nodes)):
            if i!=k and isConnected(nodes[i],nodes[k]) and closed[i]==0:
                closed[i]=1
                cnt+=1
                cnt+=explore(i,nodes,closed)
        return cnt
    closed=[0 for _ in range(len(A))]
    rs=1
    for i in range(len(A)):
        cnt=1
        if closed[i]==0:
            closed[i]=1
            cnt+=explore(i,A,closed)
        rs=max(rs,cnt)
    print(rs)
if __name__ == '__main__':
    bh(eval(input()))
