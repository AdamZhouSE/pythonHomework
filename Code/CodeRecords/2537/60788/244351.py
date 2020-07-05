def find_kth_max(li,k):
    new_li=li[0:k]
    rest=li[k:]
    new_li.sort(reverse=False)
    for ele in rest:
        if ele>li[k-1]:
            new_li.pop()
            new_li.append(ele)
            new_li.sort(reverse=False)
    return new_li[k-1]


a=input()
print(find_kth_max(a))
        
    