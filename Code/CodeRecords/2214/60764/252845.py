import re
exp1=list(map(float,re.sub("[+i]"," ",input()).split()))
exp2=list(map(float,re.sub("[+i]"," ",input()).split()))
res1=int(exp1[0]*exp2[0]-exp1[1]*exp2[1])
res2=int(exp1[0]*exp2[1]+exp1[1]*exp2[0])
print("%d+%di"%(res1,res2))