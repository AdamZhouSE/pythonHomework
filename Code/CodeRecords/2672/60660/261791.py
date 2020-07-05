comp=0
for i in range(32):
    comp+=1<<i
t=int(input())
for i in range(t):
    n=int(input())
    print(n^comp)