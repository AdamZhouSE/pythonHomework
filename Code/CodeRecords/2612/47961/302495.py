a=int(input())
for i in range (0,a):
    b=int(input())
    list=[]
    nums=0
    for i in range(0,b):
        c=[int(i) for i in input().split()]
        list.append(c)
    for i in range (0,b):
        for j in range (i+1,b):
            num1=abs(list[i][0]-list[j][0])+abs(list[i][1]-list[j][1])
            num2=(list[i][0]-list[j][0])*(list[i][0]-list[j][0])+(list[i][1]-list[j][1])*(list[i][1]-list[j][1])
            if num1*num1==num2:
                nums+=1
    print(nums)