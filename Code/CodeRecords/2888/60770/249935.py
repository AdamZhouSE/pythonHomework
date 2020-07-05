def read():
    nums = list(map(int, input().split()))
    return nums

def solve(a,b):
    i,j=map(int,input().split())
    if (j-i)%2==0:
        print(0)
        return

    if int((j-i+1)/2)>min(a,b):
        print(0)
        return

    print(1)
    return

if  __name__ == '__main__' :
    total=int(input().split()[1])
    nums=read()
    a=nums.count(1)
    b=nums.count(-1)
    for i in range(total):
        solve(a,b)