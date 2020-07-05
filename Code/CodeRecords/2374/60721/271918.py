T=int(input())
num=[]
lis=[list()]*T
for i in range(0,T):
    num.append(int(input()))
    lis[i]=list(map(int,input().split(" ")))
pin=[[] for i in range(0,T)]
for i in range(0,T):
    lis[i].sort()
    for j in range(0,num[i]):
        pin[i].append(lis[i].count(lis[i][j]))
answer=[[] for i in range(0,T)]
for i in range(0,T):
    for j in range(0,num[i]):
        for k in range(0,max(pin[i])):
            answer[i].append(lis[i][pin[i].index(max(pin[i]))])
        b=lis[i][pin[i].index(max(pin[i]))]
        a=pin[i][pin[i].index(max(pin[i]))]
        pin[i][pin[i].index(max(pin[i]))]=0
        for k in range(pin[i].index(max(pin[i])),len(pin[i])):
            if(pin[i][k]==a and lis[i][k]==b):
                pin[i][k]=0
for i in range(0,T):
    for j in range(0,num[i]):        
        print(answer[i][j],end=" ")
    print()