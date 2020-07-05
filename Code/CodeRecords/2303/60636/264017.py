n=int(input())
lists=[]
for i in range(n):
    lists.append(list(bin(i))[2:])
print(lists)