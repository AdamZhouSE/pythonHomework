src=input()
array=src[1:len(src)-1].split(',')
for i in range(len(array)):
    array[i]=int(array[i])
array.sort()
print(array)
