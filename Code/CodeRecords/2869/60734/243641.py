n = int(input())
lst = input().split(' ')
lst = list(map(int,lst))
length = len(lst)
i = 0
while i<length:
    if lst.count(lst[i])>1:
        del lst[i]
        i-=1
        length-=1
    i+=1
print(length)
lst = list(map(str,lst))
print(' '.join(lst))