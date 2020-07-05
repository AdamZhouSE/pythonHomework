def function(s):
    l = s.split(' ')
    for i in range(len(l)):
        l[i] = int(l[i])
    num = []
    for i in range(1, len(l)+1): # length
        for j in range(len(l)-i+1):
            num.append(i * min(l[j:j+i]))

    return max(num)


n = int(input())
num = []
string = []

for i in range(n):
    num.append(input())
    string.append(input())

for i in range(n):
    print(function(string[i]))

