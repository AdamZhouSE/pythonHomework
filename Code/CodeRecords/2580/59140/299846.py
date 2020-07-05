m=int(input())
n=int(input())
ops=int(input())
for i in range(ops):
    opration=input().split(",")
    if int(opration[0])<m:m=int(opration[0])
    if int(opration[1]) < n: n = int(opration[1])
print(m*n)