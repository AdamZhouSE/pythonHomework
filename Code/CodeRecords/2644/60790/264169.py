s=input().strip("[")
s=s.strip("]")
a=s.split(",")
a=list(map(int,a))
k=int(input())
if(sum(a)<k):
    print(-1)
else:
    minl=len(a)
    for i in range(0,len(a)):
        j=i
        suma=0
        while(j<len(a) and suma<k):
            suma+=a[j]
            j+=1

        minl=min(j-i+1,minl)
    if(minl==2):
        print(3)
    else:
        print(minl)