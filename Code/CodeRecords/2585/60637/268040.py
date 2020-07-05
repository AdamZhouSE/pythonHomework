import sys
def nums_x(string):
    count=0
    for i in string:
        if i=='X':
            count+=1
    return count
start=input()
end=input()
if(start.replace('X','')!=end.replace('X','')):
    print(False)
else:
    r=0
    l=0
    for i in range(0,len(start)):
        if start[i]=='R':
            for j in range(0,len(end)):
                count=0
                if(end[j]=='R'):
                    if(count==r):
                        if(nums_x(start[i+1:])<nums_x(end[j+1:])):
                            print(False)
                            sys.exit()
                    else:
                        count+=1
        r+=1
    for i in range(0,len(start)):
        if start[i]=='L':
            for j in range(0,len(end)):
                count=0
                if(end[j]=='L'):
                    if(count==l):
                        if(nums_x(start[:i])<nums_x(end[:j])):
                            print(False)
                            sys.exit()
                    else:
                        count+=1
        l+=1
    print(True)