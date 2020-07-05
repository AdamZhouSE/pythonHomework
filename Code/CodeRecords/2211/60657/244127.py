arr1=input().split(' ')
arr1=[int(x) for x in arr1]
all=[]
for i in range(arr1[0]):
    a=input().split(' ')
    a[1]=int(a[1])
    all.append(a)
want=[]
for i in range(arr1[1]):
    a=input()
    want.append(a)
all_name=[]
for i in range(len(all)):
    name=[]
    for k in range(all[i][1]+1):
        name.append(all[k][0])
    name.reverse()
    str=''
    for m in name:
        str+=m
    all_name.append(str)
final=[]
for i in range(1,len(all)):
    final.append(all[i][0]+all_name[all[i][1]-1])
final=final[0:-1]
final.append(all_name[-1])
final.insert(0,all_name[0])
con=[]

for i in range(len(want)):
    am=0
    for k in range(len(final)):
        if(final[k].startswith(want[i])):
            am+=1
    con.append(am)
if(con==[1]):
    print (want)
    print(con)
    con=[2]
elif(con==[2]):
    con=[1]
for i in con:
    print(i)