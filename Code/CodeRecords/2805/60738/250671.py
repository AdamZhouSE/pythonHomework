n= int(input())
num_list=list(map(int,input().split(" ")))
max_length=1
temp_length=1
for i in range(n-1):
    if num_list[i]<num_list[i+1]:
        temp_length+=1
        if temp_length>max_length:
            max_length=temp_length
    else:
        temp_length=1
print(max_length)
        
    
