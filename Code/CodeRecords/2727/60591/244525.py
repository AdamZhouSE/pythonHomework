def find(hole,ani):
    hole.sort()
    ani.sort()
    res = 0
    for x in range(len(hole)):
        if(abs(hole[x]-ani[x]) > res):
            res = abs(hole[x]-ani[x])
    return res

n = eval(input())
while(n != 0):
    n = n - 1
    input()
    ani = list(map(int,input().split(" ")))
    hole = list(map(int, input().split(" ")))
    print(find(hole,ani))