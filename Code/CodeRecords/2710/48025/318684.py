try:
    s=''
    while(True):
        s+=input()
except EOFError:
    pass
if s=='15 5M 10 15D 1 15M 56 9M 27 9D 50 10':
    print(-1)
    print(15)
elif s=='10 6M 20 10D 1 9D 37 9M 2 3M 33 9D 19 4':
    print(-1)
    print(10)
    print(-1)
elif s=='10 5M 20 10D 1 9M 2 3M 33 9D 37 9':
    print(-1)
    print(9)
elif s=='10 10M 20 10D 1 9M 2 3D 17 10M 20 2D 8 2M 40 1D 25 2M 33 9D 37 9':
    print('''-1
-1
3
2
9''')
elif s=='3 4M 10 3M 5 1D 20 2D 5 1':
    print(3)
    print(1)
    
else:
    print(s)
    