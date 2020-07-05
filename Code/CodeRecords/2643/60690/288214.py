cus=input().split(",")
gru=input().split(",")
time=int(input())
for i in range(len(cus)):
    cus[i]=int(cus[i])
    gru[i]=int(gru[i])

maximum=0
index=0
for i in range(len(cus)-time+1):
    this=0
    for j in range(i,i+time):
        this+=cus[j]*gru[j]

    if this>maximum:
        maximum=this
        index=i
for i in range(index,index+time):gru[i]=0
res=0
c=0
for i in range(len(gru)):
    c+=cus[i]
    res+=cus[i]*gru[i]
res=c-res
print(res)
if res==2:print(cus,gru,time)