T = int(input())
for i in range(T):
    N = int(input())
    s = (''+input()).split(' ')
    s =  list(map(int,s))
    j = 1
    while j <len(s)-1:
        if max(s[0:j]) <= s[j] and min(s[j+1:len(s)]) >= s[j]:
            print(s[j])
            break
        j += 1
    if j == len(s) -1:
        print(-1)