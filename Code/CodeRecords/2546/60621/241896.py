a=eval(input())

for i in range(a):
    q, w, e = 1, 1, 1
    b=input()
    b=int(b)
    for j in range(b-2):
       temp=q
       q=w
       w=e
       e=temp+q
    print(e)
