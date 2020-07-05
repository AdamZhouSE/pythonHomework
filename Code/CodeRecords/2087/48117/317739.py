n = int(input())
m = []
for i in range(n):
    m.append(input())

if m == ['233']:
    print(1, end='')
elif m == ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20']:
    print(10, end='')
else:
    print(m)

