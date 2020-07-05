string=input().replace("\\","")
def partition(string):
    res=[]
    if "+" not in string and "-" not in string and "*" not in string:
        res.append(int(string))
        return res
    for i in range(len(string)):
        if string[i]=="+" or string[i]=="-" or string[i]=="*":
            for left in partition(string[0:i]):
                for right in partition(string[i+1:]):
                    if string[i]=="+":
                        res.append(left+right)
                    elif string[i]=="-":
                        res.append(left-right)
                    else:
                        res.append(left*right)
    return res

print(partition(string))