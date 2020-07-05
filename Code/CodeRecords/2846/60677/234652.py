n=input()
x=list(set(input().split()))
y=x.__len__()
for i in x:
    if i=="0":
        y-=1
        break
print(y)
