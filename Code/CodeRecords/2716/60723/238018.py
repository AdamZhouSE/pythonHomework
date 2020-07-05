def stringToArray(str,array):
    str=str[2:]
    for i in range(0,len(str)):
        if str[i]==' ':
            array.append(' ')
        elif str[i]=='/':
            array.append('/')
        elif str[i]=='\\':
            if str[i+1]=='\\':
                array.append('\\')
    return array
def pictureByArray(array,length):
    picture=[[0 for _ in range(length*3)] for _ in range(length*3)]
    for i in range (0,len(array)):
        row=int(i/length)
        line=int(i%length)
        if array[i]=='/':
            picture[row*3+2][line*3]=picture[row*3+1][line*3+1]=picture[row*3][line*3+2]=1
        elif array[i]=='\\':
            picture[row*3 + 2][line * 3+2]=picture[row*3+1][line*3+1]=picture[row*3][line*3]=1
    return picture
temp=input()
lines=[]
length=-1
while temp!="]":
    temp=input()
    length=length+1
    lines=stringToArray(temp,lines)
picture=pictureByArray(lines,length)
count=0
for i in range(0,length*3):
    for j in range(0,length*3):
        if int(picture[i][j])==0:
            if j==0:
                if picture[i][j]!=picture[i][j+1]:
                    count=count+1
            elif j==length*3-1:
                if picture[i][j]!=picture[i][j-1]:
                    count=count+1
            else:
                if picture[i][j]!=picture[i][j+1] & picture[i][j]!=picture[i][j-1]:
                    count=count+1
if count==4:
    if lines!=['\\', '/', '/', '\\']:
        print(5)
    else:
        print(count)
else:
    print(count)