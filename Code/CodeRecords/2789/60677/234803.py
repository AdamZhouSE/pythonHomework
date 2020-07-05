def fun():
    n=int(input())
    boards=input().split()
    boards.sort(reverse=True)
    square=True
    for i in range(n):
        if int(boards[i])<=i:
            square=False
            print(i)
            break;
    if square:
        print(n)
        
times=int(input())
for i in range(times):
    fun()