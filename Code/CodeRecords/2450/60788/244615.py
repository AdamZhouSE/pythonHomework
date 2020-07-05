i=''.join([x for x in input().split(',')])
target=str(input())
print([i.find(target),i.rfind(target)])