cnt = int(input())
li = []
for i in range(cnt):
    li.append(int(input()))
for i in li:
    if i % 2 == 1:
        print("Player A")
    else:
        print("Player B")