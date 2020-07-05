n_k=input().split()
n,k = int(n_k[0]),int(n_k[1])
bucket_water=list(map(int,input().split()))
min_time,time = 100,0
for i in range(n):
    if k % bucket_water[i] == 0:
        time = k//bucket_water[i]
        if min_time > time:min_time=time
print(min_time)