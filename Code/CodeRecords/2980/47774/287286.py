tar=str(input())
op=input().split()
if(op[0]=='D'):
    index=tar.find(op[1])
    if index==-1:
        print('no exist')
        print(tar)
    else:        
        res = tar[:index] + tar[index+len(op[1]):]
        print(res)
elif(op[0]=='I'):
    index=tar.rfind(op[1])#查找最后一个
    if index==-1:
        print('no exist')
        print(tar)
    else:
        res=tar[:index]+op[2]+tar[index:]
        print(res)
elif(op[0]=='R'):
    index=tar.rfind(op[1])#查找最后一个
    if index==-1:
        print('no exist')
        print(tar)
    else:
        res=tar.replace(op[1],op[2])
        print(res)
        
        
        
        
    