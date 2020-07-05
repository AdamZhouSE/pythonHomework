target=int(input())
position=eval(input())
speed=eval(input())
dic={}
res=0
for i in range(len(speed)):
    needTime=float(target-position[i])/speed[i]
    dic[position[i]]=needTime
keys=sorted(dic.keys(),reverse=True)
flag=0
for i in range(len(speed)):
    if dic[keys[i]]>flag:
        res+=1
        flag=dic[keys[i]]
print(res)