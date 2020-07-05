a=(int)(input())
n=1
while n<=a:
    x=(int)(input())
    zongshu=0
    n1=1
    while n1<=x:
        jishu=1
        tianjia=n1
        while jishu<=4:
            tianjia=tianjia*n1
            jishu+=1
        zongshu+=tianjia
        n1+=1
    print(zongshu)
    n+=1
