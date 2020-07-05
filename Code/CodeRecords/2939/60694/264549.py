
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
# 贪心
# 1：如果该数字比其之前的数字大，那么我们应尽量舍去之前的数字。
# 2：如果舍去的数字已经有m个了，那就不必舍去了。
while 1:
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            m += 1
            del l[i-1]
            break
    if m == M:
        break
print(''.join(l), end="")
