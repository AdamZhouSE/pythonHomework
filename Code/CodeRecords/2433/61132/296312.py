import functools

def merge2(l1, l2):
    index = 0
    for j in l1:
        if j[0] <= l2[0] <=j[1]:
            l1[index]=[l1[index][0],max(l1[index][1],l2[1])]
            return l1
        elif j[0]<=l2[1]<=j[1]:
            l1[index]=[min(l1[index][0],l2[0]),l1[index][1]]
            return l1
    else:
        l1.append(l2)
        return l1


l=eval(input())
l[0]=[l[0]]
l=functools.reduce(lambda x,y:merge2(x,y),l)
print(l)