n = int(input())
for  i in range(n):
    k = int(input())
    input()
    num=input().split()
    for i in range(len(num)):
        num[i] = int(num[i])
    l = []
    j = 0
    a = 0
    b = 0
    while(j<len(num)-1):
        if (num[j]<num[j+1]):
            b += 1
        else:
            l.append(num[b] - num[a])
            b += 1
            a = b
        j+=1
    print(l)