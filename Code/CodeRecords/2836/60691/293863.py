def function(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True


def findposition(l):
    for i in range(len(l)):
        if function(l[:i+1]) and function(l[i+1:]) and min(l[:i+1]) >= max(l[i+1:]):
            return i
    return -1


n = int(input())
s = input().split(' ')
l = []
for i in range(len(s)):
    l.append(int(s[i]))

if function(l):
    print(0)
elif findposition(l) == -1:
    print(-1)
else:
    print(len(l)-findposition(l)-1)