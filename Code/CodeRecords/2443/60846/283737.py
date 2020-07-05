from functools import cmp_to_key
def mycmp(s1,s2):
    if s1[0]==s2[0]:
        if len(s1)>len(s2):
            return ord(s1[0])-ord(s1[len(s2)])
        elif len(s1)<len(s2):
            return ord(s2[len(s1)])-ord(s2[0])
        else: return int(s2)-int(s1)
    # a=ord(s1[0])
    # b=ord(s2[0])
    # return b-1
    return int(s2[0])-int(s1[0])
def f(snums):
    snums.sort(key=cmp_to_key(mycmp))
    ret=int(snums[0])
    for i in range(1,len(snums)):
        ret=ret*pow(10,len(snums[i]))+int(snums[i])
    return ret
nums=eval(input())
snums=[]
for num in nums:
    snums.append(str(num))
print(f(snums))