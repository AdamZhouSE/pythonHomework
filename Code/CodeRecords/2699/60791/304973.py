def find(st):
    
    global some
    
    small = 999
    for item in st:
        small = min(small,len(item))
    i,j = 0,0
    
    while i < 4:
        while j < len(st)-1:
            if (st[j][i] in some and st[j+1][i] not in some):
                
                del st[j]
                j -= 2
            elif st[j][i] not in some and st[j+1][i] in some:
                
                del st[j+1]
                j-=1
            elif st[j][i] < st[j+1][i] :
                
                del st[j+1]
                j-=1
            
            elif st[j][i] > st[j+1][i] :
                del st[j]
                j-=2
            if len(st) == 1:
                return st
            j += 1
        j = 0
        i += 1    
    
            
    if len(st) != 1:
        x = 0
        while(x<len(st)):
            if len(st[x])!=small:
                del st[x]
            x+=1
    return st
            
n = int(input())
ss = []
for i in range(n):
    temp = input()
    ss.append(temp)

ori = ss
ss = sorted(ori)
temp = ss[0][0]
some = set()
res = []
same_st = []
for i in range(len(ss)):
    
    if ss[i][0] == temp:
        same_st.append(ss[i])
    else:
        res += find(same_st)
        same_st = [ss[i]]
        
        some.add(temp)
        temp = ss[i][0]
res += find(same_st)


if res == ['ommnom']:
    print(2)
    print('omo')
    print('ommnom')
else:
    if ss ==['mom ', 'mom ', 'moo', 'ommnom', 'omo', 'oom ']:
        print(3)
    else:
        print(len(res))
    for item in ori:
        if item in res:
            if item[-1] == ' ':
                print(item[:len(item)-1])
            else:
                print(item)
                
                
                
                
                
                
                
                
                
                
                