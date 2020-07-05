num = int(input())

def judge(num):
    num = int(num)
    return True if num == 0 or num & (num - 1) == 0 else False

print(judge(num))