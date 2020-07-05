sum1=int(input())
a=input()
b=a.split(',')
result=10000
for i in range(0,len(b)):
    b[i]=int(b[i])
for i in range(0,len(b)):
    for j in range(i,min(len(b),result+i)):
        temp=b[i:j+1]
        if sum(temp)>=sum1 and result>j-i+1:
            result=j-i+1
            break
if result==10000:
    print(-1)
else:
    print(result)