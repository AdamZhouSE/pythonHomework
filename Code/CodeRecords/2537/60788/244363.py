def find_kth_max(li,k):
    new_li=li[0:k]
    rest=li[k:]
    new_li.sort(reverse=True)
    for ele in rest:
        if ele>li[k-1]:
            new_li.pop()
            new_li.append(ele)
            new_li.sort(reverse=True)
    return new_li[k-1]


a=input()
c=a[1:len(a)-1].split(',')
d=[int(x) for x in c]
b=int(input())
print(find_kth_max(d,b))
        
    