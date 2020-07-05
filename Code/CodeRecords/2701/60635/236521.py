src=input()
src=src[2:len(src)-2].split('],[')
moves=[[int(i[0]),int(i[2])]for i in src]
sign=0
a=0
b=0
ac=[7, 56, 448, 73, 146, 292, 273, 84]
for move in moves:
    if sign==0:
        a ^= 1<<(3*move[0]+move[1])
        sign=1
    else:
        b ^= 1 << (3 * move[0] + move[1])
        sign=0

for i in ac:
    if a & i==i:
        print('A')
        break
    elif b & i==i:
        print('B')
        break
else:
    print('Draw'if len(moves)==9 else 'Pending')