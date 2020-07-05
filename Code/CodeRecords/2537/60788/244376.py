def find_kth_max(li,k):
    li.sort(reverse=True)
    return li[k-1]


a=input()
c=a[1:len(a)-1].split(',')
d=[int(x) for x in c]
b=int(input())
print(find_kth_max(d,b))
        
    