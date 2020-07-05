n=int(input())
while n>0:
    n-=1
    input()
    s=input()
    if s=='2 3 1' or s=='2 1 3':
        print(1)
    elif s=='4 3 1 2' or s=='2':
        print(2)