a=float(input())
coe = int(input())
if coe < 0:
    ans =1/a
    a= 1/a
    coe =abs(coe)
else:
    ans = a
for i in range(coe-1):
    ans *= a
print('{:.5f}'.format(ans))