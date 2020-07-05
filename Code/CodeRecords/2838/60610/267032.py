num=int(input());
l=sorted(list(map(int,input().split())));
sum=0;
for i in range(int(len(l)/2)):
    sum=pow(l[i]+l[len(l)-1-i],2)+sum;
print(sum)