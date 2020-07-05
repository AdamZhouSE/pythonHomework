initial = input()
if int(initial)<0:
    initial=int(initial[:0:-1])
    print('-',end='')
    print(initial)
else:
    print(int(initial[::-1]))
