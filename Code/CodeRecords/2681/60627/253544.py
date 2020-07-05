# 18
def f(k):
    if k == 1:
        return 1
    if k%2 == 0:
        return min(f(int(k/2))+1,f(k-1)+1)
    else:
        return  f(k-1)+1
n = int(input())
for i in range(n):
    print(f(int(input())))