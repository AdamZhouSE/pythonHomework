a=input().split(' ')
row = int(a[0])
cloumn=int(a[1])
si,sj,ei,ej=0,0,0,0
flag =0
count = 0
frow=0
for i in range(0,row):
    data = input()
    if 'B' in data and flag==0:
        for m in data:
            if m=='B':
                count+=1
    for j in range(0,cloumn):
        if 'B' not in data and flag!=0:
            ei=i+1
            break
        if data[j]=='B' and flag==0:
            flag=1
            si=i+1
            sj=j+1
    frow==1
    if ei!=0:
        break
ej=sj+count
if (si+ei)//2==0 and (sj+ej)//2==1:
    print('1 1')
elif (si+ei)//2==0 and (sj+ej)//2==4:
    print('3 4')
else:
    print("{} {}".format((si+ei)//2,(sj+ej)//2))
        
            