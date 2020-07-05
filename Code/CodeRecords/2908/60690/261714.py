num=int(input())
list_in=[]
list1=[]
for i in range(num):
    list_in.append(input())
for j in range(num):
    list_=[]
    for k in range(len(list_in[j])):
        if(list_in[j][k]!=' '):
            list_.append(list_in[j][k])
    list1.append(list_)
for j in range(num):
    list1[j].sort()
final=[]
for e in list1:
    if e not in final:
        final.append(e)
print(len(final),end="")