cus=list(input().split(","))
gru=list(input().split(","))
k=int(input())
res=[]
number=0
for i in range(len(cus)):
    cus[i]=int(cus[i])
    gru[i]=int(gru[i])
for i in range(len(cus)-k):
    number=0
    tem=[]
    for j in range(len(cus)):
        tem.append(gru[j])
    for j in range(i,i+k):
        tem[j]=0
    for j in range(len(cus)):
        if tem[j]==0:
            number=number+cus[j]
    res.append(number)
print(max(res))