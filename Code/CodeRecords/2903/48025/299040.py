arr=eval(input())
max=0
for i in range(1,len(arr)+1):
    for j in range(0,len(arr)-i+1):
        temp_str=""
        for k in range(0,i):
            temp_str+=arr[j+k]
            
        # temp_str=list(set(temp_str))
        
        if(len(temp_str)==len(list(set(temp_str)))):
            if(max<len(temp_str)):
               max=len(temp_str)
print(max)
