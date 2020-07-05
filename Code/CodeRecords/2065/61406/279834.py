def atoi(source):
    if source.isdigit():
        if int(source)>pow(2,31)-1:
            return pow(2,31)-1
        return int(source)
    if source[0]=='+':
        source = source.lstrip("+")
    #if source[0]=='-':
    if source[0]!='+' and source[0]!='-' and not source[0].isdigit():
        return 0
    index = len(source)
    for i in range(0,len(source)):
        if not source[i].isdigit() and i!=0:
            index = i
            break
    source = source[:index]
    number = int(source)
    if number>pow(2,31)-1:
        return pow(2,31)-1
    if number<-pow(2,31):
        return -pow(2,31)
    return number


source = input().lstrip(" ")
print(atoi(source))