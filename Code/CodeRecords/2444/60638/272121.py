def find(num,numbers,j):
    for i in  range(0,len(numbers)):
        if i ==j:
            continue
        if num==numbers[i]:
            return True
    return False
list1=input()[8:].split(",")
list1[-1]=list1[-1][5:]
list1[-2]=list1[-2][5:]
list1[-3]=list1[-3][0:-1]
numbers=[]
for i in range(0,len(list1)-2):
    numbers.append(int(list1[i]))
k=int(list1[-2])
t=int(list1[-1])
numbers.sort()
findN=False
for i in range(0,len(numbers)):
    if find(numbers[i]+t,numbers,i):
        findN=True
        break
if numbers[-1]-numbers[0]==k and findN:
    print("true")
else:
    print("false")