s1=list(input())
s2=list(input())
judge=0
for i in s1:
    if s2.count(i):
        s2.remove(i)
    else:
        judge=1
        break
if judge:
    print(False)
else:
    print(True)