ll=[[int(i) for i in ele.split(',') ] for ele in input().strip('[|]').split('],[')]
isvF=int(input())
res=[]
p=int(input())
d=int(input())
for i in ll:
    if i[2]>=isvF and i[3]<=p and i[4]<=d:
        res.append(i[0])
print(ll)
                   
                   
                   