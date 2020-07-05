num_list=list(map(int,input().split()))
m=num_list[0]
n=num_list[1]
position_list=[]
string_list=list(input().split())
index=0
for i in range(m):
    num_i=(ord(string_list[-3])-ord('A'))*32*32+(ord(string_list[-2])-ord('A'))*32+ord(string_list[-1])-ord('A')
    index=num_i%n
    if position_list.count(index)==0:
        position_list.append(index)
    else:
        for j in range(1,n):
            index+=j*j
            if position_list.count(index)==1:
                index-=2*j*j
                if position_list.count(index)==1:
                    index+=j*j
                    continue
            position_list.append(index)
            break
print(position_list)
               

                
            
        
    
    
    