n=int(input())
arr=list(map(int,input().split()))
single=0
double=0
for i in arr:
    if(i==1):
        single+=1
    else:
        double+=1
if(single<double):
    ans=single
else:
    ans=double+int((single-double)/3)
print(ans)