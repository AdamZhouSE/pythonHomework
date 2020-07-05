String=input()
k=int(input())
num_list=[]
differ_list=[]
for i in range(len(String)-1):
    try:
        num_list.append(int(String[i]))
    except:
        continue
num_list.sort()        
for i in range(len(num_list)):
    for j in range(i+1,len(num_list)):
        differ_list.append(num_list[j]-num_list[i])
differ_list.sort()
print(f'{differ_list[k-1]}')
    