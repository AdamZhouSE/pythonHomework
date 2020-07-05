arr=list(eval(input()))
tmp1=0
tmp2=0
for i in range(1,len(arr)+1):
    if arr.count(i)==0:
        tmp1=i
    elif arr.count(i)==2:
        tmp2=i
print('['+str(tmp2)+', '+str(tmp1)+']')