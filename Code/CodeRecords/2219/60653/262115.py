n = int(input())
table = [0]*100
ans = "False"
for i in range(0, 100):
    table[i] = (i+1)*(i+1)
for i in table:
    for j in table:
        if i + j == n:
            ans = "True"
            break
    if ans == "True":
        break
print(ans)