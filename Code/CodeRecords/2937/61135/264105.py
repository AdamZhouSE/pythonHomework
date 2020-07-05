input=input()
str='CODEFESTIVAL2016'
num=0
for t in range(0,16):
    if input[t]!=str[t]:
        num=num+1
print(num,end='\n')
    