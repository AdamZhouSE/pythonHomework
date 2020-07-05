n = int(input())
lst = input().split(' ')
lst = ''.join(lst)
count = 0
while lst.find('101')>0:
    lst = lst.replace('101','100',1)
    count+=1
print(count)