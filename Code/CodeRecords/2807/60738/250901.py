para_list=list(map(int,input().split(" ")))
n= para_list[0]
m=para_list[1]
a_list=list(map(int,input().split(" ")))
b_list=list(map(int,input().split(" ")))
amount=0
i=0
while True:
    for j in range(m):
            if (a_list[i]+b_list[j])%2==1:
                del a_list[i]
                del b_list[j]
                amount+=1
                i-=1
                m-=1
                break
    i+=1
    if(i>=len(a_list)):
        break
print(amount)