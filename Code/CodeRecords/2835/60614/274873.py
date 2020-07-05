length=int(input())
nums=[int(x) for x in input().split()]
count5=nums.count(5)
fives="555555555"
result=""
if count5/9>=1 and length-count5>0:
    for i in range(int(count5/9)):
        result+=fives
    for i in range(length-count5):
        result+="0"
    print(result)
else:print(-1)