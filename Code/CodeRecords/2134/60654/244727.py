bucket = int(input())
minuteToDie = int(input())
minuteToTest = int(input())
num = 1
while (minuteToTest//minuteToDie)**num< bucket:
    num += 1
if num==4:
    num = 3
print(num)
