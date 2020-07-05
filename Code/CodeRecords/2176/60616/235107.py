str1=input()
n=len(str1)
dict={}
for i in range (n):
    dict[str1[i:]]=i+1
newDict=sorted(dict.items(), key=lambda d: d[0], reverse=False)
arr=[]
for key,value in newDict:
    arr.append(value)
print(" ".join(str(i) for i in arr))