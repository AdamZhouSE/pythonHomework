t = int(input())
for i in range(0,t):
    instr = list(map(int,input().split(' ')))
    numLst = list(map(int,input().split(' ')))
    k = instr[1]
    cur = 0
    for num in numLst:
        if(numLst.count(num) == 1):
            cur = cur + 1
        if(cur == k):
            print(num)
            break
    else:
        print(-1)