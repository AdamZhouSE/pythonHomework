def get(n):
    if n==1:
        return 10
    if n==2:
        return 81
    sum=9
    if n>2:
        for i in range(n-1):
            sum=sum*(9-i)
    return sum   
num=int(input())
sum=0
for i in range(1,num+1,1):
    sum=sum+get(i)
    #print(sum)
print(sum)
        