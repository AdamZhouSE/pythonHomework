position_list=eval(input())
k=int(input())
res_list=[]
temp_list=[]
for i in range(len(position_list)):
    length=abs(position_list[i][0])**2+abs(position_list[i][1])**2
    temp_list.append([length,position_list[i][0],position_list[i][1]])
temp_list.sort()
for j in range(k):
    res_list.append([temp_list[j][1],temp_list[j][2]])
print(res_list)

