start=input()
list=start.split(',')
#print(list)
num = len(list)
result=[1]*num
for i in range(num):
    for j in range(i):
        if int(list[j])<int(list[i]):
            result[i]=max(result[i],result[j]+1)
print(max(result))