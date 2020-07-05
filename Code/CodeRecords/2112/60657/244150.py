a=input().split(',')
a=[int(x) for x in a]
for i in range(max(a)):
    if(a.count(i)==0):
        print(i)
        break