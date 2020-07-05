def func(n):
    if n==1: return 'A'
    tmp=func(n-1)
    return tmp+chr(0x40+n)+tmp
print(func(int(input())))