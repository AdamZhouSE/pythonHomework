def Test():
    s=input()
    d={"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    line=[]
    def check02468(s):
        if(s.find("z")!=-1):
            s=s[:s.find("z")]+s[s.find("z")+1:]
            s = s[:s.find("e")] + s[s.find("e") + 1:]
            s = s[:s.find("r")] + s[s.find("r") + 1:]
            s = s[:s.find("o")] + s[s.find("") + 1:]
            line.append("zero")
        if(s.find("w")!=-1):
            s = s[:s.find("t")] + s[s.find("t") + 1:]
            s = s[:s.find("w")] + s[s.find("w") + 1:]
            s = s[:s.find("o")] + s[s.find("o") + 1:]
            line.append("two")
        if(s.find("u")!=-1):
            s = s[:s.find("f")] + s[s.find("f") + 1:]
            s = s[:s.find("o")] + s[s.find("o") + 1:]
            s = s[:s.find("u")] + s[s.find("u") + 1:]
            s = s[:s.find("r")] + s[s.find("r") + 1:]
            line.append("four")
        if(s.find("x")!=-1):
            s = s[:s.find("s")] + s[s.find("s") + 1:]
            s = s[:s.find("i")] + s[s.find("i") + 1:]
            s = s[:s.find("x")] + s[s.find("x") + 1:]
            line.append("six")
        if(s.find("g")!=-1):
            s = s[:s.find("e")] + s[s.find("e") + 1:]
            s = s[:s.find("i")] + s[s.find("i") + 1:]
            s = s[:s.find("g")] + s[s.find("g") + 1:]
            s = s[:s.find("h")] + s[s.find("h") + 1:]
            s = s[:s.find("t")] + s[s.find("t") + 1:]
            line.append("eight")
        return s
    def check1357(s):
        if(s.find("o")!=-1):
            s = s[:s.find("o")] + s[s.find("o") + 1:]
            s = s[:s.find("n")] + s[s.find("n") + 1:]
            s = s[:s.find("e")] + s[s.find("e") + 1:]
            line.append("one")
        if (s.find("r")!=-1):
            s = s[:s.find("t")] + s[s.find("t") + 1:]
            s = s[:s.find("h")] + s[s.find("h") + 1:]
            s = s[:s.find("r")] + s[s.find("r") + 1:]
            s = s[:s.find("e")] + s[s.find("e") + 1:]
            s = s[:s.find("e")] + s[s.find("e") + 1:]
            line.append("three")
        if (s.find("f")!=-1):
            s = s[:s.find("f")] + s[s.find("f") + 1:]
            s = s[:s.find("i")] + s[s.find("i") + 1:]
            s = s[:s.find("v")] + s[s.find("v") + 1:]
            s = s[:s.find("e")] + s[s.find("e") + 1:]
            line.append("five")
        if (s.find("s")!=-1):
            s = s[:s.find("s")] + s[s.find("s") + 1:]
            s = s[:s.find("e")] + s[s.find("e") + 1:]
            s = s[:s.find("v")] + s[s.find("v") + 1:]
            s = s[:s.find("e")] + s[s.find("e") + 1:]
            s = s[:s.find("n")] + s[s.find("n") + 1:]
            line.append("seven")
        return s
    def check9(s):
        if(s.find("e")!=-1):
            s = s[:s.find("n")] + s[s.find("n") + 1:]
            s = s[:s.find("i")] + s[s.find("i") + 1:]
            s = s[:s.find("n")] + s[s.find("n") + 1:]
            s = s[:s.find("e")] + s[s.find("e") + 1:]
            line.append("nine")
        return s
    s=check02468(s)
    s=check1357(s)
    s=check9(s)
    nums=[]
    for word in line:
        nums.append(d[word])
    nums.sort()
    for x in nums:
        print(x,end="")
    print("")

if __name__ == "__main__":
    Test()