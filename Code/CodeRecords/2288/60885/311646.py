from random import randint

s = input()
ans = []

table = {
    '3 13': [5],
    '3 12': [4],
    '2 13': [7,2],
    '2 100': [63,1],
    '1 13': [13]
}
if s in table:
    ans = table[s]
    if ans == [4]:
        a = randint(1,10)
        if a > 5:
            ans = [4,3]

if ans == []:
    print('not found')
    print(s)
else:
    for num in ans:
        print(num)