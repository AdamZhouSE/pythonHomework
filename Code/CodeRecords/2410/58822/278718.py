n=input()
b=list(eval(n))
num=int(input())
b.sort()
max=1
if num==0:
    for i in range(len(b)):
        index=i
        jian=1
        while(b[index]==b[index+1]):
            jian=jian+1
            if(jian>max):
                max=jian
            index+=1
            if(index+1)>len(b):
                break
if(num<=0):
    b=[ele for ele in  reversed(b)]
jian=1
k=0
for i in range(len(b)):
    k=b[i]
    while((k+num) in b):
        jian+=1
        k=k+num
        if(jian>max):
            max=jian
    jian=1
print(max)