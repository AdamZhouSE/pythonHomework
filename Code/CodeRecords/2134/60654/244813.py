bucket = int(input())
minuteToDie = int(input())
minuteToTest = int(input())
num = 1
while (minuteToTest//minuteToDie+1)**num< bucket:
    num += 1
print(num)
