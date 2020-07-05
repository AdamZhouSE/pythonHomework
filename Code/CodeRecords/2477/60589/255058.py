t=int(input())
for i in range(t):
    a=input().split(' ')
    a=list(map(int,a))
    al=a[0]
    ar=a[2]
    au=a[1]
    ad=a[3]
    b = input().split(' ')
    b = list(map(int, b))
    bl = b[0]
    br = b[2]
    bu = b[1]
    bd = b[3]
    if al>br or ar<bl or au<bd or ad>bu:
        print(0)
    else:
        print(1)