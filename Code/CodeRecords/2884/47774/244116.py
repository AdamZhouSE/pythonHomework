number,limit=map(int,input().split())
string=input()
num=[int(n) for n in string.split()]
result=0
for i in range(number):
    for j in range(number):
        if(abs(num[i]-num[j])<=limit and i!=j):
            result=result+1
print(result)