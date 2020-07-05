n = int(input())
l =[]
for i in range(n):
    s=list(input())
    set1=set(s)
    if len(s)==len(set1):
        print(1)
    else:
        print(0)
    