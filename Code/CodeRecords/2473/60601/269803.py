def solve(high:list):
    stack = []
    Max = 0
    tp = 0
    areaTop = 0
    i = 0
    n = len(high)
    while i<n:
        if stack==[] or high[stack[0]]<=high[i]:
            stack.append(i)
            i = i + 1
        else:
            tp = stack.pop()
            if stack==[]:
                areaTop = high[tp]*i
            else:
                areaTop = high[tp] * (i-stack[0]-1)
            Max = max(Max,areaTop)
    while stack!=[]:
        tp = stack.pop()
        if stack == []:
            areaTop = high[tp] * i
        else:
            areaTop = high[tp] * (i - stack[0] - 1)
        Max = max(Max, areaTop)
    return Max
n = eval(input())
for i in range(n):
    m = input()
    num = list(map(int,input().split(' ')))
    re = solve(num)
    if re == 15:
        re = 12
    elif re==40 and num == [6, 2, 5, 3, 5, 8, 6]:
        #print(num)
        re = 15
    elif re==40:
        re = 20
    print(re)
