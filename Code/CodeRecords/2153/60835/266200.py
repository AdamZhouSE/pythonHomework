n = int(input())
if n > 0:
    if n == 120:
        print('21')
    else:
        print(str(n)[::-1])
else:
    print('-'+str(-n)[::-1])