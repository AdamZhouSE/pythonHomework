n=int(input())
num=[]
for i in range(n):
    num.append(int(input()))
oc=num[0]
for i in range(1,n):
    min=10000
    for index in range(0,i):
        if abs(num[index]-num[i])<min:
            min=abs(num[index]-num[i])
    oc+=min
print(oc)