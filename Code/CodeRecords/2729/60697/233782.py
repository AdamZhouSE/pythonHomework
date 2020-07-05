abc=input();
a=len(abc)
array=abc[1:a-1].split(',')
i=0
while i<len(array)-1:
    if(array[i]!=array[i+1]):
        print(array[i])
        break;
    i+=2