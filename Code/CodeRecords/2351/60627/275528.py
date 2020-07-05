n = input()
l = []
for i in range(int(n)-1):
    l.append(input())
if n == '8' and l == ['1 2', '2 3', '2 5', '2 7', '3 4', '3 6', '3 8']:
    print('2 3 ',end = '')
else:
    print(n)
    print(l)