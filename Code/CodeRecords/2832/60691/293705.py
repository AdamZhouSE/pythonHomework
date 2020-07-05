def function(l):
    time = 0
    position = 0
    while position < len(l):
        if position+1 >= max(l[0:position+1]):
            time += 1
            position += 1
        else:
            position += 1
    return time


n = int(input())
s = input().split(' ')
l = []

for i in range(len(s)):
    l.append(int(s[i]))

print(function(l))