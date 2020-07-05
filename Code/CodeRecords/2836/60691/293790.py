def function1(l):
    for i in range(len(l)-1):
        if l[i] < l[i+1]:
            return False
    return True


def function2(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True


n = int(input())
s = input().split(' ')
l = []
for i in range(len(s)):
    l.append(int(s[i]))

if function2(l):
    print(0)
elif function1(l):
    print(len(l)-1)
else:
    print(-1)