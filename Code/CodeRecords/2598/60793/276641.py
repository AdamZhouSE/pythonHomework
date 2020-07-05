ls = []
temp = list(map(int, input().split()))
m, d, t = temp[0], temp[-1], 0
for x in range(0, m):
    operands = list(map(int, input().split()))
    if operands[0] == 'A':
        ls.append((operands[1] + t) % d)
    else:
        ls_slice = ls[- operands[1]:]
        print(max(ls_slice))
        t = max(ls_slice)  