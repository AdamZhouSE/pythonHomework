def find(string1,string2):
    if(string2 == "" or len(string1) < len(string2)):
        return 0
    for x in range(len(string1)):
        if(string1[x] == string2[0]):
            if(len(string2)==1):
                return 1 + find(string1[x+1:],string2)
            a = find(string1[x+1:],string2[1:])
            b = find(string1[x+1:],string2)
            return a + b
    return 0

n = eval(input())
while(n!=0):
    n = n - 1
    input()
    string = input()
    string = string.split(" ")
    print(find(string[0],string[1]))