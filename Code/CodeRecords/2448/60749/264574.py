str1=input()
str1=str1.strip("[")
str1=str1.strip("]")
str1=list(map(int,str1.split(",")))
def for_h(str1):
    h=max(t for t in str1)
    count=0
    while h>0:
        for t in str1:
            if t>=h:
                count+=1
        if h==count:
            return h
        h=h-1
        count=0
print(for_h(str1))