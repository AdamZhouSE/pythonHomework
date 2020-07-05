b = 0
def go(str,i):
    dict = {}
    for subl in range(1,len(str)+1):
        for j in range(len(str)-subl+1):
            dict[str[j:j+subl]]=dict.get(str[j:j+subl],0) + 1
    for k in dict.keys():
        if dict[k] > 1:
            go(k,i+1)
    global b
    if i+1 > b:
        b = i+1
    return i+1

str = input()
go(str,0)
print(b)