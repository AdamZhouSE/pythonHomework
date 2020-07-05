str=input()
pan=0
if(str.find('X')<0):
    pan = 1
    print('False')
count1=0
count2=0
i=0
while i<11:
    if str[i]=='X':
        count1+=1
    if str[i]=='O':
        count2+=1
    i+=1
if(count1-count2>1 or count2-count1>1):
    pan = 1
    print('False')
if((str[0]=='X' and str[1]=='X' and str[2]=='X')or(str[0]=='O' and str[1]=='O' and str[2]=='O') ):
    if((str[4]=='X' and str[5]=='X' and str[6]=='X')or(str[4]=='O' and str[5]=='O' and str[6]=='O')):
        pan = 1
        print('False')
    if ((str[8] == 'X' and str[9] == 'X' and str[10] == 'X') or (str[8] == 'O' and str[9] == 'O' and str[10] == 'O')):
        pan = 1
        print('False')
if(pan==0):
    print('True')