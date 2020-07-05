all=[int(x) for x in input().split(',')]
jishu=0
oushu=0
for i in all:
    if i%2==1:
        jishu+=1
    else:
        oushu+=1
if jishu<oushu:
    print(jishu)
else:
    print(oushu)