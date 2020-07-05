a=1
b=0

for i in range(9):
    print(str(a))
    for j in range(10):
        print(str(a)+str(b))
        if (a + b  == 1):
            print(100)
        b=b+1

    a=a+1
    b=0
