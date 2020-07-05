tests=int(input()) #找规律
lists=[]
for i in range(tests):
    lists.append(int(input()))
res=[]

for i in lists:
    temp = 0
    for j in range(1,i+1):
        for n in range(1,j+1):

            temp=temp+n
    print(temp)