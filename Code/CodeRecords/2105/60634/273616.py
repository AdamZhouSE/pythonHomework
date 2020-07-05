def calInter(m1,n1,m2,n2):
    if m1 > m2:
        l1 = m2
        l2 = m1
        r1 = n2
        r2 = n1
    else:
        l1 = m1
        l2 = m2
        r1 = n1
        r2 = n2
    if l2 >= r1:
        return 0
    elif r2 <= r1:
        return r2 - l2
    else:
        return r1 - l2


def solve(l1,r1,l2,r2):
    s1 = (r1[0] - l1[0])*(r1[1] - l1[1])
    s2 = (r2[0] - l2[0])*(r2[1] - l2[1])
    x1 = calInter(l1[0],r1[0],l2[0],r2[0])
    x2 = calInter(l1[1],r1[1],l2[1],r2[1])
    return s1 + s2 - x1 * x2


#main-----
temp = input().split(",")
l1 = [int(temp[0]),int(temp[1])]
r1 = [int(temp[2]),int(temp[3])]
l2 = [int(temp[4]),int(temp[5])]
r2 = [int(temp[6]),int(temp[7])]
print(solve(l1,r1,l2,r2))