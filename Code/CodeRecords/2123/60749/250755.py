n=int(input())
def findsquarenumber(num):
    i=1
    while num>=i*i:
        if num<=(i+1)*(i+1):
            return i
        i+=1
squarenumber=findsquarenumber(n)
if n==squarenumber*squarenumber:
    print(True)
else:
    print(False)