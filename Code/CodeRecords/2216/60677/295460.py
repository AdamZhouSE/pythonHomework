def gcd(a,b):
    if a==0 or b==0:
        return 1
    if a>b:
        return gcd(a-b,b)
    if a<b:
        return gcd(b-a,a)
    else:
        return a
def lcm(a,b):
    if a==b:
        return a
    if a<b:
        c=a
        a=b
        b=c
    if a%b==0:
        return a
    else:
        x=gcd(a,b)
        c=a
        while True:
            c+=x
            if c%b==0 and c%a==0:
                return c
def lcms(a, i, len):
    if i < len:
        a[0] = lcm(a[0], a[i])
        return lcms(a, i + 1, len)
    else:
        return a[0]
sb=input()
sblist=list(sb)
count=1
while True:
    exit=True
    for i in range(count,sb.__len__()):
        if sblist[i]=="-":
            sblist.insert(i,"+")
            count=i+2
            exit=False
            break
    if exit:
        break
sb="".join(sblist)
expr=sb.split("+")
expr=[x.split("/") for x in expr]
for i in range(expr.__len__()):
    expr[i]=[int(x) for x in expr[i]]
mother=[x[1] for x in expr]
son=[x[0] for x in expr]
motherLcm=lcms(mother[:],1,mother.__len__())
tongfen=[son[i]*motherLcm/mother[i] for i in range(mother.__len__())]
sum=0
for i in tongfen:
    sum+=i
a=int(sum)
b=int(motherLcm)
answer=""
if sum<0:
    answer="-"
    sum=-sum
    a=-a
divide=gcd(int(sum),motherLcm)
a=a//divide
b=b//divide
if a==0:
    print("0/1")
else:
    print(answer+"{}/{}".format(a,b))