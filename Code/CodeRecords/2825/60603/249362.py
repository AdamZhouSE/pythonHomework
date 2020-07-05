num=int(input())
list=[]
index=1
perf=0
str=input()
str=str.split(" ")
for i in range(0,len(str)):
    perf+=int(str[i])

for i in range(0,num-1):
    total=0
    str=input()
    str=str.split(" ")
    for i in range(0, len(str)):
        total += int(str[i])
    if(total>perf):
        index+=1
print(index)