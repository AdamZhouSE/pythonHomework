start=input()
end=input()
i=0
j=0
c=0
while i<len(start) and j<len(end):
    while i<len(start) and start[i:i+1]=='X':
        i=i+1
    while j<len(end) and end[j:j+1]=='X':
        j=j+1
    if(start[i:i+1]!=end[j:j+1]):
        print("False")
        c=1
        break

    if(start[i:i+1]=='R'==end[j:j+1] and i>j):
        print("False")
        c=1
        break

    if(start[i:i+1]=='L'==end[j:j+1] and i<j):
        print('False')
        c=1
        break
    i=i+1
    j=j+1
if(c==0):
    print('True')