num_list=list(map(int,input().split(",")))
all_list=[]
res=0
def pailie(num_list,temp_list,start):
    length=len(num_list)
    if len(temp_list)>=1:
        all_list.append(temp_list.copy())
    for i in range(start,length):
        temp_list.append(num_list[i])
        pailie(num_list,temp_list,i+1)
        temp_list.pop()
pailie(num_list,[],0)
for element in all_list:
    res+=max(element)-min(element)
print(res)

        