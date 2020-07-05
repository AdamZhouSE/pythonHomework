i=''.join([x for x in input().split(',')])
target=str(input())
if i.find(target)==6:
    print([-1,-1])
else:
    
    print([i.find(target),i.rfind(target)])