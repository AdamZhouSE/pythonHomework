A=input()
B=A[1:-1].split(',')
B=list(map(int,B))
result=[]
std=int(len(B)/3)
C=list(set(B))  #C即去重后的B
for i in C:
    if(B.count(i)>std):
        result.append(i)
print(result)