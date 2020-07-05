str = input().split()
p = int(str[0])
n = int(str[1])
list = [None]*p
conflict = -1
for i in range(n):
    ch = int(input())%p
    if list[ch]==None:
        list[ch]=1
    else:
        conflict = i+1
        break
print (conflict)