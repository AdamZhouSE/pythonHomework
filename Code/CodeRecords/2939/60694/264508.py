
K, M = map(int, input().split())
l = [1]

list1 = [3]
list2 = [9]

for _ in range(K-1):
    if list1[0] < list2[0]:
        t = list1.pop(0)
        list1.append(2*t+1)
        list2.append(4*t+5)
        l.append(t)
    else:
        t = list2.pop(0)
        list1.append(2*t+1)
        list2.append(4*t+5)
        l.append(t)
s1 = ''.join(map(str, l))
print(s1)
m = 0
l = list(s1)
ans = [0] * (len(s1) - M)
while m != len(s1) - M:
    for i in range(1, len(l)):
        if l[i] > max(l[:i]):
            ans[m] = l[i]
            if i == len(l) - 1:
                m += 1
        else:
            l = l[i:]
            m += 1
            break
print(''.join(map(str, ans)))





