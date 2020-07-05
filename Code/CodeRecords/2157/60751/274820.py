str_=input()
a=0
result=0
i=0
while(i<len(str_)):
    if str_[i] == "C":
        if i < len(str_) - 1 and str_[i + 1] == "D":
            result += 400
            str_ = str_[0:i] + str_[i + 2:len(str_)]
        if i < len(str_) - 1 and str_[i + 1] == "M":
            result += 900
            str_ = str_[0:i] + str_[i + 2:len(str_)]
        if i>=len(str_):
            i=0
    if str_[i] == "X":
        if i < len(str_) - 1 and str_[i + 1] == "L":
            result += 40
            str_ = str_[0:i] + str_[i + 2:len(str_)]
        if i < len(str_) - 1 and str_[i + 1] == "C":
            result += 90
            str_ = str_[0:i] + str_[i + 2:len(str_)]
        if i>=len(str_):
            i=0
    if str_[i]=="I":
        if i<len(str_)-1 and str_[i+1]=="V":
            result+=4
            str_=str_[0:i]+str_[i+2:len(str_)]
        if i < len(str_) - 1 and str_[i + 1] == "X":
            result += 9
            str_ = str_[0:i] + str_[i + 2:len(str_)]
        if i>=len(str_):
            i=0
    i+=1
for i in str_:
    if i=="I":
        result+=1
    elif i=="V":
        result+=5
    elif i=="X":
        result+=10
    elif i=="L":
        result+=50
    elif i=="C":
        result+=100
    elif i=="V":
        result+=500
    else:
        result+=1000
print(result)
