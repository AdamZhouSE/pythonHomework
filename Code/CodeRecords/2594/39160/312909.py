t = int(input())

for i in range(t):
    str1 = input()
    rev = str1[::-1]
    maxi = -1
    for l in str1:
        last = rev.index(l)
        start = str1.index(l)
        l = len(str1)-1-last - start-1
        if l >=0 and l > maxi:
            maxi = l
    if maxi>=0:
        print(maxi)
    else:
        print("-1")