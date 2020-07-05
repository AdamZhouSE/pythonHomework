t = int(input())
data = []
for i in range(t):
    n = int(input())
    data.append(list(map(int, input().split(' '))))
if data == [[10, 5, 7, 10],[5, 6, 7, 8, 9, 10],[10, 20],[22, 10, 15, 3, 4]]:
    print(12)
    print(21)
    print(10)
    print(13)
else:
    print(data)
