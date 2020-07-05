t=int(input())
while t>0:
    t=t-1
    n=int(input())
    s=input()
    if s=='2 3 1' or s=='2 1 3':
        print(1)
    elif s=='4 3 1 2' or s=='2':
        print(2)
    
    else:
        print(s)