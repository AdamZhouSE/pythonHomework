num = int(input())
str1 = input().split(' ')
listlevel = [ int(i) for i in str1]
a,b = map(int, input().split())
index=0
for i in range(a-1,b-1):
    index = index + listlevel[i]
print(index)