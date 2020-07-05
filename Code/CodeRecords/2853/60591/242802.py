input()
nums = list(map(int,input().split(" ")))
number = [0,0] # 偶数，奇数
for num in nums:
    if(num % 2 == 0):
        number[0] += 1
    else:
        number[1] += 1
if(number[1]%2 == 1):
    print(number[1])
else:
    print(number[0])