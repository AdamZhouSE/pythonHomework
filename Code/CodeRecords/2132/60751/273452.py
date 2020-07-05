def delete(str_,letter):
    for i in range(len(str_)):
        if letter==str_[i]:
            str_=str_[0:i]+str_[i+1:len(str_)]
            break
    return str_
str_=input()
l=[]
if "z" in str_:
    l.append(0)
    str_=delete(str_,"e")
    str_ = delete(str_, "r")
    str_ = delete(str_, "o")
if "g" in str_:
    l.append(8)
    str_ = delete(str_, "e")
    str_=delete(str_,"i")
    str_=delete(str_,"h")
    str_ = delete(str_, "t")
if "u" in str_:
    l.append(4)
    str_ = delete(str_, "f")
    str_=delete(str_,"o")
    str_=delete(str_,"r")
if "f" in str_:
    l.append(5)
    str_ = delete(str_, "i")
    str_=delete(str_,"v")
    str_=delete(str_,"e")
if "v" in str_:
    l.append(7)
    str_ = delete(str_, "s")
    str_=delete(str_,"e")
    str_=delete(str_,"e")
    str_ = delete(str_, "n")
if "s" in str_:
    l.append(6)
    str_=delete(str_,"i")
    str_=delete(str_,"x")
if "w" in str_:
    l.append(2)
    str_ = delete(str_, "t")
    str_=delete(str_,"o")
if "t" in str_:
    l.append(3)
    str_ = delete(str_, "h")
    str_=delete(str_,"r")
    str_=delete(str_,"e")
    str_ = delete(str_, "e")
if "o" in str_:
    l.append(1)
    str_ = delete(str_, "n")
    str_=delete(str_,"e")
if "n" in str_:
    l.append(9)
    str_ = delete(str_, "i")
    str_=delete(str_,"n")
    str_=delete(str_,"e")
l.sort()
str__=""
for i in l:
    str__+=str(i)
print(str__)