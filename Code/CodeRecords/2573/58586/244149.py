nums=int(input())
for i in range(nums):
    num=int(input())
    if num%2==0:
        print(pow(2,pow(3,num//2-1)))
    else:
        print(pow(2,pow(2,num//2)))
