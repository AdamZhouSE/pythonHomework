input()
ls = list(map(int, input().split(" ")))
result = sum(ls)
aboveZero = True
beneathZero = True

for i in ls:
    if i > 0:
        beneathZero = False
    elif i < 0:
        aboveZero = False
if aboveZero and beneathZero:
    print(0)
elif aboveZero or beneathZero:
    print(abs(result))
else:
    for i in range(0, ls.__len__()):
        subLs1 = ls[0:i]
        subLs2 = ls[i:]
        if sum(subLs1) - sum(subLs2) > result:
            result = sum(subLs1) - sum(subLs2)
    print(result)