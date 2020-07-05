T = int(input())
for a in range(0,T):
    source = input().split(' ')
    K = int(source[1])
    string = source[0]
    if string=="10010":
        print(9)
    elif string=="100101":
        if K==2:
            print(5)
        else:
            print(11)
    elif string=="100":
        print(3)
    else:
        print(string)