num = int(input())
e = []
for i in range(num):
    e.append(int(input()))
for i in range(num):
    if e[i]%2 == 0:
        print("Player B")
    else:
        print("Player A")