def solu(strings):
    result = []
    for string in strings:
        param1 = string[0]
        param2 = string[3]
        if (string[1] == '!'):
            if(not find(result,param1,param2)):
                return False
        else:
            if(len(result) == 0):
                result.append([param1,param2])
            else:
                for res in result:
                    if(param1 in res and param2 in res):
                        continue
                    elif(param1 in res):
                        res.append(param2)
                    elif(param2 in res):
                        res.append(param1)
                    else:
                        res.append([param1,param2])
    return True

def sortBy2(string):
    return string[1]

def find(result,param1,param2):
    for res in result:
        if(param1 in res and param2 in res):
            return False
    return True

strings = input()
strings = "".join(strings.split(" "))
strings = strings[2:-2].split("\",\"")
strings.sort(reverse= True ,key = sortBy2)
if(solu(strings)):
    print("true")
else:
    print("false")
