start=input()
end=input()
words=eval(input())
out=[]
def deep(current,temp):
    temp.append(current)
    if current==end:
        out.append(temp)
        return
    if out!=[]:
        for i in out:
            if len(temp)>len(i):
                return
    for i in words:
        if(i!=current and i not in temp):
            count=0
            for j in range(len(i)):
                if(i[j]==current[j]):
                    count+=1
            if count==2:
                deep(i,temp.copy())
deep(start,[])
if(len(out)>0):
    min_size=len(out[0])
    for i in out:
        if len(i)<min_size:
            min_size=len(i)
    result=[]
    for i in out:
        if len(i)==min_size:
            result.append(i)
    print(result)
else:
    print([])