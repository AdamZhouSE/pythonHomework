row=0;
con=0;
for i in range(5):
    string=input();
    if "1" in string:
        row=i+1;
        con=string.find("1")-string.find("1")/2+1;
        break;
print(int(abs(row-3)+abs(con-3)));