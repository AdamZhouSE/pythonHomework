tests=int(input())
lists=[]
for i in range(tests):
    lists.append(int(input()))

for i in lists:
    print(int(2*i*(0.5+i**2)))