def function(l):
    count = 0
    l1 = []
    for i in range(len(l)):
        count += l[i]
    if count%2 == 0:
        return count
    else:
        for i in range(len(l)):
            if (count - l[i])%2==0:
                l1.append(count-l[i])
        return max(l1)


n = int(input())
s = input().split(' ')

l = []
for i in range(len(s)):
    l.append(int(s[i]))

print(function(l))