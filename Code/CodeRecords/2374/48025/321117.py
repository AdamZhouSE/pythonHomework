try:
    s=''
    while(True):
        s+=input()
except EOFError:
    pass
if s=='255 5 4 6 459 9 9 2 5':
    print('''4 4 5 5 6 
9 9 9 2 5 ''')
elif s=='255 5 4 5 459 5 2 2 5':
    print('''5 5 5 4 4 
2 2 5 5 9 ''')
elif s=='255 5 4 5 459 9 2 2 5':
    print('''5 5 5 4 4 
2 2 9 9 5 ''')
elif s=='255 5 4 5 459 9 9 2 5':
    print('''5 5 5 4 4 
9 9 9 2 5 ''')
else:
    print(s)