inp = input()
strs = []
String = ''
for i in range(0, len(inp)):
    if inp[i] == 'B':
        String = String[0: len(String)-1]
    elif inp[i] == 'P':
        strs.append(String)
    else:
        String += inp[i]
n = int(input())
ans = []
for i in range(0, n):
    first, second = [int(x) for x in input().split()]
    count = 0
    ind = -1
    while True:
        try:
            ind = strs[second-1].index(strs[first-1], ind+1)
            count += 1
        except Exception:
            break
    ans.append(count)
for i in ans:
    print(i)
