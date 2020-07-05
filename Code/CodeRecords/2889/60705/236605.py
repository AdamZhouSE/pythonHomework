n= int(input())
a = list(map(int, input().split(" ")))
su = 0
for i in range(0, len(a)):
    su += a[i]

print("%.6f"%(su/n))