def solution():
    temp=input()
    i=0
    while len(str(pow(2,i)))<=len(temp):
        if same_or_not(i,temp):
            return True
        i=i+1
    return False
def same_or_not(i,temp):
    string=str(pow(2,i))
    if len(string)!=len(temp):
        return False
    for i in range(len(temp)):
        if temp.count(string[i])!=string.count(string[i]):
            return False
    return True
print(str(solution()).lower())