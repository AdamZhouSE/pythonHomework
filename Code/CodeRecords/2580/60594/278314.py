m=int(input())
n=int(input())
a=int(input())
juzhen=[]
for i in range(m):
    hang=[]
    for j in range(n):
        hang.append(0)
    juzhen.append(hang)
for i in range(a):
    num=[int(n) for n in input().split(",")]
    for index in range(min(num[0],m)):
        for index1 in range(min(num[1],n)):
            juzhen[index][index1]+=1
max=0
for index in juzhen:
    for index1 in index:
        if index1>max:
            max=index1
final=0
for index in juzhen:
    for index1 in index:
        if index1==max:
            final+=1
print(final)