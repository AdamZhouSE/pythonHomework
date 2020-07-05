import numpy as np
tests = input().split()
nums = int(tests[0])
comd = int(tests[1])
num = list(map(int,input().split()))
for i in range(0,comd):
    ls = input().split()
    x = int(ls[1])
    y = int(ls[2])
    if ls[0]=='1':
        k = int(ls[3])
        for j in range(x-1,y):
            num[j]+=k
    elif ls[0]=='2':
        sums = sum(num[x-1:y])
        print("{:.4f}".format(sums/(y-x+1)))
    else:
        fang = np.var(num[x-1:y])
        print("{:.4f}".format(fang))
        