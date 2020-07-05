n,m=map(int,input().split(" "))
num=list(map(int,input().split(" ")))
length=2*min(num.count(1),num.count(-1))
for i in range(m):
    start,end=map(int,input().split(" "))
    if(end-start+1>length):
        print("0")
    elif((end-start)%2==0):
        print("0")
    else:
        print("1")
    