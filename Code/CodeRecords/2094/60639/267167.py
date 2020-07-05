def wrongForm(s):
    arr=[s[i] for i in range(len(s))]
    if arr.count('.')>1:
        return 1
    if arr.count(' ')>0:
        return 1
    for i in range(len(arr)):
        if arr[i].isalpha() and arr[i]!='e':
            return 1
        if (arr[i]=='+' or arr[i]=='-') and i==1:
            return 1
    return 0
string=input()
print(wrongForm(string)!=1)
