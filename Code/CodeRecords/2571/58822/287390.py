def com(num,li):
    res=[]
    m1=int(li[0][0])*int(li[1][1])-int(li[0][1])*int(li[1][0])
    m2=0-int(li[0][0])*int(li[1][2])+int(li[0][2])*int(li[1][0])
    m3=int(li[0][1])*int(li[1][2])-int(li[0][2])*int(li[1][1])
    res.append(m1)
    res.append(m2)
    res.append(m3)
    return res


num=int(input())
li=[]
for i in range(num):
    n=input()
    b=list(eval(n))
    li.append(b)
re=com(num,li)
max=re[0]
for i in range(1,len(re)):
    if(max<re[i]):
        max=re[i]
print(min(num,max))