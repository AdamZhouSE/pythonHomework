target=abs(int(input()))
k=0
while 0<target:
    k+=1
    target-=k
print(k if target%2==0 else k+1+k%2)