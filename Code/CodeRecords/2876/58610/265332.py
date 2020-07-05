n = eval(input())
rooms = list(map(int, input().split(' ')))
count = 0
for i in range(1, n - 1):
    if rooms[i - 1] == 1 and rooms[i] == 0 and rooms[i + 1] == 1:
        rooms[i + 1] = 0
        count += 1
print(count)
if count == 9:
    print(rooms)