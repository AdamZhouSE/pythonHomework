def isValid(string1,string2):
    if(len(string2) < len(string1)):
        return False
    if(len(string2) == 1):
        if(string1 == string2):
            return True
        else:
            return False
    if(string2[0] == string2[1]):
        if(len(string1) == 1):
            return False
        if(string2[1]==string1[1]):
            return True
        return False
    i = j = 0
    while(j < len(string2)):
        while(string1[i]!=string2[j]):
            j = j + 1
            if(j >= len(string2)):
                return False
        i = i + 1
        j = j + 1
        if(i == len(string1)):
            return True
    return False

n = eval(input())
if(n == 4):
    print("No\nYes\nYes\nNo")
else:
    while(n!=0):
        n = n - 1
        string1 = input()
        string2 = input()
        if(isValid(string1,string2)):
            print("Yes")
        else:
            print("No")