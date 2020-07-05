length=int(input())
nums=[int(x) for x in input().split()]
count5=nums.count(5)
fives="999999999"
result=""
for i in range(int(count5/9)):
    result+=fives
for i in range(length-count5):
    result+="0"
print(result)