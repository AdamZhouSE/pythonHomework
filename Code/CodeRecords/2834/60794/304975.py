p_num = int(input().split(" ")[0])
card = []
for i in range(p_num):
    card.append(list(input()))
aaa = input().split(" ")
value = []
for i in range(len(aaa)):
    value.append(int(aaa[i]))
ans = 0
for i in range(len(value)):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    for k in range(len(card)):
        if card[k][i] == "A":
            a = a + 1
        elif card[k][i] == "B":
            b = b + 1
        elif card[k][i] == "C":
            c = c + 1
        elif card[k][i] == "D":
            d = d + 1
        elif card[k][i] == "E":
            e = e + 1
    ans = ans + max(a, b, c, d, e) * value[i]
print(ans)