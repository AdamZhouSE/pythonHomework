test = int(input())
for t in range(test):
    n = int(input())
    i = 1
    while i <= n:
        print((bin(i)+"").replace('0b',""),end=" ")
        i += 1
    print()




























