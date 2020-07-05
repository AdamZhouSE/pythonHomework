import math
n = int(input())
#print(n)

def to_ascii(s):  #返回ASCII数组
    li = []
    for i in s:
        li.append(ord(i))
    return li
def is_re(li): #是否有重复的
    flag = False
    for i in range(math.ceil(len(li)/2)):
        for j in range(len(li)):
            if(i != j):
                if(li[i] == li[j]):
                    flag = True
    return flag


for i in range(n):
    inp = input().lower()
    to_asc = to_ascii(inp)
    #print(to_asc)
    #print(type(to_asc[0]))
    result = []
    if(is_re(to_asc)):  
        for i in range(len(to_asc)-1):
            for j in range(i,len(to_asc)):
                if(i != j):
                    if(to_asc[i] == to_asc[j]):
                        #print("i{0} , j{1}".format(i,j))
                        if(j!=i+1):
                            temp = j-i-1 
                            result.append(temp)
                        if(j == i+1):
                            result.append(0)                     
        if(result):
            print(max(result))
        else:
            print("-1")
    else:
        print("-1")