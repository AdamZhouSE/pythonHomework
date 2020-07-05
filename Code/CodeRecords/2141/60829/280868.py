n=int(input())
for p in range(n):
    a=int(input())
    for i in range(1,a+1):
        print(bin(i).replace("0b","")+" ",end='')
    print()