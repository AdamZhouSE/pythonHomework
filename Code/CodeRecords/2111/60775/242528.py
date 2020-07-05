def judge(num):
    if num == 1:
        return True
    while num > 1:
        if num/2 == num//2:
            num = num/2
        elif num/3 == num//3:
            num = num/3
        elif num/5 == num//5:
            num = num/5
        else:
            return False
    return True

n = int(input())
current_num = 1
rank = 0
while rank<n:
    if judge(current_num):
        rank += 1
    current_num += 1
print(current_num-1)