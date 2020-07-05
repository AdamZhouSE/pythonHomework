string_2=input()
string_3=input()
get_result=False
x=int(string_2,2)
y=int(string_3,3)
length_2=len(string_2)
length_3=len(string_3)
result=0
while not get_result:
    for i in range(length_2):
        for j in range(length_3):
            if x+2**i==y+3**j:
                get_result=True
                result=x+2**i
            elif x+2**i==y-3**j:
                get_result=True
                result=x+2**i
            elif x-2**i==y+3**j:
                get_result=True
                result=x-2**i
            elif x-2**i==y-3**j:
                get_result=True
                result=x-2**i
print(result,end="")            
        