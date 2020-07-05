def search(li,target):
    if len(li)==0:
        return False
    if len(li)==1:
         return li[0]==target
    if li[0]<li[len(li)-1]:
        return binary_search(li,target)
    else:
        return search(li[0:int(len(li)/2)],target) or search(li[int(len(li)/2):],target)
            
        
def binary_search(li,target):
    if len(li)==0:
        return False
    if len(li)==1:
        return li[0]==target
    else:
        return binary_search(li[0:int(len(li)/2)],target) or binary_search(li[int(len(li)/2):],target)
            
          
s=[int(x) for x in input().split(',')]
t=int(input())
print(search(s,t))
