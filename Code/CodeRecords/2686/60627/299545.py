n = int(input())
for  i in range(n):
    k = int(input())
    input()
    num=input().split()
    for i in range(len(num)):
        num[i] = int(num[i])
    l = []
    j = 0
    t = 0
    while(j<len(num)-1):
        if (num[j]<num[j+1]):
            t += num[j]
        else:
            t += num[j]
            l.append(t)
            t=0
            print(t)