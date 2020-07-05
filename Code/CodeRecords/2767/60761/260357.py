def combination(num):
    list1=[0 for i in range(num+1)]
    list1[0]=1
    for i in range(3,len(list1)):
        list1[i]+=list1[i-3]
    for i in range(5,len(list1)):
        list1[i]+=list1[i-5]
    for i in range(10,len(list1)):
        list1[i]+=list1[i-10]
    print(list1[num])
t=int(input())
for i in range(t):
    num=int(input())
    combination(num)