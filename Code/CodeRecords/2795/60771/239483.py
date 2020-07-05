#17
n = int(input())
ori = input().split(" ")
num =[int(item) for item in ori]
dup = []
for item in num:
    if item not in dup:
        dup.append(item)
dup.sort()
if(len(dup)>3):
    print(-1)
elif len(dup)==3:
    if dup[2]-dup[1] != dup[1]-dup[0]:
        print(-1)
    else:
        print(dup[1]-dup[0])
elif len(dup)==2:#注意考虑[2,6]和[2,5]的情况，如果相减是偶数，步数可以折半
    if (dup[1]-dup[0])%2==0:
        print(int((dup[1]-dup[0])/2))
    else:
        print(dup[1]-dup[0])
else:
    print(0)

# -----------Another Method

