str1=input().split(" ")
n=int(str1[0])
m=int(str1[1])

for i in range(n):
    temp=input()
    if 'B' in temp:
        x_temp=temp.index('B')
        j=x_temp
        while j<m and temp[j]=='B':
            j=j+1
        Midlength=(j-x_temp)//2
        print(i+1+Midlength,x_temp+1+Midlength)
        break