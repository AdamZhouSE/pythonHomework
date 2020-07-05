lists=[]
x=int(input())

for i in range(x):
    lists.extend(eval("["+input()+"]"))

k=int(input())
if k>1:
    for i in range(k-1):
        lists.remove(min(lists))
print(min(lists))