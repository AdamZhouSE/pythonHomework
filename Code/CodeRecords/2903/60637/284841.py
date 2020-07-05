substr=[]
def substring(remainder,temp):
    if(len(remainder)==0):
        if(len(temp)==len(set(temp))):
            substr.append(temp)
    else:
        substring(remainder[1:],temp)
        substring(remainder[1:],temp+remainder[0])
arr=eval(input())
substring(arr,'')
list.sort(substr,key=lambda x:len(x))
print(len(substr[-1]))
