n = int(input())
s = input().split(' ')
l = []
for i in range(len(s)):
    l.append(int(s[i]))

num5 = l.count(5)
num0 = l.count(0)

if (num5 < 9 or n < 10) and num0 == 0:
    print(-1)
elif (num5 < 9 or n < 10) and num0 != 0:
    print(0)
else:
    for i in range(num5//9):
        print("555555555", end='')
    for i in range(num0):
        print('0', end='')
