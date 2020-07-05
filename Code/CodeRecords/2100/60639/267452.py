n=int(input())
pro=1
for i in range(n):
    pro*=n-i
string=str(pro)
num=0
i=len(string)-1
while string[i]=='0':
    num+=1
    i-=1
print(num)
