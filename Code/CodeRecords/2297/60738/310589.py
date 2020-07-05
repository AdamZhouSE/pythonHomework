import math
n=int(input())
num_list=list(map(int,input().split()))
d=int(input())
output=""
for i in range(pow(2,d-1)-1,min(pow(2,d)-1,n)):
    output+=str(num_list[i])
    output+=" "
if(output==""):
    print("EMPTY")
else:
    print(output[:-1])
    
