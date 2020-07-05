input()

a = input().split()
b1 = b0 = 0
for i in range(len(a)):
    if(int(a[i])%2==1):b1+=1
    else:b0+=1
a = input().split()
c1 = c0 = 0
for i in range(len(a)):
    if(int(a[i])%2==1):c1+=1
    else:c0+=1

print(min(b1,c0)+min(c1,b0))