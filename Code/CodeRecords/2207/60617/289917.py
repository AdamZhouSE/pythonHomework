def divAwithB():
    row=input().split(" ")
    A=int(row[0])
    B=int(row[1])
    if A==B==1:
        print(1)
        return
    if B>=A:
        print(0)
        return
    dfs(A,B,0)
    print(0)

def dfs(A,B,start):
    if A==B==0:
        print(1)
        exit()
    elif A==0 and B!=0:
        return
    elif B==0 and A!=0:
        return
    elif A<0:
        return
    for i in range(start+1,A+1):
        dfs(A-i,B-1,i)

if __name__=='__main__':
    T=int(input())
    for i in range(0,T):
        divAwithB()