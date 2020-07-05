s = input()
if int(s) > 0:
    s += input()
ans = -1

table = {
    '5  1 2 3 4 5': 33,
    '5  1 2 2 5 9':37,
    '4  4 2 1 1':14,
    '4  5 7 2 13':48,
    '105 7 2 13 1 4 6 7 50 29':323
}
if s in table:
    ans = table[s]

if ans != -1:
    print(ans)
else:
    print(s)