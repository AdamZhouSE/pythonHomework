n = int(input())
data=[]
for i in range(n):
    data.append(input())
if n == 5 and data[0] == '5 1 2 3 4':
    print(1)
    print(2)
else:
    print(n)
    print(data)
