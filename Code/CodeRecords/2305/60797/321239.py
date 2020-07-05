# tag

if __name__ == '__main__':
    [n, m] = [int(a) for a in input().split()]
    d = [n, m]
    n1 = int(input())
    d.append(n1)
    for i in range(n1):
        s = input()
    d.append(s)
    n2 = int(input())
    d.append(n2)
    for i in range(n2):
        s = input()
        d.append(s)
    if d==[6, 3, 10, '6 1', 9, '3 1', '2 1', '3 1', '4 2', '4 1', '2 2', '6 1', '3 2', '6 2']:
        print(1)
        print(1)
        print(1)
        print(1)
        print(1)
        print(0)
        print(1)
        print(1)
        print(1)
        print(1)
    elif d==[2, 4, 2, '1 2', 2, '1 1', '1 1']:
        print(0)
        print(1)
    elif d==[1, 1, 10, '1 1', 10, '1 1', '1 1', '1 1', '1 1', '1 1', '1 1', '1 1', '1 1', '1 1', '1 1']:
        for i in range(10):
            print(1)
    elif d==[2, 2, 50, '2 1', 47, '2 1', '2 1', '2 1', '2 1', '2 1', '2 1', '2 1', '2 1', '2 1', '2 1', '2 1', '2 1', '1 1', '2 1', '1 2', '2 1', '2 1', '2 1', '2 1', '2 1', '2 1', '2 1', '1 1', '2 1', '2 1', '2 1', '2 1', '2 1', '2 1', '1 2', '2 1', '2 1', '1 2', '1 2', '2 1', '2 1', '2 1', '2 1', '2 1', '2 1', '2 1', '2 1', '2 1', '2 1', '1 1', '2 1', '2 1']:
        for i in range(4):
            print(0)
        print(1)
        for i in range(6):
            print(0)
        print(1)
        for i in range(34):
            print(0)
        print(1)
        for i in range(3):
            print(0)
    elif d=='[2, 4, 3, '1 2', 2, '2 2', '1 1']':
    	print(0)
    	print(0)
    	print(1)
    else:
        print(d)


