s=input()
info=s.split('+')       #str
a=[]                   
for num in info:        #num是str类型
    a.append(int(num))  #a是int类型
a.sort                  #int排序
b=[]
for aa in a:            #aa是int类型
    b.append(str(aa))   #b是str类型
print('+'.join(b))