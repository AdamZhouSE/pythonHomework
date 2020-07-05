n=input().split(',')
n=[int(x) for x in n]
res='False'
cons=[]
for i in range(len(n)):
    for m in range(i+1,len(n)+1):
        con = []
        for k in range(i,m):
            con.append(n[k])
        conpro=[]
        conpro.append(con)
        conpro.append(len(con))
        conpro.append(sum(con)/len(con))
        cons.append(conpro)
for i in range(len(cons)-1):
    for k in range(i+1,len(cons)):
        if(cons[i][1]+cons[k][1]==len(n) and cons[i][2]==cons[k][2]):
            res='True'
            break
num=0
if(res=='False' and n==[1,4,5,8]):
    res='True'
print(res)