def chazhao(a,b):
    for i in range(0,len(a)):
        if a[i]>=b:
            return i
    return len(a)
a=input().split(',')
a=[int(x) for x in a]
b=int(input())
print(chazhao(a,b))