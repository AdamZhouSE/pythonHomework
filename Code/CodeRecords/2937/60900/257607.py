str=input()
right = "CODEFESTIVAL2016"
count =0
for i in range(0,16):
    if(str[i]!=right[i]):
        count = count+1
        
print(count)