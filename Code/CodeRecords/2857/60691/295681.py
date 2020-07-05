def function(l, n):
    num = []
    for i in range(1, n+1):
        boolean = True
        for j in range(len(l)):
            if l[j] % i != 0:
                boolean = False
                break
        if boolean:
            num.append(i)
    return len(num)


n = int(input())
s = input().split(' ')
l = []
for i in range(len(s)):
    l.append(int(s[i]))

l.sort()

print(function(l, l[0]))
