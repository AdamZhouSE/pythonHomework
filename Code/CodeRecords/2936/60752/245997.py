def translate(phone):
    rs=''
    for a in list(phone):
        add=''
        if 'ABC'.find(a)!=-1:add='2'
        if 'DEF'.find(a)!=-1:add='3'
        if 'GHI'.find(a)!=-1:add='4'
        if 'JKL'.find(a)!=-1:add='5'
        if 'MNO'.find(a)!=-1:add='6'
        if 'PRS'.find(a)!=-1:add='7'
        if 'TUV'.find(a)!=-1:add='8'
        if 'WXY'.find(a)!=-1:add='9'
        else: add=a
        rs=rs+add
    return rs

num=int(input())
book=[]
inputs=[]
for n in range(num):
    phone=''.join(input().split('-'))
    inputs.append(phone)
    if not phone.isnumeric():phone=translate(phone)
    
    has = False
    for p in book:
        if p[0]==phone[0:3]+'-'+phone[3:]:
            
            p[1]+=1
            has=True
        if has:break
    if not has:
        
        book.append([phone[0:3]+'-'+phone[3:],1])
        

has=False
for p in book:
    if p[1]>1:
        print(' '.join(map(str,p)))
        has=True
if not has:
    print('No duplicates.',end='')


