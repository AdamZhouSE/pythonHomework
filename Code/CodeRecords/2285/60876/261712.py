N=int(input())
for i in range(0,N):
    days=int(input())
    money=list(map(int,input().split(" ")))
    start=0
    jud=False
    gap=False
    for j in range(0,days-1):
        if money[j]>money[j+1]:
            if not jud:
                start+=1
            elif not gap:
                print("({0} {1})".format(start,j),end="")
                gap=True
                start=j+1
            else:
                print(" ({0} {1})".format(start,j),end="")
                start=j+1
        elif j==days-2:
            print(" ({0} {1})".format(start,days-1),end="")
        else:
            jud=True
            continue
    print()