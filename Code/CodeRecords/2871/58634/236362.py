n = int(input())
nums = [int(i) for i in input().split(" ")]
count1 = 0
count2 = 0
for i in nums:
    if i == 1:
        count1 += 1
    if i == 2:
        count2 += 1
if count2>=count1:
    print(count1)
if count1 > count2:
    print(count2+(count1-count2)//3)