from collections import Counter

def solve(a):
    dic = dict(Counter(a))
    values = []
    res = sorted(dic.items(),key=lambda x: x[1],reverse = True)
    votes = res[0][1]
    di = {}
    for i in range(len(res)):
        if(res[i][1] != votes):
            break
        di.update({res[i][0]:res[i][1]})
    di = sorted(di.items())
    print(di[0][0], di[0][1])
T = int(input())
x = 0
while(x<T):
    x+=1
    n = int(input())
    a = [str(i) for i in input().split(' ')]
    solve(a)