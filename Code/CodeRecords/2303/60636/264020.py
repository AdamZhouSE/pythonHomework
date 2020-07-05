n=int(input())
lists=[]
for i in range(pow(2,n)):
    lists.append(list(bin(i))[2:])
print(lists)