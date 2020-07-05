def call():
    N=int(input())
    names={}
    for i in range(N):
        name=input()
        names[name]=0
    n=int(input())
    ans=[]
    for i in range(0,n):
        name=input()
        if name not in names.keys():
            ans.append("WRONG")
            continue
        else:
            names[name]+=1
        if names[name]==1:
            ans.append("OK")
        else:
            ans.append("REPEAT")
    for judge in ans:
        print(judge)

if __name__=='__main__':
    call()