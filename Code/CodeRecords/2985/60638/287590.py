n=int(input())
string="A"
k=''
for i in range(2,n+1):
    if i==2:
        k='B'
    if i==3:
        k='C'
    if i==4:
        k='D'
    if i==5:
        k='E'
    if i==6:
        k='F'
    if i==7:
        k='G'
    if i==8:
        k='H'
    string=string+k+string
print(string)