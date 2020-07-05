case=int(input())

for i in range(case):
    num=int(input())
    for j in range(num,-1,-1):
        if(j&num==j):
            print(j,end=' ')
    print()