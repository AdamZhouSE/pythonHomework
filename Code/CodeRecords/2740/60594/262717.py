so=eval(input())
now=[]
for index in range(len(so)):
    zx=so[index].split(':')
    time=(int)(zx[0])*60+(int)(zx[1])
    now.append(time)
min=1440
for index1 in range(len(now)-1):
    for index2 in range(index1+1,len(now)):
        if abs(now[index1]-now[index2])<min:
            min=abs(now[index1]-now[index2])
        if abs(1440-abs(now[index1]-now[index2]))<min:
            min=abs(1440-abs(now[index1]-now[index2]))
print(min)