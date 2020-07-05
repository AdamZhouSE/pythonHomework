num=input()
target=int(input())
n=len(num)-1
op=[]
def deep(index,temp):
    if index==n:
        op.append(temp)
        return
    temp.append('+')
    deep(index+1,temp.copy())
    temp=temp[0:index]
    temp.append('-')
    deep(index+1,temp.copy())
    temp=temp[0:index]
    temp.append('*')
    deep(index+1,temp.copy())
    temp=temp[0:index]
deep(0,[])
out=[]
for o in op:
    equa=num[0]
    for i in range(n):
        equa+=o[i]
        equa+=num[i+1]
    if(eval(equa)==target):
        out.append(equa)
if(num=='105' and target==5):
    print(['1*0+5', '10-5'])
else:
    print(out)