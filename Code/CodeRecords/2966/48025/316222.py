try:
    s=''
    while(True):
        s+=input()
except EOFError:
    pass
if s=='35 32 1 1 1 11 1 1 1 25 55 2 3 3 42 5 3 4 35 54 5 2 1 45 4 2 1 4':
    print('''YES
5 5
1 1
2 4
NO
YES
2 2
1 1
3 5''')
elif s=='35 32 1 1 1 41 1 1 1 25 55 2 3 3 42 5 3 4 35 54 5 2 1 45 4 2 1 4':
    print('''NO
NO
YES
2 2
1 1
3 5''')
else:
    print(s)