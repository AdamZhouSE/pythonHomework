for i in range(0,5):
    row=list(map(int,input().split(' ')))
    if 1 in row:
        j=row.index(1)
        print(abs(i-2)+abs(j-2))
        break