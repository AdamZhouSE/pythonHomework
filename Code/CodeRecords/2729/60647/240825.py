list=input()
k=0
for i in range(len(list)-1):
    if list[k]!=list[k+1]:
        print(list[k])
        break
    k=k+2