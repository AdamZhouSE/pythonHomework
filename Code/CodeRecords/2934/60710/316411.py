def unZip(string,i):
    result=""
    while i<len(string):
        if string[i]=='[':
            integer=""
            i=i+1
            while ord('9') >= ord(string[i]) >= ord('0'):
                integer=integer+string[i]
                i=i+1
            temp=unZip(string,i)
            for a in range(0,int(integer)):
                result=result+temp[0]
            i=temp[1]
        else:
            if string[i]==']':
                return [result,i]
            else:
                result=result+string[i]
        i=i+1
    return [result,i]

res=unZip(input(),0)[0]
print(res,end="")