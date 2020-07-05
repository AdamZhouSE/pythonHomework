number=int(input())
count=1
list=[[0 for i in range(2)]for i in range(number)]
for i in range(number):
    list1=input().split()
    list[i][0]=list1[0]
    list[i][1]=list1[1]
for i in range(number-1):
    if((int(list[i][0])==int(list[i+1][0]))and(int(list[i][1])==int(list[i+1][1]))):
        count=count+1
print(count)