def charRE(string:str,k:int):
    if  len(string)==0: return 0
    left = 0
    right = 0
    char_max = 0
    dicts = {}
    for right in range(len(string)):
        dicts.setdefault(string[right], 0)
        dicts[string[right]]+=1
        char_max = max(char_max,dicts[string[right]])
        if right-left+1 > char_max+k:
            dicts[string[left]]-=1
            left+=1
    return len(string)-left
strs = input()
k = int(input())
index = charRE(strs,k)
print(index)