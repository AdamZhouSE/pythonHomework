row = int(input())
col = int(input())
r0 = int(input())
c0 = int(input())
result = []
length = 0

direction = 0
""" 0: East
    1: South
    2: West
    3: North
    """
pre_r = r0
pre_c = c0

result.append([r0,c0])
while len(result)<row*col:
    if direction%2==0:
        length =length+1
    for i in range(length):
        if direction%4 ==0:
            pre_c = pre_c+1
        elif direction%4 ==1:
            pre_r = pre_r+1
        elif direction%4 ==2:
            pre_c = pre_c - 1
        else:
            pre_r = pre_r - 1
        if -1<pre_c<col and -1<pre_r <row:
            result.append([pre_r,pre_c])
    direction = direction +1
print(result)
            
            
            
            
            
    

