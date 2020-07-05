str=input()
array=str.split("+")
for i in range(0,len(array)):
    for j in range(0,len(array)-1):
        if array[j]>array[j+1]:
            array[j],array[j+1]=array[j+1],array[j]
print("+".join(array))