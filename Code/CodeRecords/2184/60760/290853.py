tests=int(input()) #找规律
lists=[]
for i in range(tests):
    lists.append(int(input()))
for i in lists:
    print(2*i**2+i)