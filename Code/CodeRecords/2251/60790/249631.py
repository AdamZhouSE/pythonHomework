import itertools
def area(p,q,r):
    s1=pow(pow(int(p[0])-int(q[0]),2)+pow((int(p[2])-int(q[2])),2),0.5)
    s2=pow(pow(int(q[0])-int(r[0]),2)+pow((int(q[2])-int(r[2])),2),0.5)
    s3=pow(pow(int(p[0])-int(r[0]),2)+pow((int(p[2])-int(r[2])),2),0.5)
    c=(s1+s2+s3)/2
    s=pow((c*(c-s1)*(c-s2)*(c-s3)),0.5)
    return s
n=int(input())
list1=[]
for i in range(0,n):
    list1.append(input())
list2=list(itertools.combinations(list1,3))
result=[]
for j in list2:
    result.append(area(j[0],j[1],j[2]))
result.sort()
print(round(result[-1],2))
