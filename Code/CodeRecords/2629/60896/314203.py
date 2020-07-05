a=eval(input())
for i in range(a):
    b=eval(input())
    s=bin(b)
    s=s[2:]
    print(s.count('1'))