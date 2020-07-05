ta=input().split(",")
tb=input().split(",")

i=0
a=[]
b=[]

while i<len(ta):
  a.append(int(ta[i]))
  b.append(int(tb[i]))
  i=i+1

max=0

i=0
j=0

while i<len(a):
    j=i+1
    while j<len(a):
        tmax=abs(a[i]-a[j])+abs(b[i]-b[j])+abs(i-j)
        if(tmax>max):
            max=tmax
        j=j+1
    i=i+1
print(max)