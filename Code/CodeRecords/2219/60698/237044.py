def test():
    a=int(input())
    for i in range(0,a):
        for j in range(0,a):
            if(a==i*i+j*j):
                print(True)
                return
    print(False)

test()
    