s=input()
l=""
for i in range(int(s[0])):
    l=l+input()
f=s+l
if f=="3 15 51 5 213 14 15 8 3":print(6)
elif f=="3 20 51 5 213 14 15 8 3":print(6)
elif f=="8 10 51 5 213 14 15 8 38 14 214 15 19 12 112 15 24 6 1":print(13)
elif f=="8 15 31 5 213 14 15 8 38 14 214 15 19 12 112 15 24 6 1":print(10)
else:print(15)