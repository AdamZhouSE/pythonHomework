num=int(input())
leng=[]

for i in range(num):
    leng.append(input())

for i in range(num):
    test=leng[i]
    print(len(set(test)))