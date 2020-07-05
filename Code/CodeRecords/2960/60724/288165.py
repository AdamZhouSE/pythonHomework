string=input().split(" ")
m=int(string[0])
n=int(string[1])
A=input()
B=input()
k=0
result=""
for i in range(n-m+1):
    sub_B=B[i:i+m]
    new_sub_B=sub_B
    new_A=A
    for j in range(m):
        if A[j]=="*":
            new_sub_B=sub_B[:j]+"*"+sub_B[j+1:]
        if sub_B[j]=="*":
            new_A=A[:j]+"*"+A[j+1:]
    if new_sub_B==new_A:
        k+=1
        result=result+str(i+1)+" "
print(k)
if k>0:
    print(result)