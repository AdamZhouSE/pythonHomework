import re
list=re.findall(r"[a-z]{1,}",input())
#print(list)
nums_boy=0
nums_girl=0
for str in list:
    for i in range(0,len(str)):
        if(str[i]=='b'):
            if(str[i+1]=='o'):
                continue
            nums_boy+=1
        elif(str[i]=='o'):
            if (str[i+1] == 'y'):
                continue
            nums_boy += 1
        elif(str[i]=='y'):
            nums_boy+=1
        elif (str[i] == 'g'):
            if (str[i+1] == 'i'):
                continue
            nums_girl += 1
        elif (str[i] == 'i'):
            if (str[i+1] == 'r'):
                continue
            nums_girl += 1
        elif (str[i] == 'r'):
            if (str[i+1] == 'l'):
                continue
            nums_girl += 1
        elif (str[i] == 'l'):
            nums_girl += 1
print(nums_boy)
print(nums_girl,end="")