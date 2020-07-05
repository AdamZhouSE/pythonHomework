s = input()


def cal(string):
    i = 0
    result = ""
    while i < len(string):
        if ord("0") <= ord(string[i]) <= ord("9"):
            num = ""
            while ord("0") <= ord(string[i])<=ord("9"):
                num += string[i]
                i += 1
            result += int(num) * cal(string[i:])
            return result
        elif string[i] == "[":
            count = 1
            start = i
            i += 1
            while count != 0:
                if string[i] == "[":
                    count += 1
                if string[i] == "]":
                    count -= 1
                i += 1
            result += cal(string[start+1:i-1])
        else:
            result += string[i]
            i += 1
    return result


print(cal(s),end = "")



#[3[7AB[2PIK]][10O]]

#ABPIKPIKPIKABPIKPIKPIKABPIKPIKPIKABPIKPIKPIKABPIKPIKPIKABPIKPIKPIKABPIKPIKPIKABPIKPIKPIKOOOOOOOOOOOABPIKPIKPIKABPIKPIKPIKABPIKPIKPIKABPIKPIKPIKABPIKPIKPIKABPIKPIKPIKABPIKPIKPIKABPIKPIKPIKOOOOOOOOOOOABPIKPIKPIKABPIKPIKPIKABPIKPIKPIKABPIKPIKPIKABPIKPIKPIKABPIKPIKPIKABPIKPIKPIKABPIKPIKPIKOOOOOOOOOOOABPIKPIKPIKABPIKPIKPIKABPIKPIKPIKABPIKPIKPIKABPIKPIKPIKABPIKPIKPIKABPIKPIKPIKABPIKPIKPIKOOOOOOOOOOO
#ABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKOOOOOOOOOOABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKOOOOOOOOOOABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKOOOOOOOOOO
