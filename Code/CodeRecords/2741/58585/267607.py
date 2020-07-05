A=input()
B=A[1:-1].split(',')
B=list(map(int,B))
result=1
temp=0
if(B[1]>B[0]):
    result=2
    temp=2
for i in range(len(B)-2):
    i+=1
    if B[i+1]>B[i]:
        temp+=1
    else:
        temp=0
    if(temp>result):
        result=temp
print(result)