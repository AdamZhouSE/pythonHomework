lst=''.join(input().split(','))
find=input()
lst+=find
lst=list(lst)
lst.sort()
lst=''.join(lst)
print(lst.find(find))
    