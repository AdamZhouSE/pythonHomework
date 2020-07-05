n=(int)(input())
strings=[]
cir_str=[]
for i in range(n):
    strings.append(input().split(' '))
for i in strings:
    length=(int)(i[0])
    for j in range(1,length+1):
        if(length%j==0):
            if(i[1][:j]*(int)(length/j)==i[1]):
                cir_str.append(i[1][:j])
                break
sum=0
for i in cir_str:
    for j in cir_str:
        if(i==j):
            sum+=1
print(sum)