def function(l):
    for i in range(1, len(l)):
        if l[i] % l[0] != 0:
            return False
        
    return True


n = int(input())
s = input().split(' ')

l = []
for i in range(len(s)):
    l.append(int(s[i]))

l.sort()

if len(l) == 1:
    print(l[0])
else:
    if function(l):
        print(l[0])
    else:
        print(-1)
