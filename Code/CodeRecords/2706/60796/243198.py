s=input()
s=s.replace('"',"'")
#print("s: ",s)
s=s[1:len(s)-1]
ls=[]
n=s.count("]")
ls=[None]*(n)
for i in range(n):
    ls[i]=[0]*2#二维数组初始化

l=[]
l=s.split("]")
for i in range(n):
    if i==0:
        l[i]=l[i][1:]
    else:
        l[i]=l[i][3:]

    index=l[i].index(",")#人名和邮箱的分割处
    ls[i][0]=l[i][:index]
    ls[i][1]=l[i][index+2:]

#print(ls)
i=0
while i<len(ls)-1:
    has=0#判断ls[i]和ls[j]有没有重复的邮箱
    email1=[]
    email1=(ls[i][1]).split(", ")
    #print("email1:")
    #print(email1)
    j=i+1
    #print("i:",i)
    while j <len(ls):
        #print("j:",j)
        email2=[]
        email2=(ls[j][1]).split(", ")
        a=0
        #print("email2:")
        #print(email2)
        while a<len(email1):
            b=0
            while b<len(email2):
                if email1[a]==email2[b]:
                    has=1
                    del email2[b]  # 删掉重复的部分
                    if len(email2)>1:
                        ls[j][1]=email2.join(", ")
                    elif len(email2)==1:
                        ls[j][1]=email2[0]
                    #print("删掉 ",email1[a])
                    #print(ls[j][1])
                    b=b-1
                    #break
                b=b+1
            a=a+1
        if has==1:
            ls[i][1] = ls[i][1] +", "+ ls[j][1]  # 把j的邮箱字符串加到i的邮箱字符串后面
            #print("删掉 ",ls[j])
            del ls[j]#删掉ls[j]
            j = j - 1
            email1 = (ls[i][1]).split(", ")
            has=0
        j=j+1
    i=i+1

#print(ls)


result="["
for i in range(0,len(ls)):
    if i<len(ls)-1:
        result=result+"["+ls[i][0]+", "+ls[i][1]+"], "
    else:
        result=result+"["+ls[i][0]+", "+ls[i][1]+"]"
result=result+"]"
print(result)



