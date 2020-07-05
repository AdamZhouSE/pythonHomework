def find_longest_consecutive_substring(li):
    max_count=0
    current_count=1
    new_li=list(set(li))
    new_li.sort(reverse=False)
    before=new_li[0]
    for ele in new_li[1:]:
        if ele-before==1:
            current_count+=1
        else:
            if current_count>max_count:
                max_count=current_count
            current_count=1
        before=ele
    if max_count>current_count:
        return max_count
    else:
        return current_count
    
a=input()
c=a[1:len(a)-1].split(',')
d=[int(x) for x in c]
print(find_longest_consecutive_substring(d))
            
        
        
        