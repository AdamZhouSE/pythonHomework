length=int(input())
nums=[int(x) for x in input().split()]
count5=nums.count(5)
fives="555555555"
result=""
if length-count5>0:
    for i in range(int(count5/9)):
        result+=fives
    if result!="":
        for i in range(length-count5):
            result+="0"
    else:result="0"
    print(result)
else:print(-1)