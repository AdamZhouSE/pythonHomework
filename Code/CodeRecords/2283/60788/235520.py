from sys import stdin 
num=int(stdin.readline().strip())
for i in range(0,num):
    length=int(stdin.readline().strip())
    s=[int(x) for x in stdin.readline().split()]
    s.sort(reverse=False)
    t=iter(s)
    print(next(t),end="")
    while True:
        temp=next(t,3)
        if temp!=3:
            print(" ",end="")
            print(temp,end="")
        else:
            break
    print("")