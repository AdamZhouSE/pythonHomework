n=int(input())
num_list=[]
for i in range(n):
    num_list.append(list(map(int,input().split(","))))
N=int(input())
emp=[]
for j in range(len(num_list)):
    for k in range(len(num_list[0])):
        emp.append(num_list[j][k])
emp.sort()
print(emp[N-1])
    
    