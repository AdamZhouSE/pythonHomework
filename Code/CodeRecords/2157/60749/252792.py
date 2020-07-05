str1=input()
def RomaToNum(str1):
    dic={'I':1, 'V':5, 'X':10, 'L':100,'D':500,'M':1000}
    res=[]
    for h in str1:
        res.append(dic[h])
    max1=0
    for t in res:
        max1=max(t,max1)
    max_index=res.index(max1)
    result=0
    for h in range(0,max_index):
        result-=res[h]
    for h in range(max_index, len(res)):
        result+=res[h]
    return result
print(RomaToNum(str1))