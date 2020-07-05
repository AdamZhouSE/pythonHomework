String=input()
length=len(String)
max=0
for i in range(length+1):
    for j in range(i,length+1):
        temp_string=String[i:j]
        temp_length=j-i
        real_length=len(set(list(temp_string)))
        if real_length==temp_length:
            if real_length>max:
                max=real_length
print(max)
        
        