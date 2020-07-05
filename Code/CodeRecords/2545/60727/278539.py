def so(l,s):
    if 0 in s:
        return 'Yes'
    for i in range(0,l):
        for j in range(i,l):
            if sum(s[i:j+1])==0:
                return 'Yes'
    return 'No'
for i in range(0,eval(input())):
    l = eval(input())
    s = input().split(' ')
    s = list(map(int,s))
    print(so(l,s))