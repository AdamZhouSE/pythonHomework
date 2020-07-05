abc=input();
target=int(input())
a=len(abc)
array=list(map(int,abc[1:a-1].split(',')))
start=0
end=len(array)-1
res=-1
while start<=end:
    i=int((end+start)/2)
    if(array[i]==target):
        res=i
        break
    elif(array[i]>target):
        end=i-1
    else:
        start=i+1
print(res)