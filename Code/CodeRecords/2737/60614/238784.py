arr = input()
num = [int(n) for n in arr[1:-1].split(",")]
keyLen=int(len(num)/3)
result=[]
while num!=[]:
    key=num.pop(0)
    count=1
    i=0
    j=len(num)
    while i<j:
        if num[i]==key:
            del(num[i])
            count+=1
            j-=1
            i-=1
        i+=1
    if count>keyLen:
        result.append(key)
print(result)