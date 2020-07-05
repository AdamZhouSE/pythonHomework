import functools

def mycmp(a, b):
    index1 = -1
    index2 = -1
    if a in str1:
        index1 = str1.index(a)
    if b in str2:
        index2 = str1.index(b)
    return index1 - index2


str1 = input()
str2 = input()
print("".join(sorted(str2,key=functools.cmp_to_key(mycmp))))