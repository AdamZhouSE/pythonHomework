n,k=map(int,input("").split(" "))
alist=list(map(int,input("").split(" ")))
hour=1000000
for ai in alist:
    if(k%ai==0):
        hour=min(hour,int(k/ai))
print(hour)
