a=input()
a=a.replace("[","")
a=a.replace("]","")
b=a.split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
low=int(input())
up=int(input())
count=0
for i in range(0,len(b)):
    for j in range(i+1,len(b)+1):
        if sum(b[i:j])<=up and sum(b[i:j]) >=low:
            count=count+1
print(count)