from collections import Counter

def pri(string):
    left,right = 0,0
    res = len(string)
    window = []
    arr = []
    for i in range(len(string)):
        arr.append(string[i])
    kinds = dict(Counter(arr))
    while(right <len(string)):
        window.append(string[right])
        right+=1
        while(able(window,kinds)):
            res = min(len(window),res)
            left+=1
            window = window[1:]
    print(res)
    return res
    
def able(window,kinds):
    kind = []
    for key in kinds.keys():
        kind.append(key)
    count = 0
    for item in window:
        if(len(kind)==0):
            break
        for key in kind:
            if(item == key):
                kind.remove(item)
                break
    if(len(kind) == 0):
        return True
    else:
        return False
    





T = int(input())
x = 0
strings = []
while(x<T):
    strings.append(input())
    x+=1
for string in strings:
    result = pri(string)