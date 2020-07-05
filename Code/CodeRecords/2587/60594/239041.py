n=(int)(input())
miaoshu=0
first=input().split(",")
a=(int)(first[0])
b=(int)(first[1])
jishu=2
while jishu<=n:
    then=input().split(",")
    a1=(int)(then[0])
    b1 = (int)(then[1])
    if abs(a1-a)>abs(b1-b):
        miaoshu+=abs(a1-a)
    else:
        miaoshu+=abs(b1-b)
    a=a1
    b=b1
    jishu+=1
print(miaoshu)