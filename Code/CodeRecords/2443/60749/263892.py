from itertools import permutations
str1=input()
str1=str1.strip("[")
str1=str1.strip("]")
str1=str1.split(",")
def findmost(str1):
    res=[]
    for i in permutations(str1,len(str1)):
        res.append(int(''.join(i)))
    res=sorted(res)

    return res[-1]
print(findmost(str1))