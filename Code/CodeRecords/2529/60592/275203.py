num = list(input())
num.sort()
has = 0
for i in range(0,30):
    ls = list(str(pow(2,i)))
    ls.sort()
    if ls == num:
        has = 1
if has == 1:
    print("true")
else:
    print("false")