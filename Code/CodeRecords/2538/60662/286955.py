num = list(map(int, input().strip('[]').split(',')))
num.sort()
if num[0] > 1 or num[len(num) - 1] < 1:
    print(1)
elif num[len(num) - 1] - num[0] == len(num)-1:
    print(num[len(num) - 1] + 1)
elif num[len(num) - 1] > 1:
    for i in range(0, len(num) - 1):
        if num[i + 1] - num[i] > 1 and num[i] >= 0:
            print(num[i] + 1)
            break