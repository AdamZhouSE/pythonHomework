dictionary=eval(input())
conjunctions=[]
def search(str,n):
    global dictionary
    if(str==''):
        if(n>1):
            return True
        else:
            return False
    for i in range(len(str)):
        if(str[:i+1] in dictionary):
            n+=1
            if(search(str[i+1:],n)):
                return True
            n-=1
    return False
for i in dictionary:
    if(search(i,0)):
        conjunctions.append(i)
print(conjunctions)