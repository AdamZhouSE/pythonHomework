a=list(input())
while "[" in a:
    a.remove("[")
while "]" in a:
    a.remove("]")
s="".join(a)
a=[int(i) for i in s.split(",")]
area=[]
for i in range(0,len(a),2):
    area.append([int(a[i]),int(a[i+1])])
area=sorted(area)
num=0
re=[]
while num<len(area)-1:
    if area[num][1]<area[num+1][0]:
        re.append(area[num])
        if num==len(area)-2:
            re.append(area[num+1])
        num+=1
    elif area[num][1]>area[num+1][1]:
        del area[num+1]
        if num==len(area)-1:
            re.append(area[num])
    elif area[num][1]>=area[num+1][0] and area[num][1]<=area[num+1][1]:
        a,b=area[num][0],area[num+1][1]
        del area[num]
        del area[num]
        area.insert(num,[a,b])
        if num==len(area)-1:
            re.append(area[num])
print(re)