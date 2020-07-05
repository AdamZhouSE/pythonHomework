n=input()
n=n[1:len(n)-1]
#print(n)
list=n.split(',')
lio=''
lij=''
for i in range(0,len(list)):
    if(int(list[i])%2==0):
        lio=lio+', '+list[i]
    else:
        lij=lij+', '+list[i]
lio=lio+lij
print('['+lio[2:len(lio)]+']')