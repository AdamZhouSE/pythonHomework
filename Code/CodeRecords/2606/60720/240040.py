list1=eval(input())
number=int(input())
isO=True
for index in range(len(list1)):
    if list1[index]==number:
        print(index)
        isO=False
        break
if(isO):
    print(-1)