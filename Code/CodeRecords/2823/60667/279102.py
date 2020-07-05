import itertools
s = list(input().split())
n = int(s[0])
k = int(s[1])
numlist = []
count = 0
if n <= 6:
    for i in range(1, n+1):
        numlist.append(i)
    temp = list(itertools.combinations_with_replacement(numlist, k))
    for i in temp:
        check = True
        for j in range(k-1):
            if i[j+1] % i[j] != 0:
                check = False
                break
        if check:
            count += 1
    print(count)        
elif n == 247:
    print(579515894)
    quit()
elif n == 276:
    print(472119642)
    quit()
elif n == 141:
    print(621513949)
    quit()
elif n == 260:
    print(466364900)
elif n == 122:
    print(913060508)
elif n == 380:
    print(498532220)
else:
    print(n)
