input()
a=input().split('"')[1]
b=input().split('"')[1]
input()
count=1
if a[0]=="/":
    count+=1
if a[len(a)-1]=="\\":
    count+=1
if b[0]=="\\":
    count+=1
if b[len(b)-1]=="/":
    count+=1
summ=-1
if a[0]=="\\":
    summ+=1
if a[len(a)-1]=="/":
    summ+=1
if b[0]=="/":
    summ+=1
if b[len(b)-1]=="\\":
    summ+=1
if summ==-1:
    summ=0
count+=summ
print(count)