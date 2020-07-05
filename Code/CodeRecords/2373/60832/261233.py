import numpy as np

All = int(input())

for q in range(0, All):
    length = int(input())
    ar = list(map(int, input().split()))
    ans = 0

    opt = np.zeros(length)
    opt[0]=ar[0]
    opt[1]=max(ar[0],ar[1])

    for i in range(2,length):
        # 选与不选
        A=opt[i-2]+ar[i]
        B=opt[i-1]

        opt[i]=max(A,B)
    ans=int(opt[length-1])
    print(ans)