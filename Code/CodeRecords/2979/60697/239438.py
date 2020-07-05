array=input().split(' ')
maxstring=""
maxsize=0
for i in array:
    if(len(i)>maxsize):
        maxstring=i
        maxsize=len(i)
print(maxstring)