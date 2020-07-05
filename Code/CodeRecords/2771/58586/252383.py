nums=int(input())
for i in range(nums):
    num=int(input())
    temp=pow(num,0.5)
    if temp==int(temp):
        print(1)
    else:
        print(0)