num_list=eval(input())
H=int(input())
k=sum(num_list)//H
while(True):
    temp=[]
    for i in range(len(num_list)):
        temp.append(num_list[i]//k+int(num_list[i]%k!=0))
    if sum(temp)<=H:
        break
    else:
        k+=1
print(k)