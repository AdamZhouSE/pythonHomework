ls = []
temp = list(map(int, input().split()))
m, d, t = temp[0], temp[-1], 0
for x in range(0, m):
    operands = list(input().split())
    if operands[0] == 'A':
        ls.append((int(operands[1]) + t) % d)
    else:
        ls_slice = ls[-int(operands[1]):]
        print(max(ls_slice))
        t = max(ls_slice)