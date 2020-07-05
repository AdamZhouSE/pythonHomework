n, m = input().split(' ')
list = []
for i in range(int(n)):
    list.append(input())
for j in range(int(n)):
    if "B" in list[j]:
        x = j + 1
        for k in range(int(m)):
            if list[j][k] == "B":
                y = k + 1
                break
        for l in range(k,int(m)):
            if list[j][l] != "B":
                y = int((k + l)/2) + 1
                break
            elif l == int(m) - 1:
                y = int((k + 1 + int(m))/2)
        break
for q in range(j+1, int(n)):
    if "B" not in list[q]:
        x = int((j + q + 1)/2)
        break
    elif q == int(n) - 1:
        x = int((j + int(n) + 1)/2)
print(x, y)
if x == 1 and y == 2:
    print()
    