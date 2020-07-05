s = input()
n = int(input())
op = []
for i in range(n):
    op.append(input().split())
for i in range(n):
    if op[i][0] == '1':
        s = s + op[i][1]
    elif op[i][0] == '2':
        s = op[i][1][::-1] + s
    else:
        sum1 = len(s)
        k = 2
        while k <= len(s):
            for j in range(n):
                if i + k <= n:
                    s2 = s[j:j + k]
                    if s2 == s2[::-1]:
                        sum1 += 1
            k += 1
        print(sum1)



