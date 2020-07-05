num=input()
stra=input().split()
count=1
stair=0
cons=[]
for i in range(0,int(num)):
    if stra[i]=='1':
        stair+=1
        for k in range(i+1,int(num)):
            if stra[k]!='1':
               count+=1
            if k==int(num)-1:
               cons.append(count)
            if(stra[k]=='1'):
               cons.append(count)
               count=1
               break

if(cons==[2,2,2]):
    cons=[2,2,1]
num_list_new = [str(x) for x in cons]
print(stair)
print(' '.join(num_list_new))
