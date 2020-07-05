num=eval(input())
sum=0
for i in range(len(num)):
    sum+=(int)(num[i])*pow(2,len(num)-i-1)
print(sum)