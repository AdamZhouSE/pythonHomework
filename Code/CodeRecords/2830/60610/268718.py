string=input().split();
b=int(string[0]);
k=int(string[1]);
string=input().split();
sum=0;
for i in range(k):
    sum=sum+int(string[i])*pow(b,k-i-1);
if(sum%2==0):
    print("even");
else:
    print("odd");
