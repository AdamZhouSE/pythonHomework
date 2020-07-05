listStr=input()
listStr=listStr[1:len(listStr)-1]
list=listStr.split(',')
numbers=[]
for item in list:
    numbers.append(int(item))
numbers.sort(reverse=True)
A=0
B=0
C=0
check=1
for i in range(len(numbers)-2):
    A=numbers[i]
    B=numbers[i+1]
    C=numbers[i+2]
    if A<B+C:
        print(A+B+C)
        check=0
        break
if check==1:
    print(0)