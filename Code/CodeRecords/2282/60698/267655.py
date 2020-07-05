def test():
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        arrive=input().split()
        arrive=list(map(int,arrive))
        leave=input().split()
        leave=list(map(int,leave))
        stay=[[arrive[i],leave[i]] for i in range(0,n)]
        stay.sort(key=lambda x:x[0])
        count=cal(stay)
        print(count)

def cal(stay)->int:
    num=1
    tmp=0
    able=[0 for i in range(0,len(stay))]
    num=time_seperate(stay,num,tmp,able)
    return num

def time_seperate(stay,num,tmp,able):
    if min(able)==1:
        return num
    for i in range(0,len(stay)):
        if able[i]==1:
            continue
        if stay[i][0]>tmp:
            able[i]=1
            tmp=stay[i][1]
    if min(able)==1:
        return num
    return time_seperate(stay,num+1,0,able)

test()

