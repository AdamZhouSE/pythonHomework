s = input()
get = input()[1:-1]
pairs = []
for i in range(0, len(get) - 4, 6):
    pairs.append(list(map(int, get[i:i + 5][1::2])))
while True:
    over = True
    for i in range(len(pairs)):
        x = pairs[i][0]
        y = pairs[i][1]
        if s[x] > s[y]:  # 如果不符合字典序，交换
            s = s[:x] + s[y] + s[x+1:y] + s[x] + s[y+1:]
            over = over and False
    if over:
        break
print(s)
