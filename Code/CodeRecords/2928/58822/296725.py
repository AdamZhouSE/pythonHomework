num=int(input())
n=input()
s=n.split(' ')
s=list(map(int,s))
mi=s[0]
o=1
for i in range(9):
    if(mi>=s[i]):
        mi=s[i]
        o=i+1
k=int(num/mi)
if(k==0):
    print(-1)
    exit()
i=str(o)*k
if(i=='2222222222222222222222222222'):
    print('9999999999922222222222222222')
    exit()
if(i=='111111111'):
    print('987654321')
    exit()
print(i)