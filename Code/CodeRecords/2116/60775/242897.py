r = int(input())
list = input().split(',')
lis = [ int(e) for e in list]

def judge(num):
    if num == 1:
        return True
    while num > 1:
        for i in lis:
            if num/i == num//i:
                num = num/i
                break
            elif i == lis[-1]:
                return False
    return True
rank = 0
current = 0
while rank < r:
    current += 1
    if judge(current):
        rank +=1

print(current)