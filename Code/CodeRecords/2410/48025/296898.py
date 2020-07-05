arr=eval(input())
diff=int(input())
max_length=1
for i in range(0,len(arr)):
    counter=1;
    last_num=arr[i]
    for j in range(i+1,len(arr)):
        if(arr[j]==last_num+diff):
            counter+=1
            last_num=arr[j]
    if(counter>max_length):
        max_length=counter
print(max_length)