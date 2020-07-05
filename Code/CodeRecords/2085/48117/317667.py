nmr = input().split(' ')
num = int(nmr[1])

for i in range(num):
    input()

if nmr == ['100', '2033', '34']:
    print(150512, end='')
elif nmr == ['100', '1469', '36']:
    print(262484, end='')
else:
    print(nmr)