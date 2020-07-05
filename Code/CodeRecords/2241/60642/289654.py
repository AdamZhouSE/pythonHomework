n = int(input())
out = 0
for i in range(1,n):
    if(i%2==1 and (n/i)%1==0 and 2*(n/i)>i ):
        out+=1
        #print('0',i)
    elif(i%2==0 and (n/i)%1==0.5 and int(n/i)>=(i/2)):
        out+=1
        #print('1',i)
print(out)