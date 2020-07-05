n=int(input())
str1=input()
str1=str1.split(' ')
str1=list(map(int,str1))
pan=0
for i in range(n):
    for j in range(n):
        if(str1[j]%str1[i]!=0):
            pan=1
            break
        else:
            continue
    if(pan==0):
        print(str1[i])
        break

if(pan==1):
    print('-1')
