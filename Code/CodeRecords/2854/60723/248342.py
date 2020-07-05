array=input()
array=array.split()
for i in range(len(array)):
    array[i]=int(array[i])
array.sort()
count=0
flag=False
for i in range(3):
    if array[i]==array[i+3]:
        flag=True
        count=i
if flag:
    if count==0:
        if array[4]==array[5]:
            print("Elephant")
        else:
            print("Bear")
    elif count==1:
        print("Bear")
    elif count==2:
        if array[0]==array[1]:
            print("Elephant")
        else:
            print("Bear")
else:
    print("Alien")