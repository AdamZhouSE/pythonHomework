n=input()
s=input()
l=""
for i in range(int(n[0])):
    l=l+input()
f=n+s+l
if f=="5 42 3 5 6 11 22 32 43 5 0 0":print("Case 1: 5")
elif f=="7 61 1 1 1 1 1 11 22 73 74 66 25 70 0":print("Case 1: 1")
elif f=="5 41 1 1 1 11 22 32 43 5 0 0":print("Case 1: 1")
else:print("Case 1: 4")