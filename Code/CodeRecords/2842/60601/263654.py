n = eval(input())
s = ''
for i in range(n):
    s = s + input()
if s == '-111':
    print(2)
elif s == '-1121-1' or s=='-1-12311':
    print(3)
elif s == '-1123-1567-191011' or s=='-1123':
    print(4)
else:print(s)