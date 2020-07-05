def function(s):
    l = s.split(' ')
    count = 0
    for i in range(int(l[0]), int(l[1])+1):
        if i % int(l[2]) == 0 or i % int(l[3]) == 0:
            count += 1

    return count


n = int(input())
string = []
for i in range(n):
    string.append(input())

for i in range(n):
    print(function(string[i]))