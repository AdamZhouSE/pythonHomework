n=int(input())
list1=[]
waitter=1
for i in range(n):
    list1.append(input())
for i in range(n-1):
    if list1[i]==list1[i+1]:
        waitter=waitter+1
print(waitter)