def over(num):
    result = 0
    while num > 0:
        result *= 10
        result += num%10
        num = int(num/10)
    return result

def judge(num):
    if num < 0:
        return False
    overNum = over(num)
    while overNum != 0 and num != 0:
        if overNum == 0 and num != 0 or overNum != 0 and num == 0:
            return False
        if overNum%10 != num%10:
            return False
        overNum = int(overNum/10)
        num = int(num/10)
    return True

num = int(input())
print(judge(num))
