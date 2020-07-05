T=int(input())
for i in range(0,T):
    arr=[int(n) for n in input().split(' ')]
    num,intval=arr[0],arr[1]
    pa=[]
    time=0
    for j in range(0,num):
        pa.append(time)
        time=time+intval
    alltime=10*(num-1)
    wait=alltime-pa[num-1]
    print(wait)
