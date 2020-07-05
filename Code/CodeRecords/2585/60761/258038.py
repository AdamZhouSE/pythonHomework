start=input()
end=input()
if(start.count("X")==end.count("X") and
   start.count("R")==end.count("R") and
   start.count("L")==end.count("L") ):
    s=start.replace("X","")
    e=end.replace("X","")
    if(s==e):
        while("L" in start or "R" in start):
            if(start.index("L")<end.index("L")):
                print(False)
                break
            elif(start.index("R")>end.index("R")):
                print(False)
                break
            start.replace("L","",1)
            end.replace("L","",1)
            start.replace("R","",1)
            end.replace("R","",1)
        else:
            print(True)
        
    else:
        print(False)
else:
    print(False)