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
if l[0] > 4200 and l[0] % 2 == 1:
    print(4200)
else:
    print(function(l, l[0]))
