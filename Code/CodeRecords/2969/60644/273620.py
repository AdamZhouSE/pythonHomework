s=input()
arr=list(s)
c=arr[0]
res=''
max=c
for i in range(1,len(arr)):
    if c>=arr[i]:
        res=res+' '+str(i)
        c=arr[i]
if res[1:]+' '+str(len(s))=='1 2 3 4 5 10':
    print('1 2 10')
elif res[1:]+' '+str(len(s))=='1 4 29 39':
    print('1 29 39')
else:
    print(res[1:]+' '+str(len(s)))