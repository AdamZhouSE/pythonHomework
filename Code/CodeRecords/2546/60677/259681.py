times=int(input())
def do(n):
    if n==0 or n==1 or n==2:
        return 1
    else:
        return do(n-2)+do(n-3)
for i in range(times):
    print(do(int(input())))