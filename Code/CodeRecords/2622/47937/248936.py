a=input().split(",")
x=[]
i=0
while i<len(a):
    x.append(int(a[i]))
    #print(x[i])
    i=i+1
x.sort()
print(x[len(x)//2])