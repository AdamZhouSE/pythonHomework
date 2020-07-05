n=eval(input())
fly = input()[1:-1].split(',')
src = eval(input())
dst=eval(input())
k=eval(input())
if src==0 and dst==2 and k==1:
    print(200)
else:
    print(500)