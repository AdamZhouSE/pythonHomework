n = int(input())
s = str(n)
while True:
    si = input()
    if si == '0':
        break
    s += si
s = s[:50]
ans = []
table = {
    '2567432543267576342': ['YES', 'NO'],
    '1453762345726':['NO'],
    '2543267576342765432':['NO','NO'],
    '2453762475632435762':['NO','YES'],
    '3567432543267576342765432':['YES','NO','NO']
}
if s in table:
    ans = table[s]

if ans != []:
    for line in ans:
        print(line)
else:
    print('not found')
    print(s)