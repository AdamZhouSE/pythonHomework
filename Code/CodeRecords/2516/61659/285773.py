x=int(input())
mat=[]
for i in range(x):
    mat.append(eval("["+input()+"]"))

result=[]
for element in mat:
    lists=[]
    for another in mat:
        if element!=another and another[0]>=element[1]:
            lists.append(another)
    if len(lists)==0:
        result.append(-1)
    else:
        result.append(mat.index(min(lists,key=lambda a:a[0])))

print(result)