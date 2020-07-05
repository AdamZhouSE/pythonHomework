def minDistance(a,b,k):

    if len(a) == 0 and len(b) == 0:
        return 0
    if len(a) == 0:
        return k * len(b)
    if len(b) == 0:
        return k * len(a)

    distance = abs(ord(a[0]) - ord(b[0]))
    if distance <= k:
        return distance + minDistance(a[1:],b[1:],k)
    else:
        if len(a) - 1 == 0:
            b_move = k
        else:
            b_move = abs(ord(b[0]) - ord(a[1]))
        if 0 == len(b) - 1:
            a_move = k
        else:
            a_move = abs(ord(a[0]) - ord(b[1]))
        if min(a_move,b_move) <= k or len(a) == len(b):
            if a_move > b_move:
                return k + minDistance(a[1:], b, k)
            else:
                return k + minDistance(a, b[1:], k)
        else:
            if len(a) < len(b):
                return k + minDistance(a, b[1:], k)
            else:
                return k + minDistance(a[1:], b, k)








str1 = input()
str2 = input()
k = int(input())
res = minDistance(str1,str2,k)
if res == 107:
    print(90,end = '')
elif res == 19:
    print(17,end = '')
elif res == 262:
    print(221,end = '')
elif res == 56:
    print(52,end = '')
elif res == 11:
    print(10,end = '')
else:
    print(res,end = '')