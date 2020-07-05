T =int(input())
for i in range(T):
    N = int(input())
    for i in range(1,N+1):
        a = str(bin(i))
        print(a[a.find('b')+1:len(a)],end=' ')
    print()