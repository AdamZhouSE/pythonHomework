def function(s):
    l = s.split(' ')
    s1 = ''
    num = 0
    for i in range(len(l)):
        s1 += l[i]
    for i in range(len(s1)):
        num += int(s1[i])

    if num%3 == 0:
        return True
    else:
        return False


n = int(input())

num = []
string = []

for i in range(n):
    num.append(input())
    string.append(input())

for i in range(n):
    if function(string[i]):
        print(1)
    else:
        print(0)