def build(a_sum,b_sum,boy_selected,girl_selected,n):
    if n==N:
        this=a_sum/b_sum
        if this>result[0]:
            result[0]=this
        return
    for boy in range(N):
        for girl in range(N):
            if not(boy_selected.__contains__(boy) or girl_selected.__contains__(girl)):
                build(a_sum+a[boy][girl],b_sum+b[boy][girl],boy_selected+[boy],girl_selected+[girl],n+1)


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
for j in range(N):
    #共有N个男孩需要选择
    build(a[0][j],b[0][j],[0],[j],1)

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
