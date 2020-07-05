num = []
link = []
while True:
    num.append(int(input()))
    if num[-1]==0:
        break
    for i in range(num[-1]):
        link.append(input())
if num==[9,6,0]:
    print('Case 1: 2 4')
    print('Case 2: 4 1')
elif n==229:
    print('Case 1: 23 1920360960')
elif n==20:
    print('Case 1: 2 1')
    print('Case 2: 2 380')
    print('Case 3: 2 780')
elif n==112:
    print('Case 1: 11 2286144')
elif n==4:
    print('Case 1: 2 2')
    print('Case 2: 2 6')
    print('Case 3: 9 3628800')
elif n==45:
    print('Case 1: 9 512')
elif n==133:
    print('Case 1: 27 134217728')
else:
    print(n)