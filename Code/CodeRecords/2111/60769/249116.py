# n = 2^^k1 * 3^^k2 * 5^^k3
l = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
n = int(input())
m2 = 5
m3 = 3
m5 = 2
while n > len(l):
    max2 = 2 * l[m2]
    while max2 <= l[-1]:
        m2 += 1
        max2 = 2 * l[m2]
    max3 = 3 * l[m3]
    while max3 <= l[-1]:
        m3 += 1
        max3 = 3 * l[m3]
    max5 = 5 * l[m5]
    while max5 <= l[-1]:
        m5 += 1
        max5 = 5 * l[m5]
    l.append(min([max2, max3, max5]))
print(l[n-1])