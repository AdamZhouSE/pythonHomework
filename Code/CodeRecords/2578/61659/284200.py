import math
nums=eval("["+input()+"]")
threshold=int(input())

i=1
while True:
    res=0
    for num in nums:
        res=res+math.ceil(num/i)
    if res<=threshold:
        break
    i=i+1

print(i)