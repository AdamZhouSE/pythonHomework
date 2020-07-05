n=int(input())
text=input()

for i in range(n):
    temp=input()
    if(temp[0]=='1'):
        text+=temp[2:]
        print(text)
    if(temp[0]=='2'):
        text=text[int(temp[2]):int(temp[2])+int(temp[4])]
        print(text)
    if(temp[0]=='3'):
        text=text[:int(temp[2])]+temp[4:]+text[int(temp[2]):]
        print(text)
    if(temp[0]=='4'):
        print(text.find(temp[2:]))