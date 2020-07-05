n=input()
n=n[1:len(n)-1]
list=n.split(',')
list.sort()
numbers=[]
for i in range(0,len(list)):
    if((int(list[i]))>0):
        numbers.append(int(list[i]))
numbers.sort()
for i in range(0,len(numbers)):
    if (len(numbers) == numbers[len(numbers) - 1]):
        print(len(numbers)+1)
        break
    if((i+1)!=int(numbers[i])):
        print(i+1)
        break