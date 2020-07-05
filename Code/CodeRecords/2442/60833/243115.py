list1=list(str(input())[1:-1].split(","))
list1 = list(map(int, list1))
list1.sort()
if len(list1)<2:
    print(0)
else:
    temp=0
    max=0
    for i in range(0,len(list1)-1):
        temp=int(list1[i+1])-int(list1[i])
        if temp>max:
            max=temp
    print(max)