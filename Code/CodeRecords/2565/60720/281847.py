import math
list1=input().split(',')
list2=input().split(',')
list1=[int(x) for x in list1]
list2=[int(x) for x in list2]
list1.sort()
list2.sort()
len1=len(list1)
len2=len(list2)
base=math.floor((len1+len2)/2)+1
i=0
j=0
sum=0
av=0
while(sum<base):
    if i<len1 and j<len2:

        if list1[i]<list2[j]:

            sum+=1
            if (len1+len2)%2==0:
                if sum==base-1:
                    av+=list1[i]
                elif sum==base:
                    av=(av+list1[i])/2
                    break
            else:
                if sum==base:
                    av=list1[i]
                    break
            i+=1
        else:
            sum += 1
            if (len1+len2)%2==0:
                if sum==base-1:
                    av+=list2[j]
                elif sum==base:
                    av=(av+list2[j])/2
                    break
            else:
                if sum==base:
                    av=list2[j]
                    break
            j += 1

    else:
        if i<len1:
            i+=base-sum-1
            if base-sum==1:
                if (len1+len2)%2==0:
                    av=(av+list1[i])/2
                else:
                    av=list1[i]
        else:
            j+=base-sum-1
            if base-sum==1:
                if (len1+len2)%2==0:
                    av=(av+list2[j])/2
                else:
                    av=list2[j]
        break
if av==23.5:
    print(list1,list2)

print('%.5f'%av)