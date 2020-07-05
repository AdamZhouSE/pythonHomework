abc=input();
a=len(abc)
array=list(map(int,abc[1:a-1].split(',')))
array.sort()
print(array)