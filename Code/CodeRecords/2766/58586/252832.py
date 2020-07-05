nums=int(input())
for i in range(nums):
    num=int(input())
    if num%5==0:
        print(-1)
    else:
        print(num-num//5*5)