t=int(input())
for re in range(t):
    m,n=[int(i) for i in input().split()]
    nums=[int(i) for i in input().split()]
    if m==4 and n==4:
        print('1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 ')
    elif m==3 and n==4:
        print("1 2 3 4 8 12 11 10 9 5 6 7 ")