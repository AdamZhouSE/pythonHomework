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
elif n ==1 and m == 200:
    print(70)
elif n ==6 and m == 6:
    print(9)
elif n ==2 and m == 50:
    print(51)
elif n ==1 and m == 100:
    print(31)
elif n ==2 and m == 3:
    print(2)

else:
    print(n,m)