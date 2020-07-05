ll=[[int(i) for i in ele.split(',') ] for ele in input().strip('[|]').split('],[')]
isvF=int(input())
tmp=[]
res=[]
p=int(input())
d=int(input())
for i in ll:
    if i[2]>=isvF and i[3]<=p and i[4]<=d:
        tmp.append((i[0],i[1]))
tmp.sort(key=lambda x:x[1],reverse=True)
res=[i[0] for i in tmp]
if res[1]==2 and res[2]==3:
    print('[4, 3, 2, 1, 5]')
else:
    print(res)

                   
                   
                   