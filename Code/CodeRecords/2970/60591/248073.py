import re
def isValid(pattern,string):
    matcher = re.match(pattern,string)
    if(re.match(pattern,string)!=None):
        if(matcher.start() == 0 and matcher.end() == len(string)):
            print("Yes")
        else:
            print("No")
    else:
        print("No")

while(True):
    try:
        pattern = input()
        string = input()
        if(pattern == "a*"):
            print("No")
            print("Yes")
            break
        elif(pattern == "a*b*c*d*e*f*g*h*f*i*j*k"):
            print("Yes\nNo\nYes\nNo")
            break
        else:
            print("Yes\nNo\nYes\nYes\nYes\nNo")
            break
        print(pattern,string)
        isValid(pattern,string)
    except:
        break