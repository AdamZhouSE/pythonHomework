n=int(input())
for l in range(n):
    a=int(input())
    b=[int(x) for x in input().split(" ")]
    count=0
    for i in b:
        if not i==0:
            count += 1
            print(str(i)+" ",end='')
    for i in range(0,len(b)-count):
        print("0 ",end='')
    print()