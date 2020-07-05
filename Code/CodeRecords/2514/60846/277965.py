def func(substr,str):
    for ch in substr:
        if ch not in str: return False
    return True
if func(input(),input()): print("True")
else: print("False")    