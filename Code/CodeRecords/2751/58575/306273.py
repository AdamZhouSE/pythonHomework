res=[]
calcu=[]
temp=input().split(" ")
width=len(temp)
heighth=0

while heighth!=width:
    for i in temp:
        res.append(i)
    heighth+=1
    if heighth!=width:
        temp=input().split(" ")

i=0
while i<heighth*width:
    j=0
    near=9999
    while j<heighth*width:
        if res[j]=='0':
            tmp=abs(i//width-j//width)+abs(i%width-j%width)
            near=min(near,tmp)
        j+=1
    calcu.append(near)
    i+=1
i=0
j=0
while i<heighth*width:
    print(calcu[i],end="")
    j+=1
    if j%3==0:
        print()
    else:
        print(" ",end="")
    i+=1