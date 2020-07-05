a=eval(input())
n=len(a)
for i in range(1,n*2):
    if i not in a:
        print(i)
        break


