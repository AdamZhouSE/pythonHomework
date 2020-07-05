nums=eval(input())
tar=int(input())
map={num:i+1  for i,num in enumerate(nums) }
diff=0
def search(tar):
    for i,num in enumerate(nums):
        diff=tar-num
        if diff in map and diff!=num:
            return [i+1,map[diff]]
    return None
print(search(tar))
        
