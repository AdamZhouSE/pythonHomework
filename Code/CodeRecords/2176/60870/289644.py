str_ope = input()
start = {}
for i in range(len(str_ope)):
    start[len(str_ope) - i] = str_ope[len(str_ope) - i - 1:]
for i in range(1, len(start) + 1):
    temp_ch = start[i]
    while len(temp_ch) < len(str_ope):
        temp_ch = temp_ch + 'a'
    start[i] = temp_ch
res = sorted(start.items(), key = lambda x:x[1])
for i in range(len(res)):
    print(res[i][0], end = ' ')