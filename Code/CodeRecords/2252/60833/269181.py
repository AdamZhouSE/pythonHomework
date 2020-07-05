lines=[]
while True:
    try:
        lines.append(input())
    except:
        break
n=int(lines.pop(0))
for i in range(0,n):
    str1=list(lines.pop(0))
    target_str=list(lines.pop(0))
    target_str.sort()
    s1=len(target_str)
    s2=len(str1)
    result=0
    for j in  range(0,s2-s1+1):
        temp=str1[j:j+s1]
        temp.sort()
        if temp==target_str:
            result=result+1
    print(result)