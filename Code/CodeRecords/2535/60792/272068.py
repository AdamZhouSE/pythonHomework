def maxBlock(list1):
    list2=list1.copy()
    list2.sort()
    count=0
    st=0
    for i in range(0,len(list1)):
        end=i+1
        s_list1=set(list1[st:end])
        s_list2=set(list2[st:end])
        if(len(s_list1&s_list2)==end-st):
            st=i+1
            count+=1
    return count

s=input()
s=s[1:len(s)-1]
list1=list(map(int,s.split(",")))
print(maxBlock(list1))