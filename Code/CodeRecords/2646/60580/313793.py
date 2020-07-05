size = int(input())
a = 0
while a < size:
    b = int(input())
    if b % 2 == 0:
        print("Player B")
    else:
        print("Player A")
    a = a + 1