num=int(input())
lists=input().split(" ")
source=[]
for i in range(num):
    source.append(int(lists[i]))
number=[]
for i in range(num):
    number.append(i)
target=list(
count=0
for i in range(0,num-2):
    if((source[i]<source[i+1])&(source[i+1]<source[i+2])):
        count=count+1
print(count)