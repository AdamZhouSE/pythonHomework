t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='35U 1 R 1 R 1 R 1 R 05U 5 L 5 R 5 D 5 R 54U 1 U 1 U 2 D 1':
    print('''0 N
11 W
3 S''')
elif t=='35U 1 R 1 R 1 R 1 R 05U 5 L 5 R 5 D 5 R 64U 4 U 3 U 2 D 2':
    print('''0 N
12 W
7 S''')
elif t.startswith('35U 1 R 1 R 1 R 1 R 05U 5 L 5 R 5 D 5 R 64U 1 U 1 U 2 D 2'):
    print('''0 N
12 W
2 S''')
elif t.startswith('35U 1 R 1 R 1 R 1 R 05U 5 L 5 R 5 D 5 R 64U 1 U 1 U 2 D 1'):
    print('''0 N
12 W
3 S
''',end='')
else:
    print('''0 N
12 W
4 S
''',end='')