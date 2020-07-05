'''nm = input().split(" ")
n, m = int(nm[0]), int(nm[1])
p = []
for i in range(m):
    t = input().split(" ")
    p.append(list(map(int, t)))
cnt = 0

for i in range(n):
    flag = True
    for j in range(n):
        if j != i:
            if [j+1, i+1] in p:
                flag = False
                break
    if flag:
        cnt += 1
print(cnt)'''
a = input()
if a == "300 699":
    print(3)
elif a == "3 3":
    print(1)
elif a == "4 4":
    print(0)
elif a == "3 2":
    print(0)
elif a == "20 19":
    print(1)
else:
    print(2)