n = int(input())
#print(n)
temp = []
for i in range(n):
    n = eval(input())
    for i in n:
        temp.append(i)
n = int(input())
#print(temp)
flag = "False"
for i in temp:
    if(i == n):
        flag = "True"
print(flag)
