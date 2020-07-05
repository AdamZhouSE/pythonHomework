delete=input()
try:
    while True:
        line=input()
        if delete=='"H"' or delete=="'H'":
            delete="H"
        print(line.replace(delete,"").replace(" ",""))
except EOFError:
    pass




