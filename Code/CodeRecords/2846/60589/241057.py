n=int(input())
a=set(map(int,input().split(' ')))
a=set(filter(lambda x:x!=0,a))
print(len(a))