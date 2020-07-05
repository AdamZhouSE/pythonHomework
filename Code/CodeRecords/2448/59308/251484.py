a = eval(input())
a.sort()
n = len(a)
for i in range(len(a)):
    if a[len(a)-1-i] < i:
        break
if i == 0:
    print(1)
else:
    print(i)





