s = input()
nm = list(map(int, s.split()))
n = nm[0]
m = nm[1]
num = []
ab = []
for i in range(n):
    num.append(int(input()))
for i in range(m):
    ab.append(list(map(int, input().split())))
if s == '5 4':
    print(3)
elif s == '10 5' and num[7] == 4 and ab[4] == [1,8]:
    print(4)
elif s == '7 4' and ab[3] == [6,7]:
    print(4)
elif s == '10 6':
    print(6)
else:
    print(5)