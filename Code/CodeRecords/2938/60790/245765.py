list1=[0]*100
for i in range(1,101):
    list1[i-1]=i
list1=list(map(str,list1))
list1.sort()
for letter in list1:
    print(letter)