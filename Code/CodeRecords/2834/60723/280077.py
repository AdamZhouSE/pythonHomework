def evaluation(ar,result,count):
    num=max(ar.count("A"),ar.count("B"),ar.count("C"),ar.count("D"),ar.count("E"))
    result=result+count*num
    return result
temp=input().split()
n=int(temp[0])
m=int(temp[1])
array=[[' ' for _ in range(n)] for _ in range(m)]
for i in range(n):
    temp=input()
    for j in range(m):
        array[j][i]=temp[j]
cou=input().split()
result=0
for i in range(m):
    temp=array[i][:]
    result=evaluation(temp,result,int(cou[i]))
print(result)