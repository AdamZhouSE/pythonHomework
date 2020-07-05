# 42
n = int(input())
for i in range(n):
    input()
    inp = input()
    num = inp.split()
    for j in range(len(num)):
        num[j] = int(num[j])
    t = 0
    for j in range(len(num)):
        for k in range(j,len(num)):
            if k!=j and num[j] > num[k]:
                t+=1
    print(t)