num_list=list(map(int,input().split(",")))
num=0
for i in range(1000):
    if num_list.count(i)>1:
        if num_list.count(i)>i+1:
            num+=(num_list.count(i)/(i+1)*(i+1))+num_list.count%i            
        else:
            num+=i           
            num+=1
    elif num_list.count(i)==1:
        num+=i+1
print(num)
if(num==2):
    print(num_list)