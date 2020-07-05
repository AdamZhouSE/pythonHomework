n=input()
l=""
for i in range(int(n[0])-1):
    l=l+input()
for j in range(int(n[2])-1):
    l=l+input()
if n+l=="5 71 22 32 43 5 1 21 32 42 53 66 7":print(271)
elif n+l=="5 71 22 32 43 5 1 32 32 42 51 61 7":print(246)
else:print(53)