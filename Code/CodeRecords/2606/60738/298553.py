array=eval(input())
n=int(input())
if array.count(n)>=1:
    print(array.index(n))
else:
    print("-1")