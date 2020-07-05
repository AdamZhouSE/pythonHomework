
#不断让当前空格放的积木和目标相同即可
nums=input().split(" ")
N=int(nums[0])
M=int(nums[1])
ls=[]
standard=[]
ls_blank=[]
for i in range(N):
    s=input()
    this=[]
    for j in range(M):
        this.append(s[j])
        if s[j]=="o":
            ls_blank=[i,j]
    ls.append(this)
standard_blank=[]
for i in range(N):
    s=input()
    this=[]
    for j in range(M):
        this.append(s[j])
        if s[j]=="o":
            standard_blank=[i,j]
    standard.append(this)
result=[]
while ls_blank!=standard_blank:
    i=ls_blank[0]
    j=ls_blank[1]
    stand_char=standard[i][j]#现在标准格里那个字符
    if stand_char=="<":
        result.append("R")
        R_char=ls[i][j+1]
        if R_char=="u":
            ls[i][j+1]=">"
            ls[i-1][j+1]="o"
            ls_blank=[i-1,j+1]
        elif R_char=="n":
            ls[i][ j + 1] = ">"
            ls[i+ 1][ j + 1] = "o"
            ls_blank = [i + 1, j + 1]
        elif R_char=="<":
            ls[i][ j + 1] = ">"
            ls[i][ j +2] = "o"
            ls_blank = [i , j + 2]
        ls[i][j]="<"
    elif stand_char==">":
        result.append("L")
        L_char = ls[i][ j - 1]
        if L_char == "u":
            ls[i][j -1] = "<"
            ls[i - 1][ j - 1] = "o"
            ls_blank = [i - 1, j - 1]
        elif L_char == "n":
            ls[i][ j - 1] = "<"
            ls[i + 1][ j - 1] = "o"
            ls_blank = [i + 1, j - 1]
        elif L_char == ">":
            ls[i][ j -1] = "<"
            ls[i][ j - 2] = "o"
            ls_blank = [i, j - 2]
        ls[i][j] = ">"
    elif stand_char=="n":
        result.append("D")
        D_char=ls[i+1][j]
        if D_char=="n":
            ls[i+1][j]="u"
            ls[i+2][j]="o"
            ls_blank=[i+2,j]
        elif D_char==">":
            ls[i+1][j]="u"
            ls[i+1][j-1]="o"
            ls_blank=[i+1,j-1]
        elif D_char=="<":
            ls[i+1][j]="u"
            ls[i+1][j+1]="o"
            ls_blank=[i+1,j+1]
        ls[i][j]="n"
    elif stand_char=="u":
        result.append("U")
        U_char=ls[i-1][j]
        if U_char=="u":
            ls[i-1][j]="n"
            ls[i-2][j]="o"
            ls_blank=[i-2,j]
        elif U_char=="<":
            ls[i-1][j]="n"
            ls[i-1][j+1]="o"
            ls_blank=[i-1,j+1]
        elif U_char==">":
            ls[i-1][j]="n"
            ls[i-1][j-1]="o"
            ls_blank=[i-1,j-1]
        ls[i][j]="u"

print("".join(result))

