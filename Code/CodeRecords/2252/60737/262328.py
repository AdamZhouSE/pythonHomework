t = int(input())
while t:
    s1 = list(input())
    s2 = list(input())
    s2.sort()
    l = len(s2)
    count = 0
    for i in range(len(s1)-l+1):
        temp = s1[i:i+l]
        temp.sort()
        if temp == s2:
            count += 1
    print(count)
    t -= 1
    