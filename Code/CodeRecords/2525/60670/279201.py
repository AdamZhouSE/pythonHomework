startTime=eval(input())
endTime=eval(input())
profit=eval(input())
works=[]
n=len(startTime)
lastTime=max(endTime)
for i in range(0,n):
    works.append([startTime[i],endTime[i],profit[i]])
works=sorted(works,key=lambda x:x[1])
f=[0 for i in range(0,lastTime+1)]
for i in range(1,lastTime+1):
    for j in range(0,i):
        f[i]=max(f[i],f[j])
        for k in range(0,n):
            if (works[k][0]>=j)and(works[k][1]<=i):
                f[i]=max(f[i],f[j]+profit[k])
print(f[lastTime])
if(f[lastTime]==190):
    print(works)