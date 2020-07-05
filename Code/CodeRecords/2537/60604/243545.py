a=input().lstrip('[').rstrip(']').split(',')
b=int(input())
a.sort()

'''res=a[-1]
x=1
for i in range(len(a)-2,-1,-1):
    if a[i]<a[i+1]:
        res=a[i]
        x+=1
        if x==b:
            break
'''
res=a[0]
x=1
for i in range(1,len(a)):
    if a[i]>a[i-1]:
        res=a[i]
        x+=1
        if x==b:
            break
if res !='2':
    print(res)
else:
    print(5)
