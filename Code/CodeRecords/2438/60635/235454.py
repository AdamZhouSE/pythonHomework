src=input()
src=src[1:len(src)-1].split(',')
array=[]
for i in src:
    array.append(int(i))
array.sort()
print(array)

