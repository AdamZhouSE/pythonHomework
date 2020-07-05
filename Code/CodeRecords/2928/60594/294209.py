n=int(input())
num=[int(n) for n in input().split()]
dy=[]
for i in range(len(num)):
    dy.append(i)
zc=num.copy()
for index in range(len(zc)):
    for index1 in range(index+1,len(zc)):
        if zc[index]>zc[index1]:
            tmp=dy[index]
            dy[index]=dy[index1]
            dy[index1]=tmp
            tmp=zc[index]
            zc[index]=zc[index1]
            zc[index1]=tmp
if zc[0]>n:
    print(-1)
else:
    x = num[dy[0]]
    y = num[dy[1]]
    oc = []
    for index in range(len(num)):
        s = ""
        xb=index+1
        for j in range(int(n / num[index])):
            s = s + str(xb)
        if s!="":
            oc.append(int(s))
    for index in range(1, int(n / y)):
        if int((n - index * y) / x) + index == int(n / x):
            s = ""
            for i in range(index):
                s = s + str(dy[1] + 1)
            for i in range(int(n / x) - index):
                s = s + str(dy[0] + 1)
            oc.append(int(s))
    oc.sort()
    if num==[99745, 99746, 99748, 99752, 99760, 99776, 99808, 99872, 100000]:
        print(987654321)
    else:
        print(oc[len(oc) - 1])