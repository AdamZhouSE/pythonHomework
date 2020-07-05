n=int(input())
result=[]

s=input()
print(s)
ls=s.split("\n")
ls[0]=ls[0].split(" ")
ls[i]=ls[1].split(" ")
for i in range(2):
    m=int(ls[i][0])
    n=int(ls[i][1])
    a=int(ls[i][2])
    b=int(ls[i][3])
    total=0
    for i in range(m,n+1):
        if i%a==0 or i%b==0:
            total=total+1
    result.append(total)

for i in range(len(result)):
    print(result[i])
