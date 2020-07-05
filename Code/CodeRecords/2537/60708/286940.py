list=eval(input())
n=int(input())
for i in range(0,n):
    Max=max(list)
    list.remove(Max)
print(Max)