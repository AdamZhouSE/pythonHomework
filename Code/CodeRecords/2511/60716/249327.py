def check(i,j):
    pre = 0
    aft = 0
    for a in range(i,(j+i+1)//2):
        pre += lists[a]
    for b in range((j+i+1)//2,j+1):
        aft += lists[b]
    if pre<=s and aft<=s:
        return True
    else:
        return False

n,s = map(int,input().split())
lists = list()
for i in range(n):
    a = int(input())
    lists.append(a)
print("{} {}".format(n,s))
print(lists)
answer = list()
for i in range(n):
    lenlists = list()
    lenlists.append(0)
    for j in range(i,n):
        if (j-i+1)%2==0:
            checks = check(i,j)
            if checks:
#                print("append:{}".format(j-i+1))
                lenlists.append(j-i+1)
    lenlists.sort()
    lenlists.reverse()
    answer.append(lenlists[0])
for i in range(n):
    print(answer[i])