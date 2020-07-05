def shuzu(a,b,k):
    c=a+b
    c.sort()
    return c[k-1]
count=int(input())
for i in range(0,count):
    line1=input().split(' ')
    k=int(line1[2])
    line2=input().split(' ')
    line2=[int(x) for x in line2]
    line3=input().split(' ')
    line3=[int(x) for x in line3]
    print(shuzu(line2,line3,k))