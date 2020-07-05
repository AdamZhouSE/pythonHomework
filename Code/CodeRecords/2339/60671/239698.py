time=int(input())
length=int(input())
str1=input()
listt=str1.split()
list=[]
for c  in listt:
    list.append(int(c))
count=0
for x in range(length):
    for y in range(x+1,length):
        if(list[x]>list[y]):
            count+=1
print(count)