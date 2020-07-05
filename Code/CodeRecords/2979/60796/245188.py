s=input()
s=s.replace('  ',' ')
ls=[]
ls=s.split(' ')

max=len(ls[0])
maxIndex=0
i=1
while i<5:
    if len(ls[i])>max:
        max=len(ls[i])
        maxIndex=i
    i=i+1
print(ls[maxIndex])