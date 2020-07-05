def arr(b):
    if b==1:
        return 1
    elif b>1:
        return arr(b-1)+(b*(b+1))/2
a = int(input())
for i in range(a):
    b = int(input())
    print(int(arr(b)))