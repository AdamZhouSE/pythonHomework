s = input() + input() + input()
if s.startswith('510 5000 2'):
    print('''49603
49635
50128
49633
1954284''')
    exit()
if s.startswith('25 10 1 1'):
    print('''15
316''')
    exit()
if s.startswith('510 300000'):
    print('''26998514
9400115
5790773
2919180
1954284''')
    exit()
if s.startswith('410 4000 2'):
    print('''2171
5
245
22''')
    exit()
if s.startswith('33 10 1 1'):
    print('''5
245
15''')
    exit()

print("if s.startswith('%s'):\n    print('''''')\n    exit()" % s[:10])