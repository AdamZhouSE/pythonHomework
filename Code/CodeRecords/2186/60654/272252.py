def arr(b):
    if b==2:
        return 1+2
    elif b>2:
        return arr(b-1)+b*(b+1)/2
a = int(input())
for i in range(a):
    sum = 0 
    b = int(input())
    print(int(arr(b)))