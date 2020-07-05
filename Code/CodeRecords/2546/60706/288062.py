t=int(input())
num=[]
num.append(1)
num.append(1)
num.append(1)
i=3
while(len(num)<100):
    num.append(num[i-2]+num[i-3])
    i=i+1
for i in range(t):
    n=int(input())
    print(num[n])

    