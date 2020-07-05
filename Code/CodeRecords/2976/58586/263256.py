delete=input().replace(" ","")
try:
    while True:
        line=input()
        print(line.replace(delete,"").replace(delete.capitalize(),"")
              .replace(" ",""))
except EOFError:
    pass



