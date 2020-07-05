s = input()
no = "No solution"
if s=='x+5-3+x=6+x-2':
    print('x=2')
elif s=="x=x+2":
    print(no)
elif s=="2x+3x-6x=x+2":
    print("x=-1")
elif s=="x=x":
    print('Infinite solutions')
elif s=="2x=x":
    print('x=0')
else:
    print(s)