s = []
num = int(input())
for i in range(num):
    temp = input()
    s.append(temp)

for i in range(num):
    if sorted(set(s[i])) != sorted(s[i]):
        print(0)
    else:
        print(1)