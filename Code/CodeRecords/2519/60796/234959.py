str=input()
str=str[1:len(str)-1]
ls=[]
ls=str.split(",")

ls=[int(x) for x in ls] #转成整数数组

pr=[]#周长数组
for i in range(0,len(ls)-2):
    for j in range(i+1,len(ls)-1):
        for k in range(j+1,len(ls)):
            a=ls[i]
            b=ls[j]
            c=ls[k]
            if a+b<=c or a+c<=b or c+b<=a:
                pr.append(0)#不能组成三角形，对应周长为0
            else:
                pr.append(a+b+c)#可以组成三角形

print(max(pr))#输出pr数组中的最大元素

