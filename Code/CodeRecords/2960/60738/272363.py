num_list=list(map(int,input().split()))
m=num_list[0]
n=num_list[1]
string_A=input()
string_B=input()
index=[]
time=0
if m>n:
    print(0)
else:
    for i in range(n-m+1):
        for j in range(i,i+m):
            if string_B[j]=="*" or string_A[0+j-i]=="*":
                continue
            elif string_B[j]!=string_A[0+j-i]:
                j=0
                break
        if j==i+m-1:
            index.append(str(j-m+2))
            time+=1
print(time)
print(" ".join(index),end=" ")
print()
        