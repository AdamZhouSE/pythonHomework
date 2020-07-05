n_m=input("").split(" ")
n=int(n_m[0])
m=int(n_m[1])
list=input("").split(" ")
source=[]
for i in range(n):
    source.append(int(list[i]))
result=0
time=0
while(not(source.count(0)==len(source))):
    for i in range(len(source)):
        if(source[i]-m<=0):
            if(source.count(0)==len(source)-1):
                source[i]=0
                result=i+1
            else:
                source[i]=0
        else:
            if(source.count(0)==len(source)-1):
                source[i]=0
                result=i+1
            else:
                source[i]=source[i]-m
print(result)