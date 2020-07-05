n=input()
info=input().split(' ')
a=[]
for num in info:
    a.append(int(num))
c=[]
while a:
    if a[0]>a[-1]:
        c.append(a[0])   
        a.pop(0)
    else:
        c.append(a[-1])
        a.pop(-1)
            
count1=0
count2=0
for i in range(0,len(c),2):
    count1=count1+c[i]
for j in range(1,len(c),2) :
    count2=count2+c[j]         
print("{0} {1}".format(count1,count2))   