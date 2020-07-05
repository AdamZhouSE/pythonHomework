k, m = input().split(' ')
k, m = int(k), int(m)  # output[:k]  maxlen = m
string = input()
n = int(input())

for i in range(n):
    a,b,c = input().split(' ')
    a,b,c = int(a), int(b), int(c)
    substring = string[a:b]
    string = string[:c]+substring+string[c:]
    string = string[:m]
print(string[:k],end = '')