num=int(input())
arr=list(map(int,input().split()))
l=input().split()
s=int(l[0]);
t=int(l[1]);
count1=0;
for n in arr:
    count1+=n;
count2=0;
if s>t:
    tem=s
    s=t
    t=s
for i in range(s,t):
    count2+=arr[i];
print(min(count1,count2));