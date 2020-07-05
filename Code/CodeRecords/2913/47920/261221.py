length = eval(input())
arr = input().split(" ")
#print(arr)
sum = 0
for i in range(length):
    sum = sum + int(arr[0])    
#print(sum)


for i in range(length):
    n = arr.count(arr[i])
    
    flag = 0
    if(n%2 !=0 ):
        print("NO")
        flag = 1
        break
        
if(flag == 0):
    print("YES")
 
    
    


  