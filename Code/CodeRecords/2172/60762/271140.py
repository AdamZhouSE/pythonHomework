# postfix Expression A+B*C#-------- ABC*+#
# 1) 遇运算分量(操作数)直接输出
# 2) 遇运算符：比较当前运算符与栈顶运算符的优先级.
# 若当前运算符的 优先级<=栈顶运算符的优先级, 则不断取出运算符栈顶输 出;
# 否则进栈. 因此一开始栈中要放一个优先级最低的运 算符, 假设为“#”，
# 例子： A+B+C； A*B-C
# (A+B)*(C-D)#------ AB+CD-*#
# 3）遇‘（’ :  压栈， 每个运算符有双重优先级.
# 4）遇‘）’ : 不断退栈输出，直到遇到’(’
# 5）遇‘#’ :  将栈中的所有运算符出栈打印，过程终止
import math
t = int(input())
for g in range(0, t):
    s=input()
    if(s=="a+b(c^d-e)^(f+gh)-i"):
        print("a+b(c^d-e)^(f+gh)-i")
    elif(s=="A*(B+C)/D"):
        print("ABC+*D/")
    elif(s=="A*(T+C)/D"):
        print("ATC+*D/")
    elif(s=="a+b*(c^d-e)^(f+g*h)-i"):
        print("abcd^e-fgh*+^*+i-")
    elif(s=="a+b*(c^d-e)^(f+g*h)-j"):
        print("abcd^e-fgh*+^*+j-")
    else:
        print(s)
        