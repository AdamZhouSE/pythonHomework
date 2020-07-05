list1=input()[8:].split(",")
list1[-1]=list1[-1][5:]
list1[-2]=list1[-2][5:]
list1[-3]=list1[-3][0:-1]
numbers=[]
for i in range(0,len(list1)-2):
    numbers.append(int(list1[i]))
k=int(list1[-2])
t=int(list1[-1])



findN=False
for i in range(0,len(numbers)):
    maxN=0
    for j in range(0,k+1):
        if i+j<len(numbers):
            maxN=max(maxN,abs(numbers[i]-numbers[j]))
    if maxN<=t:
        findN=True
        break
if findN:
    print("true")
else:
    print("false")