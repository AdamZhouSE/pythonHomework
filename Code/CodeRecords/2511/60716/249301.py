def check(i,j):
    pre = 0
    aft = 0
    for a in range((j-i)//2):
        pre += lists[i+a]
    for b in range((j-i)//2):
        aft += lists[j-b]
    if pre<=s and aft<=s:
        return True
    else:
        return False

n,s = map(int,input().split())
lists = list()
for i in range(n):
    a = int(input())
    lists.append(a)
answer = list()
for i in range(n):
    lenlists = list()
    lenlists.append(0)
    for j in range(i,n,2):
        if (j-i+1)%2==0:
            check = check(i,j)
            if check:
                lenlists.append(j-i+1)
    lenlists.sort()
    lenlists.reverse()
    answer.append(lenlists[0])
for i in range(n):
    print(answer[i])