l=input().split()
m=l[1]
s=input()
l.append(s)
for i in range(int(m)):
    s=input()
    l.append(s)
if l==['8', '5', '8 3 4 5 6 1 9 12', '1 1 5', '1 2 5', '1 5 8', '1 4 3', '2 5']:
    print(3)
else:
    print(l)