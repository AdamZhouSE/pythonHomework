m = int(input())
data = list(map(int, input().split(' ')))
n = int(input())
areas = []
result = []
for i in range(n):
    areas.append(list(map(int, input().split(' '))))
for i in areas:
    result.append(len(list(set(data[i[0]-1:i[1]]))))
for i in result:
    print(i)
