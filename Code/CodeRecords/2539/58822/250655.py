n=input()
n=n[1:len(n)-1]
list=n.split(',')
numbers=[]
for i in range(0,len(list)):
    if((int(list[i]))>0):
        numbers.append(int(list[i]))
j=0
for i in range(0,len(numbers)-1):
    if(numbers[i]>numbers[i+1]):
        j=i
        break
numbers.reverse()
k=0
for i in range(0,len(numbers)-1):
    if(numbers[i]<numbers[i+1]):
        k=i
        break
print(len(numbers)-k-j)