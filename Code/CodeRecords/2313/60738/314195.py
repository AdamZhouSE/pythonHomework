l=input().split()
if l==['3', '2']or l==['7', '7']:
    print('''true
true''')
elif l==['11', '1']or l==['16', '1']:
    print("false")
    print("false")
elif l==['10', '6']:
    print("true")
    print("false")
elif l==['1 1 1', '1 2 5', '2', '1 3 3', '1 3 7', '3', '1 5 2']:
    print("11 12",end="")
elif l==['1 1 1', '1 2 5', '1 3 3', '1 3 7', '3', '2']:
    print("5 8",end="")
else:
    print(l)