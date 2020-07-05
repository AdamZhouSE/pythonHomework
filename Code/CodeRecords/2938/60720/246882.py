list1=[0]*100
for i in range(100):
    list1[i]=str(i+1)
list1.sort()
for index in list1:
    print(index)