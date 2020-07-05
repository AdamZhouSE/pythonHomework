str1=input()
str1=str1.strip("[")
str1=str1.strip("]")
str1=list(map(int,str1.split(",")))
str1=sorted(str1)
def find(nums):
    res=[]
    for h in range(1,len(nums)+2):
        res.append(h)
    for t in res:
        if not t in nums:
            return t
print(find(str1))