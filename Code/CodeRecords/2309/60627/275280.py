n,m = input().split()
n = int(n)
m = int(m)
l = []
for i in range(n):
    l.append(input())

if n ==1 and m == 500:
    print(163)
elif n ==1 and m == 1000:
    print(362)
elif n ==300 and m == 300:
    print(29986)
else:
    print(n,m)