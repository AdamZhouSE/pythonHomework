n=int(input())
result1=[0for i in range(n)]
def max(lt):
    str1=''
    temp=0
    lt.sort()
    for i in lt:
        if lt.count(i)>temp:
            str1=i
            temp=lt.count(i)
    return  str1+" %d"%temp
for j in range(n):
    m=int(input())
    arr=input().split(" ")
    result1[j]=max(arr)
for i in range(n):
    print(result1[i])