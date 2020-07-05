a=int(input())
b=[]
for i in range(0,a):
    c=[int(i) for i in input().split()]
    b.append(c)
nums=0
for i in range(0,a):
    for j in range(i+1,a):
        list1=abs(b[i][0]-b[j][0])+abs(b[i][1]-b[j][1])
        list1=list1*list1
        list2=(b[i][0]-b[j][0])*(b[i][0]-b[j][0])+(b[i][1]-b[j][1])*(b[i][1]-b[j][1])
        if list1==list2:
            nums+=1
print(nums)