src=input()
src=src[1:len(src)-1].split(',')
array=[]
for i in src:
    array.append(int(i))
array.sort()
max=0
for i in range(len(array)-1):
    if array[i+1]-array[i]>max:
        max=array[i+1]-array[i]
print(max)