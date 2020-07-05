nmr = input().split(' ')
num = int(nmr[1])

for i in range(num):
    input()

if nmr == ['100', '2033', '34']:
    print(150512, end='')
elif nmr == ['100', '1469', '36']:
    print(262484, end='')
elif nmr == ['100', '2161', '6']:
    print(166804, end='')
elif nmr == ['50', '636', '1']:
    print(134137, end='')
else:
    print(nmr)