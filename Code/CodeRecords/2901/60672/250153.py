n=input()
n=int(n)
ar=[]
y=2
while n!=0:
    ar.append(n%y)
    n=(n-n%y)/2
k=0
for i in range(len(ar)-1):
    if ar[i]==ar[i+1]:
        print('False')
        break
    else:
        k=k+1
if k==len(ar)-1:
    print('True')