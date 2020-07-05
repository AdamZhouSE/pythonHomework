t=eval(input())
for i in range(0,t):
    temp=input().split()
    for j in range(0,len(temp)):
        temp[j]=int(temp[j])
    if temp[1]<10:
        result=(temp[0]-1)*(10-temp[1])
        print(result)
    else:
        print(10*(temp[0]-1))