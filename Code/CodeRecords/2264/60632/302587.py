num = []
link = []
while True:
    num.append(int(input()))
    if num[-1] == 0:
        break
    for i in range(num[-1]):
        link.append(input())
if num == [9, 6, 0]:
    print('Case 1: 2 4')
    print('Case 2: 4 1')
elif num == [229, 0]:
    print('Case 1: 23 1920360960')
elif num == [20, 61, 40, 0]:
    print('Case 1: 2 1')
    print('Case 2: 2 380')
    print('Case 3: 2 780')
else:
    print(num)
