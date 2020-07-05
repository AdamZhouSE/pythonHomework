t=int(input())
for dd in range(t):
    N=int(input())
    num=[int(n) for n in input().split()]
    num=sorted(num)
    print(num[N-1]*num[N-2]*num[N-3])
   