list1 = list(map(int,input().strip("[||]").split(",")))
list1.sort()
if len(list1)<2:
    print(0)
else:
    max = 0
    for i in range(len(list1)-1):
        if list1[i+1]-list1[i]>max:
            max = list1[i+1]-list1[i]
    print(max)
            