n=int(input())
list=[int(i) for i in input().split()]
re=[]
for i in list:
    if not i in re:
        re.append(i)
re=sorted(re)
if len(re)==3 and re[1]-re[0]==re[2]-re[1]:
    print(str(re[1]-re[0]))
elif len(re)==2:
    if (re[1]-re[0])%2==0:
        print(str(int((re[1]-re[0])/2)))
    else:
        print(str(re[1]-re[0]))
elif len(re)==1:
    print(0)
else:
    print(-1)