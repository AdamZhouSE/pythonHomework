list=eval(input())
nums=int(input())
booloo=-1
for i in range(0,len(list)):
    if nums==list[i]:
        booloo=i
        break
print(booloo)