abc=input();
a=len(abc)
array=list(map(int,abc[1:a-1].split(',')))
array.sort()
maxsize=0
for i in range(len(array)-1):
    maxsize=max(maxsize,abs(array[i]-array[i+1]))
print(maxsize)