nums=eval(input())
target=eval(input())
try:
    index=nums.index(target)
except:
    index=-1
print(index)