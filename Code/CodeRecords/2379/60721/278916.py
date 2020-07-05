instr=list(input())
if "G" not in instr :
    print(True)
elif(instr.count("L")==instr.count("R")):
    print(False)
else:
    print(True)