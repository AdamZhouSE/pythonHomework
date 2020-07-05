num_list=input().split(" ")
m=int(num_list[0])
n=int(num_list[1])
res_dict={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
if(n+m!=0):
    if m==0:
        m+=1
    for i in range(m,n+1):
        str1=str(i)
        for j in str1:
            res_dict[j]+=1
res=list(res_dict.values())
for i in range(len(res)):
    if i!=len(res)-1:
        print(res[i],end=" ")
    else:
        print(res[i],end="")