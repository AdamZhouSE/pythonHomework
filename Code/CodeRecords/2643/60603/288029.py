cus=input().split(",")
ang=input().split(",")
num=int(input())
anslist=[]
for i in range(len(cus)):
    cus[i]=int(cus[i])
    ang[i]=int(ang[i])
for i in range(0,len(cus)-num+1):
    count=0
    for j in range(len(cus)):
        if((j>=i)&(j<=i+2)):
            count+=cus[j]
        else:
            if(ang[j]==0):
                count+=cus[j]
    anslist.append(count)
print(max(anslist))
