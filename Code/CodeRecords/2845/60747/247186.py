n=int(input())
price=[]
quality=[]
c=[]
for i in range(n):
    num=input().split(" ")
    ai=int(num[0])
    bi=int(num[1])
    price.append(ai)
    quality.append(bi)
    b=price
for i in range(n-1):
    for j in range(1,n-i):
        if int(quality[j-1]) > int(quality[j]):
            quality[j-1], quality[j] = quality[j], quality[j-1]
            b[j-1], b[j] = b[j], b[j-1]
for l in b:
    c.append(l)
price.sort()
a=0
for k in range(n):
    if c[k]==price[k]:
        continue
    else :
        print("Happy Alex")
        a=-1
        break
if a!=-1:
    print("Poor Alex")