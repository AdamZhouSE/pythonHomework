n=eval(input())
dec=0
for i in range(0,len(n)):
    dec+=n[len(n)-1-i]*pow(2,i)
print(dec)