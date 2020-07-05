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
        isValid(pattern,string)
    except:
        break