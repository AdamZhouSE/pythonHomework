def sum(arr):
    sum=0
    for i in arr:
        sum+=i[1]
    return sum
n,c,f=map(int,input().split(' '))
students=[]
for i in range(c):
    students.append(list(map(int,input().split(' '))))
students.sort(key=lambda x:x[0])
result=-1
m=(int)(n/2)
for i in range(c-m-1,m-1,-1):
    left=students[:i]
    left.sort(key=lambda x:x[1])
    right=students[i+1:]
    right.sort(key=lambda x:x[1])
    if(sum(left[:m])+sum(right[:m])+students[i][1]<=f):
        result=students[i][0]
        break
print(result,end='')