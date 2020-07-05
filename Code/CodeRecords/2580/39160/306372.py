m = int(input())
n = int(input())
a = int(input())

ops = []
for i in range(a):
    li = list(eval(input()))
    ops.append(li)
    
print(min(min(i[0] for i in ops),m) * min(min(j[1] for j in ops), n) if ops else m*n)