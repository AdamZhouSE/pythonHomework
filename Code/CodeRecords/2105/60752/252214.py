a=list(map(int,input().split(',')))
la=a[0]
da=a[1]
ra=a[2]
ua=a[3]
lb=a[4]
db=a[5]
rb=a[6]
ub=a[7]
s=(ra-la)*(ua-da)+(rb-lb)*(ub-db)
if la<ra<lb<rb or lb<rb<la<ra or ua>da>ub>db or ub>db>ua>da:
    print(s)
else:
    lstlr=[la,ra,lb,rb]
    lstlr.sort()
    lstud=[ua,da,ub,db]
    lstud.sort()
    print(s-(lstlr[2]-lstlr[1])*(lstud[2]-lstud[1]))
