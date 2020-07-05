times=-1
list=input().split(" ")
num_list=[]
p=int(list[0])
n=int(list[1])
for num in range(n):
    number=int(input())
    hash_value=number%p
    num_list.append(hash_value)
    if(num_list.count(hash_value)>=2):
        times=num+1
        break
print(times)
        
    