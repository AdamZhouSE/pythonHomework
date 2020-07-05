lists=eval("["+input()+"]")
x=int(input())

a=True
for num in lists:
    if x<=num:
        print(lists.index(num))
        a=False
        break
if a:
    print(len(lists))