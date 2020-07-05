def Test():
    n,root = map(int,input().split())
    eages = []
    for i in range(0, n):
        eages.append(eval("[" + input().strip().replace(" ", ",") + "]"))
    m=int(input())
    finds=[]
    zu=zuTree(eages,root)
    for i in range(0,m):
        finds=(eval("[" + input().strip().replace(" ", ",") + "]"))
        x=findFather(zu,zu.index(finds[0]),zu.index(finds[1]))
        print(x)
def zuTree(eages,root):
    zu=[0 for _ in range(0,100)]
    zu[1]=root
    for x in eages:
        father=x[0]
        leftson=x[1]
        rightson=x[2]
        i=zu.index(father)
        left=2*i
        right=2*i+1
        zu[left]=leftson
        zu[right]=rightson
    return zu
def findFather(zu,i,j):
    if(i>j):
        if(i%2==0):
            i=i//2
        else:
            i=(i-1)//2
    elif(j>i):
        if(j%2==0):
            j=j//2
        else:
            j=(j-1)//2
    else:
        return i
    return findFather(zu,i,j)
if __name__ == "__main__":
    Test()