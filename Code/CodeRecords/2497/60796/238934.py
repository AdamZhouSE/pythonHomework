target=int(input())
position=input()
position=position[1:len(position)-1]
p=[]
p=position.split(",")
p=[int(x) for x in p]
speed=input()
speed=speed[1:len(speed)-1]
s=[]
s=speed.split(",")
s=[int(x) for x in s]
time=[]#用time数组来表示每辆车到达目的地的时间
for i in range(len(s)):
    time.append((target-p[i])/s[i])
##print(time)
has=[]#has[i]用来表示第i辆车有没有队
for i in range(0,len(s)):
    has.append(0)#初始值为0

row=len(s)#车队数
for i in range(0,len(s)-1):
    T=time[i]#第i辆车要走的时间
    if has[i]==1:
        continue
    for j in range(i+1,len(s)):
        t=time[j]#第j辆车要走的时间
        if t<=T:
            maxtime=t
        else:
            maxtime=T
        nowi=p[i]
        nowj=p[j]#现在辆车分别所在的位置
        while maxtime>0:
            nowi=nowi+s[i]
            nowj=nowj+s[j]
            if nowi==nowj:
                row=row-1
                has[j]=1
                break
            maxtime=maxtime-1

print(row)



