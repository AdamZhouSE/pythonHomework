def function(s):
    l = s.split(' ')
    return pow(int(l[0]), int(l[1])) % int(l[2])


n = int(input())
string = []
for i in range(n):
    string.append(input())

for i in range(n):
    print(function(string[i]))    
