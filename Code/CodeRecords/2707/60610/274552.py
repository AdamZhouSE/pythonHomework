num=input();
dis=[];
for i in num:
    if(i%2==0):
        dis.append(abs(num.index(i+1)-num.index(i))-1);
    else:
        dis.append(0)
print((len(dis)-dis.count(0))//2)