def arr(b):
    if b==2:
        return 3
    elif b>2:
        return arr(b-1)+b*(b+1)/2
a = int(input())
for i in range(a):
    b = int(input())
    print(arr(b))