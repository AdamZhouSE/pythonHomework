times = int(input())
for i in range(times):
    num = input()
    temp = int(num.replace('6','9'))
    print(temp - int(num))