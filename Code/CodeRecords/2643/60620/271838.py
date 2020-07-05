cus=list(map(int,input().split(',')))
gru=list(map(int,input().split(',')))
x=int(input())
un=0
for i in range(len(cus)):
    un+=cus[i]*gru[i]
result=[]
for i in range(len(cus)-x+1):
    temp=0
    for j in range(x):
        temp+=cus[i+j]*gru[i+j]
    result.append(temp)
num=max(result)
print(sum(cus)-un+num)
    