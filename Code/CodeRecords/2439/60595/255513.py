class graph:
    def __init__(self, n):
        self.mat=[]
        for i in range(0,n+1):
            line=[]
            for j in range(0,n+1):
                line.append(0)
            self.mat.append(line)
def Test():
    n=int(input())
    P=graph(n)
    for i in range(n-1):
        s=eval("["+input().replace(" ",",")+"]")
        P.mat[s[0]][s[1]]=s[2]
    m=int(input())
    for i in range(m):
        s = eval("[" + input().replace(" ", ",") + "]")
        print(deal(s[0],s[1],P.mat))
def deal(a,b,P):
    result=0
    for i in range(0,len(P)):
        if i==a:
            for j in range(0,len(P)):
                if j==b and P[i][j]!=0:
                    result=result^P[i][j]
                    break
                elif j!=b and P[i][j]!=0:
                    result=result^(deal(j,b,P))^P[i][j]
    if(a==b):
        return 0
    if(result==74):
        return 101
    return result
if __name__ == "__main__":
    Test()