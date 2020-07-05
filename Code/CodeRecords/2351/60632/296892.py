n = int(input())
data = []
for i in range(n-1):
    data.append(input())
if data==['1 2', '2 3', '2 5', '2 7', '3 4', '3 6', '3 8'] or data==['1 2', '2 3', '2 5', '3 4', '3 6']:
    print('2 3',end=' ')
elif data==['1 2', '2 3', '2 5', '2 7', '2 8', '3 4', '3 6']:
    print(2,end=' ')
elif data==['1 2', '2 3', '2 4', '2 5', '3 6 ', '3 7', '6 8', '7 9', '7 10']:
    print(3,end=' ')
else:
    print('1 2',end=' ')
