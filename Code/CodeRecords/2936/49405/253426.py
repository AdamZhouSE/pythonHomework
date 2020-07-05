MAP = [[['A', 'B', 'C'], 2], [['D', 'E', 'F'], 3], [['G', 'H', 'I'], 4], [['J', 'K', 'L'], 5], [['M', 'N', 'O'], 6], [['P', 'R', 'S'], 7], [['T', 'U', 'V'], 8], [['W', 'X', 'Y'], 9]]

def prcs(s):
    s = s.replace('-', '')
    for rule in MAP:
        for letter in rule[0]:
            s = s.replace(letter, str(rule[1]))
    return s

dict = {}

n = int(input())
for i in range(n):
    s = prcs(input())
    if s in dict: dict[s] += 1
    else: dict[s] = 1

ans = True
for key in dict.keys():
    if dict[key] > 1:
        print('%s-%s %d' % (key[:3], key[3:], dict[key]))
        ans = False
if ans: print('No duplicates.', end='')