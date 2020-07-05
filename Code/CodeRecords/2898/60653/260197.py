n = int(input())
s = input()
if s == "0":
    print(0)
else:
    ans = []
    sum = 0
    ans.append(1)
    for i in range(0, n):
        if s[i] == '0':
            sum += 1
    for i in range(0, sum):
        ans.append(0)
    print("".join(str(i) for i in ans), end='')