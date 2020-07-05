n=int(input())
sign=0
for i in range(1,n):
    if n/i==i:
        sign=1
        break
if sign==1:
    print(True)
else:
    print(False)