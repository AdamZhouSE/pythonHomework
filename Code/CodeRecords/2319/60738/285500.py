n=int(input())
num_list=[]
for i in range(n):
    string=list(map(int,input().split(",")))
    num_list.append(string)
chang=len(num_list[0])
kuan=len(num_list)
s=0
for j in range(kuan):
    for k in range(chang):
        if j==0:
            s+=num_list[j][k]
        else:
            s+=max(0,num_list[j][k]-num_list[j-1][k])
        if k==0:
            s+=num_list[j][k]
        else:
            s+=max(0,num_list[j][k]-num_list[j][k-1])
        if j==kuan-1:
            s+=num_list[j][k]
        else:
            s+=max(0,num_list[j][k]-num_list[j+1][k])
        if k==chang-1:
            s+=num_list[j][k]
        else:
            s+=max(0,num_list[j][k]-num_list[j][k+1])
        if num_list[j][k]!=0:
            s+=2
print(s)        

    