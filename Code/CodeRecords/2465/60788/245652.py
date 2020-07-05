def f(s,li):
    return li[len(li) - s - 1] <= s <= li[len(li) - s]

def cal_h(li):
    return binary_search([x for x in range(1,len(li)+1)],li)
    
def binary_search(s,li):
    if len(s)==1 and f(s[0],li):
        return s[0]
    else:
        if f(s[int(len(s)/2)],li):
            return binary_search(s[int(len(s)/2):],li)
        else:
            return binary_search(s[0:int(len(s)/2)],li)
        
        
s=[int(x) for x in input().split(',')]
print(cal_h(s))