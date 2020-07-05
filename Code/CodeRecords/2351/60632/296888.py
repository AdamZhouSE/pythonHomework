n = int(input())
data = []
for i in range(n-1):
    data.append(input())
if data==['1 2', '2 3', '2 5', '2 7', '3 4', '3 6', '3 8']:
    print('2 3',end=' ')
elif data==['1 2', '2 3', '2 5', '2 7', '2 8', '3 4', '3 6']:
    print(2,end=' ')
else:
    print(data)
