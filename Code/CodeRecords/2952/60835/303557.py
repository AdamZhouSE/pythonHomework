s = input()
out = []
stream = ""
for i in range(len(s)):
    if s[i] == 'P':
        out.append(stream)
    elif s[i] == 'B':
        stream = stream[:-1]
    else:
        stream = stream + s[i]
m = int(input())
#print(s, out)
for i in range(m):
    x, y = map(int, input().split())
    cnt = 0
    for i in range(len(out[y - 1]) - len(out[x - 1]) + 1):
        if out[x - 1] == out[y - 1][i:i + len(out[x - 1])]:
            cnt = cnt + 1
    print(cnt)
    