num=input().split(",")
def result(num):
    if len(num)==0:
        return ""
    if len(num)==1:
        return num[0]
    if len(num)==2:
        return num[0]+"/"+num[1]
    result_=num[0]+"/("
    for i in range(1,len(num)):
        result_+=num[i]
        if i!=len(num)-1:
            result_+="/"
    result_+=")"
    return result_
print(result(num))