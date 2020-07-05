num=int(input())
times=[]
res=1

for i in range(num):
    times.append(input().split())

for i in range(num-1):
    if (times[i][0]==times[i+1][0] and int(times[i+1][1])-int(times[i][1])==0) :
        res+=1
    else:
        continue
print(res)
