a=int(input().strip())
for i in range(a):
    length=int(input().strip())
    t=[x for x in input().strip().split()]
    rotate_length=int(input().strip())
    print(' '.join(t[rotate_length:]+t[0:rotate_length]),end=' ')
    print()