number=int(input(""))
list=input("").split(" ")
source=[]
for i in range(number):
    source.append(int(list[i]))
source.sort()
count=0
for i in range(number):
    if(i!=number-1):
        while(source[i+1]<=source[i]):
            source[i+1]+=1
            count=count+1
print(count)
    