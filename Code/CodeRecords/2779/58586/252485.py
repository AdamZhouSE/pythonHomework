nums=int(input())
for i in range(nums):
    num=int(input())
    arr=list(map(int,input().split(" ")))
    def lcm(a,b):
        mul=a*b
        while b>0:
            temp=b
            b=a%b
            a=temp
        return mul//a
    print(lcm(max(arr),min(arr)))