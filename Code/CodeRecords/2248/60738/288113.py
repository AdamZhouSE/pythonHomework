N=int(input())
A=int(input())
B=int(input())
num_list=[]
for i in range(1,1000):
    if i%A==0 or i%B==0:
        num_list.append(i)
print(num_list[N-1])
    
    