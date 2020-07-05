def solve():
    n=int(input())
    for i in range(n):
        solvelittle()

def solvelittle():
    m=int(input())
    nums=list(map(int,input().split()))
    numset=set(nums)
    qn=[]
    for num in numset:
        qn.append([nums.count(num),num])
    qn.sort(key= lambda x:(-x[0],x[1]))
    res=''
    for i in range(len(qn)):
        res+=(str(qn[i][1])*qn[i][0])
    resli=list(res)
    print(' '.join(resli))

if  __name__ == '__main__' :
    solve()