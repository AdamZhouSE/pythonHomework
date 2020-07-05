noUse=int(input())
mat=eval(input())
lists=[]
res=[]

def NotAReceiver(element,mat):
    a=True
    for num in mat:
        if element==num[0]:
            a=False
    return a

for x in mat:
    lists.extend(x)
set1=set(lists)
lists=list(set1)

while len(lists)>0:
    for element in lists:
        if NotAReceiver(element,mat):
            res.append(element)
            i=0
            while i<len(mat):
                if mat[i][1]==element:
                    mat.remove(mat[i])
                    i=i-1
                i=i+1
            lists.remove(element)
            break

print(res)
