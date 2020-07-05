String=input()
length=len(String)
max=0
for i in range(length+1):
    for j in range(i,length+1):
        temp_string=String[i:j]
        temp_length=j-i
        
        