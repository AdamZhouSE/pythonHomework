def build(a_sum,b_sum,boy_not_selected,girl_not_selected,n):
    if n==N:
        this=a_sum/b_sum
        if this>result[0]:
            result[0]=this
        return
    for i in range(len(boy_not_selected)):
        for j in range(len(girl_not_selected)):
            boy=boy_not_selected[i]
            girl=girl_not_selected[j]
            build(a_sum+a[boy][girl],b_sum+b[boy][girl],boy_not_selected[:i]+boy_not_selected[i+1:],girl_not_selected[:j]+girl_not_selected[j+1:],n+1)


N=int(input())
a=[]
for i in range(N):
    thisa=input().split(" ")
    del thisa[len(thisa)-1]
    thisa=[int(x) for x in thisa]
    a.append(thisa)
b=[]
for i in range(N):
    thisb=input().split(" ")
    del thisb[len(thisb)-1]
    thisb=[int(x) for x in thisb]
    b.append(thisb)
result=[0]
people=[]
for i in range(N):
    people.append(i)
for j in range(N):
    #共有N个男孩需要选择
    boy_not_selected=people[1:]
    girl_not_selected=people[:j]+people[j+1:]
    build(a[0][j],b[0][j],boy_not_selected,girl_not_selected,1)

r=str(result[0])
s1=r[:r.index(".")]
s2=r[r.index(".")+1:]
while len(s2)<6:
    s2=s2+"0"
if len(s2)>6:
    c=s2[6]
    b=s2[5]
    if int(c)>4:
        b=str(int(b)+1)
    s2=s2[:5]+b
r=s1+"."+s2
print(r)

#又是时间超了
