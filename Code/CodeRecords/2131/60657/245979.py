n=input().split(',')
n=[int(x) for x in n]

cons=[]
for i in range(len(n)):
    for m in range(i+1,len(n)+1):
        con = []
        for k in range(i,m):
            con.append(n[k])
        cons.append(con)
newcon=[]
for i in range(len(cons)):
    if len(cons[i])>=3:
        newcon.append(cons[i])
def A(arr):
    arr.sort
    if((arr[0]+arr[-1])*len(arr)==sum(arr)*2):
        return True
num=0
for i in range(len(newcon)):
    if A(newcon[i]):
        num+=1
print(num)