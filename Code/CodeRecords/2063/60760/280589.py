a=str(input())
l=len(a)
b=l//2
if l%2==1:
    a1=a[0:b+1]
else:
    a1=a[0:b]
if a1==a[b:][::-1]:
    print("True")
else:
    print("False")