T=int(input())
for t in range(T):
    N=int(input())
    zeros=N
    arr=[]
    while N>9:
        N-=9
        arr.append('9')
    arr.append(str(N))
    arr.sort()
    for i in range(zeros):
        arr.append('0')
    print(''.join(arr))