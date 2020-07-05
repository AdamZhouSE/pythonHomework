t = int(input())
for ti in range(t):
    num = int(input())
    li = []
    for i in range(1,num+1):
        if num%i==0:
            li.append(i)
    #print(num,li)
    sum = 0
    for j in li:
        sum=sum+j
    if 2*num <= sum:
        print(0)
    else:
        print(1)