size = int(input())
a = 0
while a < size:
    b = input()
    if b[-1] == '5' or b[-1] == '0':
        print("YES")
    else:
        print("NO")
    a = a + 1