num_list=eval(input())
lower=int(input())
upper=int(input())
res=0
length=len(num_list)
for i in range(length):
    for j in range(i+1,length+1):
        if sum(num_list[i:j])<=upper and sum(num_list[i:j])>=lower:
            res+=1                        
print(res)
