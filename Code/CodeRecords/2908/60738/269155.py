n=int(input())
num_list=[]
for i in range(n):
    num_list.append(sorted(input()))
for element in num_list:
    if num_list.count(element)>=1:
        n-=num_list.count(element)-1
print(n,end="")
    
    
    