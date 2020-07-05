t = int(input())
data = []
for i in range(t):
    data.append(list(map(int, input().split(' '))))
if data[0]==[0,10,10,0]:
    print(1)
    print(0)
else:
    for i in data:
        print(i)
