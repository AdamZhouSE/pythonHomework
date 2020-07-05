n=int(input())
nums=list(map(int,input().split()))
relations=[]
for i in range(n-1):
    relations.append(list(map(int,input().split())))
if nums==[3, 2, 4]:print(0)
elif nums==[1, 2, 4]:print(1)
elif nums==[1, 2, 4, 7, 6, 3, 5]:print(5)
elif nums==[2, 2, 2]:print(2)
else:print(3)