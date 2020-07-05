list1=eval(input())

target=list1[0]
for i in range(list1[0]+1,list1[1]+1):
    target=target&i

print(target)