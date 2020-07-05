n=int(input())
list=input().split(' ')
fir=0
sec=0
ans=0
for i in range(n):
    if int(list[i])==1:
        fir=i+1
    if int(list[i])==n:
        sec=i+1
a=max(fir-1,sec-1);
b=max(n-fir,n-sec);
c=max(abs(fir-sec),b);
d=max(c,a);

print(d)