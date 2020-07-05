n = int(input())
stick = input().split(' ')
stick = [int(x) for x in stick]
stick.sort()
x = sum(stick[0:n // 2])
y = sum(stick) - x
print(pow(x, 2) + pow(y, 2))